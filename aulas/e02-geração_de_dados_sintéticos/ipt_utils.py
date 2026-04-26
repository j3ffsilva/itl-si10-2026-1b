from collections import defaultdict
from datetime import datetime, timedelta
from html import escape
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

import pandas as pd
from IPython.display import HTML, display


def carregar_relatorios_sharepoint(caminho_xlsx: Path) -> dict[str, pd.DataFrame]:
    ns = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    caminho_xlsx = Path(caminho_xlsx)

    def coluna_excel_para_indice(coluna: str) -> int:
        indice = 0
        for caractere in coluna:
            if caractere.isalpha():
                indice = indice * 26 + (ord(caractere.upper()) - 64)
        return indice - 1

    def ler_shared_strings(arquivo_zip: ZipFile) -> list[str]:
        raiz = ET.fromstring(arquivo_zip.read("xl/sharedStrings.xml"))
        return [
            "".join(texto.text or "" for texto in item.iterfind(".//main:t", ns))
            for item in raiz.findall("main:si", ns)
        ]

    def valor_celula_excel(celula, shared_strings: list[str]) -> str:
        tipo = celula.attrib.get("t")
        valor = celula.find("main:v", ns)
        if tipo == "s":
            return shared_strings[int(valor.text)] if valor is not None else ""
        if tipo == "inlineStr":
            bloco_inline = celula.find("main:is", ns)
            if bloco_inline is None:
                return ""
            return "".join(texto.text or "" for texto in bloco_inline.iterfind(".//main:t", ns))
        return valor.text if valor is not None else ""

    with ZipFile(caminho_xlsx) as arquivo_zip:
        shared_strings = ler_shared_strings(arquivo_zip)
        workbook = ET.fromstring(arquivo_zip.read("xl/workbook.xml"))
        rels = ET.fromstring(arquivo_zip.read("xl/_rels/workbook.xml.rels"))
        alvos = {rel.attrib["Id"]: "xl/" + rel.attrib["Target"] for rel in rels}

        abas = {}
        for aba in workbook.find("main:sheets", ns):
            rel_id = aba.attrib[
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
            ]
            alvo = alvos[rel_id]
            sheet_root = ET.fromstring(arquivo_zip.read(alvo))

            linhas = []
            for linha in sheet_root.find("main:sheetData", ns).findall("main:row", ns):
                valores = defaultdict(str)
                for celula in linha.findall("main:c", ns):
                    referencia = celula.attrib.get("r", "A1")
                    coluna = "".join(char for char in referencia if char.isalpha())
                    valores[coluna_excel_para_indice(coluna)] = valor_celula_excel(
                        celula, shared_strings
                    )

                if valores:
                    ultimo_indice = max(valores)
                    linhas.append([valores[i] for i in range(ultimo_indice + 1)])

            abas[aba.attrib["name"]] = pd.DataFrame(linhas)

    return abas


def serial_excel_para_data(numero_serial: float) -> pd.Timestamp:
    return pd.Timestamp(datetime(1899, 12, 30) + timedelta(days=float(numero_serial)))


def exibir_cartoes(titulo: str, cartoes: list[dict[str, str]]) -> None:
    html = [
        "<div style='margin: 8px 0 14px 0;'>",
        f"<div style='font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;'>{escape(titulo)}</div>",
        "<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 10px;'>",
    ]
    for cartao in cartoes:
        html.append(
            "<div style='border: 1px solid #d0d7de; border-radius: 12px; padding: 12px 14px; "
            "background: #f8fafc;'>"
            f"<div style='font-size: 0.82rem; color: #475569; margin-bottom: 6px;'>{escape(cartao['rotulo'])}</div>"
            f"<div style='font-size: 1.35rem; font-weight: 700; color: #0f172a;'>{escape(cartao['valor'])}</div>"
            f"<div style='font-size: 0.82rem; color: #334155; margin-top: 6px;'>{escape(cartao['apoio'])}</div>"
            "</div>"
        )
    html.append("</div></div>")
    display(HTML("".join(html)))


def exibir_tabela_html(df: pd.DataFrame, titulo: str) -> None:
    tabela = df.to_html(index=False, escape=False)
    bloco = (
        f"<div style='margin: 8px 0 14px 0;'>"
        f"<div style='font-size: 1.02rem; font-weight: 700; margin-bottom: 8px;'>{escape(titulo)}</div>"
        f"{tabela}</div>"
    )
    display(HTML(bloco))
