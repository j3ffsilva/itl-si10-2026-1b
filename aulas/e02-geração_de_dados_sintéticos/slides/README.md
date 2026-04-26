# Slides Template

Template de apresentações em LaTeX/Beamer com design customizado, fontes OpenType e slides prontos para uso.

## Requisitos

- [TeX Live 2024+](https://www.tug.org/texlive/) com LuaLaTeX
- Fontes incluídas no repositório (`fonts/`)

## Compilação

```bash
lualatex main.tex && lualatex main.tex
```

> Duas passadas são necessárias para que o TikZ resolva corretamente as referências de posição (`remember picture, overlay`).

---

## Estrutura do projeto

```
.
├── main.tex                  # Arquivo principal — edite aqui
├── styles/
│   └── slidesmainstyle.sty   # Pacote de estilos (não editar)
└── fonts/
    ├── Bebas_Neue/
    └── Inter-4.1/
```

---

## Como usar

No `main.tex`, carregue o pacote logo após o `\documentclass`:

```latex
\documentclass[aspectratio=169]{beamer}
\usepackage{styles/slidesmainstyle}

\begin{document}
  % slides aqui
\end{document}
```

---

## Slides disponíveis

### Capa

```latex
\coverslide{Título da Aula}{imagens/capa.jpg}{Seu Nome}{Aula 01 — Módulo X}
```

Passe `{}` no segundo argumento para omitir a imagem de fundo:

```latex
\coverslide{Título da Aula}{}{Seu Nome}{Aula 01 — Módulo X}
```

---

### Divisão de seção

```latex
\sectionslide{Nome da Seção}
```

---

### Declaração (statement)

```latex
\stmtslide{linha pequena acima}{Linha de destaque em bold}
```

Argumentos opcionais para ajuste fino de tamanho e espaçamento:

```latex
\stmtslide{contexto}{Frase de impacto}[32][40][0.5em]
%                                       ^    ^    ^
%                                    tamanho leading vspace
```

---

### Bullets

```latex
\bulletslide{Título}{Subtítulo opcional}{
  \item Primeiro item
  \item Segundo item
  \item Terceiro item
}
```

Omita o subtítulo com `{}`:

```latex
\bulletslide{Título}{}{
  \item Item
}
```

---

### Texto corrido

```latex
\textslide{Título}{Subtítulo opcional}{
  Parágrafo de texto livre, sem \textbackslash item.
  Pode ter múltiplos parágrafos.
}
```

---

### Pergunta

```latex
\questionslide{
  \ql{Qual é a diferença entre}
  \qh{null e undefined}
  \ql{no JavaScript?}
}
```

- `\ql{}` — texto apagado (roxo claro)
- `\qh{}` — texto destacado (branco)

---

### Imagem à direita

```latex
\rightimgslide{Título}{Subtítulo}{imagens/foto.jpg}{0.5}
%                                                    ^
%                                          fração da largura ocupada pela imagem
```

---

### Imagem à esquerda

```latex
\leftimgslide{Título}{Subtítulo}{imagens/foto.jpg}{0.45}
```

---

### Somente imagem

```latex
\imgslide{imagens/diagrama.png}
```

---

### Slide final

```latex
\finalslide{imagens/encerramento.png}
```

---

### Código

```latex
\begin{singlecodeslide}{Título do Slide}{JavaScript}
\begin{lstlisting}
const soma = (a, b) => a + b;
console.log(soma(2, 3)); // 5
\end{lstlisting}
\end{singlecodeslide}
```

Linguagens suportadas pelo `listings`: `JavaScript` (definido no pacote), `Python`, `bash`, `SQL`, e outras padrão do LaTeX.

---

## Usar este projeto como template

Este repositório é o template base. O fluxo recomendado é:

### 1. Clonar o template para uma nova aula

```bash
git clone https://github.com/seu-usuario/slides-template.git aula-01
cd aula-01
```

### 2. Desconectar do repositório original

```bash
rm -rf .git
git init
git add .
git commit -m "Início da aula 01"
```

### 3. Criar um repositório novo e fazer o push

```bash
git remote add origin https://github.com/seu-usuario/aula-01.git
git push -u origin main
```

### 4. Editar o conteúdo

Abra o `main.tex` e substitua os slides de exemplo pelo conteúdo da aula. Não mexa em `styles/` nem em `fonts/`.

---

## Atualizar o template em projetos existentes

Se você corrigir algo no template e quiser propagar para uma aula já criada, adicione o template como remote:

```bash
git remote add template https://github.com/seu-usuario/slides-template.git
git fetch template
git merge template/main --allow-unrelated-histories
```

Resolva eventuais conflitos e mantenha suas alterações no `main.tex`.