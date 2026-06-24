# Prompt — Calibração de Correção (Ponderada S10)

---

Você vai me ajudar a calibrar a correção de uma atividade prática de análise de dados.

## Contexto da atividade

A atividade é de um curso de graduação em Sistemas de Informação. Os estudantes receberam um Jupyter Notebook com código parcialmente pronto e precisavam completar quatro partes analíticas. O tema é **análise de sensibilidade aplicada a métricas de interface digital**.

### Dados e modelo

O notebook gera automaticamente um dataset com 180 dias de observações de um app de compras, com estas colunas:

- `taxa_abandono_carrinho_pct` — taxa de abandono do carrinho (%)
- `profundidade_scroll_pct` — profundidade média de scroll na página (%)
- `tempo_primeiro_clique_s` — tempo até o primeiro clique em produto (segundos)
- `taxa_conversao_pct` — taxa de conversão (variável alvo, ~3% a 9%)

A relação verdadeira embutida nos dados é:

```
taxa_conversao = 7.5
    - 0.055 × taxa_abandono
    + 0.026 × profundidade_scroll
    - 0.085 × tempo_primeiro_clique
    + ruído
```

Um modelo de regressão linear por mínimos quadrados é ajustado a esses dados. O MAE típico gira em torno de 0,27–0,30 pontos percentuais; o RMSE, em torno de 0,34–0,37.

A correlação de Pearson com `taxa_conversao_pct` é aproximadamente:
- `taxa_abandono_carrinho_pct`: −0,64 (maior correlação em módulo)
- `profundidade_scroll_pct`: +0,49
- `tempo_primeiro_clique_s`: −0,23 (menor correlação)

Para a análise de sensibilidade, o estudante escolhe **duas** das três variáveis, aplica uma variação de +10% sobre a média de cada uma e calcula o índice:

```
índice_sensibilidade = (Δ saída / saída_base) / (Δ entrada / entrada_base)
```

Os índices típicos resultantes (usando a média do dataset como linha-base) são:
- `taxa_abandono_carrinho_pct`: ≈ −0,54
- `profundidade_scroll_pct`: ≈ +0,33
- `tempo_primeiro_clique_s`: ≈ −0,17

A variável de maior impacto absoluto é a **taxa de abandono do carrinho**.

---

## As quatro partes da atividade

**Parte 1 — Exploração**
O estudante preenche `variavel_x` com uma das features para gerar um scatter plot, e escreve quais duas variáveis escolheu para a análise de sensibilidade, justificando com evidências da exploração.

**Parte 2 — Modelo**
O estudante interpreta o erro do modelo (MAE e RMSE) em relação à escala da `taxa_conversao_pct`.

**Parte 3 — Análise de Sensibilidade**
O estudante preenche `variaveis_escolhidas` (lista com dois nomes), o código gera a tabela de sensibilidade, e o estudante compara os índices e identifica qual variável tem maior impacto, citando os valores da tabela.

**Parte 4 — Decisão**
O estudante recomenda uma ação de produto ou interface com base nos índices calculados, e aponta uma limitação, risco ou hipótese da análise.

**Seção bônus — Ao Além dos Aléns**
O estudante roda uma simulação de Monte Carlo (código fornecido, 1000 amostras) e interpreta a distribuição resultante em termos de risco para a recomendação.

---

## O que preciso de você

Imagine situações concretas de respostas que estudantes reais podem entregar em cada uma das quatro partes. Para cada parte, descreva **três perfis de resposta**:

1. **Resposta forte** — o que parece em notebooks de estudantes que entenderam o raciocínio e conectaram os números às conclusões.
2. **Resposta mediana** — completa, mas superficial, mecânica ou com algum desalinhamento entre os números e o texto.
3. **Resposta fraca** — incompleta, copiada do enunciado, genérica a ponto de não mostrar contato com os dados gerados, ou com erro de interpretação relevante.

Para cada perfil, escreva um **trecho de resposta simulado** como se fosse o texto real do estudante (célula Markdown do notebook), curto mas suficiente para ilustrar o padrão. Use os números concretos do contexto acima quando isso tornar o exemplo mais realista.

Ao final, aponte os **dois ou três sinais mais discriminantes** — os elementos que, na sua visão, mais diferenciam uma entrega forte de uma mediana, e uma mediana de uma fraca — de modo a ajudar na calibração da nota.
