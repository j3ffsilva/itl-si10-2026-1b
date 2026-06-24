# Rubrica — Ponderada S10: Análise de Sensibilidade em Métricas de Interface Digital

Esta rubrica orienta a avaliação da ponderada da Semana 10.

## Régua geral

- **10,0**: completa as quatro partes com consistência, coerência e rigor analítico, **e** entrega a seção "Ao Além dos Aléns" com simulação de Monte Carlo executada e interpretada em termos de risco.
- **9,0**: completa as quatro partes com boas respostas, consistentes e coerentes, citando números do notebook nas interpretações e na recomendação.
- **7,0 a 7,5**: completa as quatro partes, mas há problemas de coerência, interpretação superficial, recomendação desconectada dos índices ou justificativas sem evidência numérica.
- **Em torno de 6,0**: deixa de responder uma das quatro partes ou omite um dos seus itens essenciais.
- **Em torno de 3,0**: deixa de responder duas ou mais partes essenciais.

> **Penalidade de acesso**: links sem permissão de acesso recebem desconto de **20%** na nota final.

---

## Sinais discriminantes

Estes três critérios distinguem os níveis mais do que qualquer checklist de itens:

1. **Âncoras numéricas** — a resposta cita valores concretos gerados no próprio notebook (correlações, MAE/RMSE, índices de sensibilidade) e os conecta à conclusão. Respostas sem nenhum número próprio não ultrapassam 7,0.

2. **Autoria analítica** — a resposta não poderia valer para outro dataset. Frases genéricas do tipo "essa variável é importante para apps de compras" ou "o erro é baixo" sem comparação com a escala da variável alvo são marca da resposta fraca, mesmo que completa em estrutura.

3. **Interpretação com cautela** — a resposta forte diferencia associação de causalidade, entende o sinal dos índices (positivo/negativo), e converte o resultado em uma ação de produto testável — não em uma afirmação definitiva.

---

## Parte 1 — Exploração

**O que se espera:**
- `variavel_x` preenchida com um dos nomes de `features`, gerando o scatter plot.
- Ao menos uma análise visual ou tabular da relação entre variáveis de entrada e `taxa_conversao_pct` (scatter, matriz de correlação ou similar).
- Resposta escrita que justifica a escolha das duas variáveis com referência a valores concretos da exploração. Uma resposta forte cita os coeficientes de correlação (ex.: abandono ≈ −0,64; scroll ≈ +0,49; tempo ≈ −0,23) e explica por que o terceiro foi preterido.

**Indícios de problemas:**
- Scatter plot não gerado (`variavel_x` vazia ou com valor inválido).
- Justificativa sem nenhum número — menciona apenas "relação" ou "parece ter impacto".
- Variáveis escolhidas sem relação com as evidências apresentadas, ou escolha justificada por senso comum de negócio em vez de dados (ex.: "escolhi abandono porque é métrica importante para qualquer app").

---

## Parte 2 — Modelo

**O que se espera:**
- Citação dos valores de MAE e RMSE gerados.
- Contextualização em relação à escala da `taxa_conversao_pct` (que varia tipicamente entre ~3% e ~9%): o erro representa quanto da amplitude da variável alvo?
- Avaliação qualificada: o modelo é útil para comparar cenários, mas não deve ser tratado como previsão perfeita.

**Indícios de problemas:**
- Resposta que apenas reproduz os valores sem contextualizar a escala (ex.: "MAE = 0,28, RMSE = 0,35, portanto o modelo está bom").
- Afirmações absolutas como "o modelo está correto" sem nenhuma nuance sobre limitação ou uso adequado.
- Confusão entre MAE e RMSE — afirmar que o RMSE "prova" que o modelo é melhor ou pior sem entender que penaliza erros grandes.

---

## Parte 3 — Análise de Sensibilidade

**O que se espera:**
- `variaveis_escolhidas` preenchida com exatamente dois nomes válidos de `features`, gerando a `tabela_sensibilidade`.
- Comparação dos `índice_sensibilidade` citando os valores da tabela.
- Interpretação no formato: "um aumento de 10% em X causa uma variação de Y% na saída" — não apenas "X tem mais impacto que Y".
- Identificação da variável com maior impacto absoluto (índice em módulo maior).

**Indícios de problemas:**
- `variaveis_escolhidas` vazia (tabela não gerada).
- Comparação qualitativa sem citar os índices (ex.: "o abandono tem mais impacto porque a correlação é maior" — mistura correlação com sensibilidade).
- Confusão de sinal: tratar índice negativo como problema de cálculo em vez de efeito inverso.
- Confusão entre variação absoluta da saída e o índice adimensional de sensibilidade.

---

## Parte 4 — Decisão

**O que se espera:**
- Recomendação de ação de produto ou interface concreta (ex.: simplificar checkout, reduzir etapas de pagamento) com referência explícita ao índice de sensibilidade que a sustenta.
- Reconhecimento de que o modelo mostra **associação**, não causalidade — e que uma validação (A/B test, dados reais) seria necessária antes de uma mudança definitiva.
- Limitação ou risco relevante: não basta nomear "dados sintéticos" sem explicar o que isso implica para a decisão.

**Indícios de problemas:**
- Recomendação genérica desconectada dos índices (ex.: "melhorar a interface do app para aumentar a conversão").
- Limitação trivial que não afeta a conclusão (ex.: "toda análise tem erros").
- Ausência total de cautela — trata correlação/sensibilidade como prova de causalidade.

---

## Ao Além dos Aléns — Monte Carlo (bônus para 10,0)

**O que se espera:**
- Simulação executada (1000 amostras, histograma gerado).
- Interpretação da distribuição em termos de risco: citar percentis (p10/p90 ou similares) e conectar a variabilidade à recomendação da Parte 4 — o efeito esperado é robusto ou sensível à incerteza das entradas?

**Indício de entrega incompleta:**
- Código rodando e histograma gerado, mas sem nenhuma interpretação escrita sobre risco ou variabilidade.

---

## Observações de uso

- A nota deve ser atribuída a partir das evidências autorais nas células de resposta do notebook.
- Enunciados, células de código fornecidas pelo professor e blocos de exemplo não contam como produção do estudante.
- O grau de autoria se evidencia pela conexão entre os números gerados e o texto escrito. A pergunta-chave ao ler uma resposta: **essa frase poderia estar no notebook de qualquer outro estudante, mesmo sem ter aberto os dados?** Se sim, não é evidência de análise.
