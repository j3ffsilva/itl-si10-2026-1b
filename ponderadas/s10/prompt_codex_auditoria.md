# Prompt — Auditoria de Calibração (Ponderada S10)

---

## Missão

Você vai auditar 24 avaliações de uma atividade de graduação que **já foram corrigidas por outro modelo**.
Seu papel não é o de um auditor burocrático que verifica checklist. É o de alguém que procura falhas que **importam**:

- **Erros de calibração**: dois estudantes com trabalho de qualidade similar receberam notas substancialmente diferentes sem justificativa que sustente a diferença.
- **Possíveis alucinações**: o avaliador afirma que o estudante fez algo que provavelmente não está no trabalho, ou cita números que parecem inventados.
- **Inconsistência de critério**: um elemento foi premiado em um estudante e ignorado (ou penalizado) em outro.
- **Lacunas de aprendizado não sinalizadas**: um erro conceitual grave — confundir correlação com sensibilidade, tratar dados sintéticos como prova de causalidade, interpretar índice negativo como falha de cálculo — que ficou sem menção no feedback.

O que **não** procurar:
- Pequenas diferenças de estilo, formalidade ou completude de frase.
- Ausência de citação bibliográfica ou formatação.
- Divergências de décimo de ponto em casos sem justificativa clara na outra direção.
- Qualquer coisa que não mudaria a nota em ao menos 0,5 ponto se corrigida.

---

## Rubrica usada na correção

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


---

## Resumo das notas atribuídas

| # | Estudante | Nota |
|---|-----------|------|
| 01 | Bernardo de Figueiredo Meirelles | 7,5 |
| 02 | Cibele Figueredo Leal | 9,0 |
| 03 | Daniel Zular | 9,0 |
| 04 | David Deodato Alvarenga Nascimento | 10,0 |
| 05 | Enzo Salvador Barci | 8,5 |
| 06 | Fernanda Correia Nascimento | 9,5 |
| 07 | Freddy Mester Harari | 9,5 |
| 08 | Gabriela Silva | 9,5 |
| 09 | Igor Sampaio Silva | 7,5 |
| 10 | Isabelly Maia Montalvão | 10,0 |
| 11 | Isadora Tribst Gatto | 10,0 |
| 12 | Kaio Vittor Martins Silva | 7,5 |
| 13 | Leonardo Nigri Griner | 10,0 |
| 14 | Leonardo Souza Martins | 9,5 |
| 15 | Marcelo Faska Sitton | 8,5 |
| 16 | Marcelo Rubim Rossignolli | 9,0 |
| 17 | Mariana de Paula Barbosa Souza | 9,0 |
| 18 | Matheus Fernandes Guimarães de Sousa | 8,0 |
| 19 | Mirella Borim Lima | 8,0 |
| 20 | Moyses Birman Anijar | 9,0 |
| 21 | Paulo Octavio de Paula | 7,5 |
| 22 | Pedro El Haouli Faria | 10,0 |
| 23 | Ricardo de Toledo Planas | 10,0 |
| 24 | Stefano Tamer Parente | 9,0 |

---

## Avaliações individuais

Cada avaliação abaixo contém: nota atribuída, feedback e evidência por parte.

### 01. Bernardo de Figueiredo Meirelles — Nota: 7,5
### 02. Cibele Figueredo Leal — Nota: 9,0
### 03. Daniel Zular — Nota: 9,0
### 04. David Deodato Alvarenga Nascimento — Nota: 10,0
### 05. Enzo Salvador Barci — Nota: 8,5
### 06. Fernanda Correia Nascimento — Nota: 9,5
### 07. Freddy Mester Harari — Nota: 9,5
### 08. Gabriela Silva — Nota: 9,5
### 09. Igor Sampaio Silva — Nota: 7,5
### 10. Isabelly Maia Montalvão — Nota: 10,0
### 11. Isadora Tribst Gatto — Nota: 10,0
### 12. Kaio Vittor Martins Silva — Nota: 7,5
### 13. Leonardo Nigri Griner — Nota: 10,0
### 14. Leonardo Souza Martins — Nota: 9,5
### 15. Marcelo Faska Sitton — Nota: 8,5
### 16. Marcelo Rubim Rossignolli — Nota: 9,0
### 17. Mariana de Paula Barbosa Souza — Nota: 9,0
### 18. Matheus Fernandes Guimarães de Sousa — Nota: 8,0
### 19. Mirella Borim Lima — Nota: 8,0
### 20. Moyses Birman Anijar — Nota: 9,0
### 21. Paulo Octavio de Paula — Nota: 7,5
### 22. Pedro El Haouli Faria — Nota: 10,0
### 23. Ricardo de Toledo Planas — Nota: 10,0
### 24. Stefano Tamer Parente — Nota: 9,0

```

============================================================
ESTUDANTE 01: Bernardo de Figueiredo Meirelles | NOTA: 7,5
============================================================
# Avaliação - Bernardo de Figueiredo Meirelles

Estudante: Bernardo de Figueiredo Meirelles

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

A entrega tem todas as quatro partes completas e boa iniciativa técnica: heatmap de correlação adicionado, gráfico de resíduos produzido, Monte Carlo executado com percentis e histograma. A recomendação de produto (focar no abandono do carrinho) está correta e alinhada com a análise. O problema central está na Parte 1: a justificativa de escolha de variáveis cita correlações fictícias ("−0,78 para abandono" e "−0,35 para tempo de clique") que não aparecem nos dados do notebook — os valores reais da matriz de correlação são −0,643 e −0,229, respectivamente. Isso fragiliza a âncora numérica de todo o raciocínio. A interpretação do Monte Carlo também é genérica (menciona "desenho de sino" e "dispersão apertada") sem citar os percentis que o próprio código calculou (P10 ≈ 5,37%, P90 ≈ 6,38%).

## Evidência

### Parte 1 — Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`; scatter e heatmap de correlação gerados. Escolheu abandono do carrinho e tempo do primeiro clique. A justificativa cita correlações de "−0,78" e "−0,35" que não existem na matriz exibida pelo notebook (valores reais: −0,643 e −0,229). O argumento qualitativo ("usuário com a carteira na mão") é contextual mas não se apoia nos números corretos.

### Parte 2 — Modelo

MAE 0,276 e RMSE 0,344 obtidos e exibidos. Gráfico de resíduos adicionado (iniciativa além do pedido). A interpretação é vaga: diz que os erros são "baixos" e que "RMSE não está longe do MAE", mas não compara o MAE com a escala da variável alvo (~5,87%) para quantificar a aceitabilidade.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida com abandono e tempo do primeiro clique. Tabela gerada: índice −0,489 para abandono e −0,112 para tempo. Os índices estão corretos para as variáveis escolhidas. A interpretação cita o coeficiente do modelo (−0,055) em vez dos índices de sensibilidade da tabela, misturando dois conceitos distintos. A conclusão (abandono tem maior impacto) está correta.

### Parte 4 — Decisão

Recomendação de simplificar o pagamento e deixar o frete claro é específica e acionável. Aponta limitação de linearidade e possível interação entre variáveis (abandono podendo ser influenciado pelo scroll). Não distingue explicitamente associação de causalidade no texto.

### Ao Além dos Aléns (bônus)

Presente e executado: 1000 simulações, histograma produzido, percentis P10/P90 calculados (5,37% e 6,38%). A interpretação textual, porém, é superficial — menciona "dispersão apertada" sem citar os percentis calculados ou conectá-los ao risco da recomendação. Adicionou também gráfico de Monte Carlo com linhas de percentil e análise de impacto financeiro estimado (iniciativa criativa e relevante para decisão de produto).

## Confiança

Confiança geral: Alta

Observação: as correlações fabricadas na Parte 1 são verificáveis pela matriz exibida no próprio notebook, o que torna o desvio inequívoco.

============================================================
ESTUDANTE 02: Cibele Figueredo Leal | NOTA: 9,0
============================================================
# Avaliação - Cibele Figueredo Leal

Estudante: Cibele Figueredo Leal

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Entrega completa e consistente em todas as quatro partes. A estudante cita os valores corretos de correlação (−0,643 e +0,485) na justificativa de escolha, exibe os índices de sensibilidade da tabela (−0,489 e +0,258) na Parte 3 e ainda calcula o R² (0,71) como evidência adicional da qualidade do modelo. A interpretação do MAE é bem formulada, comparando o erro com a escala da variável alvo. O bônus de Monte Carlo foi executado com um segundo cenário (abandono 10% menor), permitindo uma comparação quantitativa de risco (ganho médio de 0,288 p.p.) — isso vai além do mínimo pedido. A limitação apontada distingue associação de causalidade e propõe A/B test como validação. A nota não alcança 10,0 porque a interpretação do Monte Carlo poderia conectar melhor a distribuição ao risco da recomendação com linguagem de percentil explícita, e a recomendação de produto poderia ser mais específica em termos de ação de interface.

## Evidência

### Parte 1 — Exploração

Duas explorações geradas: scatter de abandono vs. conversão (com trendline OLS) e scatter de scroll vs. conversão. Justificativa cita correlações corretas: −0,643 para abandono (maior correlação negativa absoluta) e +0,485 para scroll. Tempo do primeiro clique descartado pela correlação mais fraca (−0,229).

### Parte 2 — Modelo

MAE 0,276 e RMSE 0,344 obtidos. Calcula também R² = 0,7144 (iniciativa além do pedido). A interpretação compara MAE com a escala da taxa de conversão (~4%–8%), afirma que o RMSE pouco acima do MAE indica ausência de erros extremos, e usa o R² como confirmação.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela correta: índice −0,489 (abandono) e +0,258 (scroll). A resposta textual cita os valores exatos da tabela e explica o sinal e a magnitude: "variação de 10% nessa variável produz uma mudança proporcionalmente maior na taxa de conversão prevista." Código adicional identifica automaticamente a variável de maior impacto absoluto. Gráfico de barras de índices gerado.

### Parte 4 — Decisão

Recomendação: priorizar redução do abandono do carrinho, cita índice −0,489 vs. +0,258. Ações propostas (simplificar checkout, reduzir etapas, mostrar frete mais cedo). Limitação menciona linearidade do modelo, dados simulados, e propõe que resultados sejam tratados como "apoio direcional" — distingue implicitamente associação de causalidade. Não cita A/B test explicitamente, mas reconhece que "dados reais" seriam necessários.

### Ao Além dos Aléns (bônus)

Presente e bem executado: 1000 simulações, estatísticas com percentis (P10 5,22%, P90 6,54%), comparação de cenário com abandono 10% menor (ganho médio de 0,288 p.p., P10 sobe de 5,34% para 5,67%), gráfico boxplot comparando cenários, probabilidade de conversão > 5% (99%). Interpreta distribuição com referência ao risco da recomendação. Adicionalmente calcula betas padronizados, ampliando o rigor da análise de importância de variáveis.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 03: Daniel Zular | NOTA: 9,0
============================================================
# Avaliação - Daniel Zular

Estudante: Daniel Zular

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Entrega completa e bem fundamentada. Daniel cita as correlações corretas (−0,643 e +0,485) para justificar a escolha das variáveis, compara o MAE com a escala da variável alvo ("entre 4% e 8%"), e cita os índices de sensibilidade da tabela com precisão (−0,489 e +0,258) com interpretação sinal+magnitude correta. A recomendação cita o índice numericamente e propõe validação com A/B test — distinguindo associação de causalidade de forma explícita. O bônus Monte Carlo foi executado com um segundo cenário (abandono 10% menor), com tabela comparando médias e percentis P10/P90 e gráfico boxplot. A nota fica em 9,0 e não em 10,0 porque a interpretação do Monte Carlo poderia conectar mais diretamente o risco do pior cenário (P10) à decisão de produto, e a exploração da Parte 1 ficou mais enxuta (um único scatter, sem heatmap ou análise adicional das outras variáveis antes da escolha).

## Evidência

### Parte 1 — Exploração

Tabela de correlação exibida, `variavel_x` preenchida com abandono, scatter com trendline OLS gerado. Justificativa cita correlações corretas: abandono −0,643 ("maior relação com a taxa de conversão"), scroll +0,485 ("relação positiva"), tempo −0,229 descartado explicitamente. Fundamentação numérica presente e correta.

### Parte 2 — Modelo

MAE 0,276 e RMSE 0,344. A interpretação compara o MAE com a escala da variável alvo ("entre 4% e 8%"), conclui que o erro é "relativamente baixo" e justifica com o fato de o RMSE penalizar erros maiores. Usa explicitamente a escala do alvo como referência — âncora numérica presente.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela gerada com valores corretos: índice −0,489 (abandono) e +0,258 (scroll). A resposta cita os valores exatos da tabela, explica o sinal (abandono aumenta → conversão cai; scroll aumenta → conversão sobe), e conclui pela prioridade do abandono com base no valor absoluto maior. Gráfico de barras de índices gerado.

### Parte 4 — Decisão

Recomendação: priorizar redução do abandono, cita índice −0,489 vs. +0,258, propõe ações específicas (fluxo de finalização, frete mais claro, reduzir etapas). Limitação aponta modelo linear e dados simulados, propõe A/B test — distingue associação de causalidade explicitamente ("a análise mostra relações entre as variáveis, mas não prova que uma causa diretamente a outra").

### Ao Além dos Aléns (bônus)

Presente e bem executado: 1000 simulações com seed diferente (rng_sim, seed 2026). Estatísticas com percentis (P10 5,34%, P90 6,34%). Cenário de melhoria (abandono 10% menor): média sobe de 5,85% para 6,14%, ganho de 0,29 p.p., P10 e P90 comparados. Gráfico boxplot lado a lado. A interpretação textual cita os percentis e o ganho médio, conectando ao risco da recomendação.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 04: David Deodato Alvarenga Nascimento | NOTA: 10,0
============================================================
# Avaliação - David Deodato Alvarenga Nascimento

Estudante: David Deodato Alvarenga Nascimento

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entrega exemplar. David vai consistentemente além do mínimo em cada parte sem perder o rigor analítico: hipóteses formalizadas antes da exploração, ranking completo de sensibilidade para as três variáveis, análise bidirecional (±10%), tabela de metas ("quanto precisa mudar para gerar 0,20 p.p.?"), cenários combinados de produto com impacto previsto, Monte Carlo com 5000 simulações, e comparação direta baseline vs. intervenção conservadora com ganho médio, P10, P50, P90 e probabilidade de ganho positivo (100%). A recomendação é estruturada como matriz de decisão com evidência, métrica de validação e risco para cada variável. A distinção entre associação e causalidade está explícita e bem fundamentada. Não há pontos fracos relevantes.

## Evidência

### Parte 1 — Exploração

Tabela de correlações + ranking por correlação absoluta + heatmap + scatter (abandono e scroll) + tabela de confirmação de hipóteses (H1, H2, H3 com sinal esperado vs. observado). Justificativa cita correlações corretas: abandono −0,643 e scroll +0,485, com tempo (−0,229) descartado explicitamente. Hipóteses formalizadas antes da exploração — abordagem metodologicamente madura.

### Parte 2 — Modelo

MAE 0,276, RMSE 0,344, coeficientes exibidos. Calcula também coeficientes padronizados (abandono −0,650, scroll +0,457, tempo −0,328). Interpreta MAE em relação à média (~5,87%): "erro é baixo o suficiente para comparar cenários locais de sensibilidade." Residual plot e histograma de resíduos produzidos. RMSE um pouco acima do MAE justificado: "não há sinal forte de que poucos erros extremos estejam dominando."

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela principal: índice −0,489 (abandono) e +0,258 (scroll). Além disso: ranking completo das três variáveis (incluindo tempo: −0,112), análise bidirecional (±10% para todas), tabela de metas de produto (quanto mudar para +0,20 p.p. e +0,50 p.p.), e cenários combinados. Todos os índices corretamente calculados e interpretados com sinal e magnitude.

### Parte 4 — Decisão

Matriz de decisão formal com prioridade 1/2/3, ação, variável alvo, evidência, métrica de validação e risco para cada variável. Recomendação principal: reduzir abandono (índice −0,489, maior impacto). Limitação explícita: "o modelo estima uma relação local em uma base simulada, não um efeito causal observado em usuários reais" — distingue causalidade e propõe teste controlado com métricas de validação definidas.

### Ao Além dos Aléns (bônus)

Presente e executado com rigor: 5000 simulações, estatísticas com P5/P10/P25/P50/P75/P90/P95, probabilidade de ficar abaixo da linha base (49,1%), histograma com marcadores de P10 e P90. Cenário de intervenção conservadora (abandono −5%, tempo −5%): ganho médio de 0,176 p.p., P10 do ganho = 0,155 p.p., prob. de ganho positivo = 100%, histograma sobreposto base vs. intervenção. Interpreta a distribuição com referência ao risco: "a recomendação não deve ser lida como ganho fixo" e define próximo passo (teste controlado).

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 05: Enzo Salvador Barci | NOTA: 8,5
============================================================
# Avaliação - Enzo Salvador Barci

Estudante: Enzo Salvador Barci

Rubrica: `../../../rubrica_s10.md`

Nota: 8,5

Feedback:

Entrega completa nas quatro partes, com citação correta das correlações (−0,643 e +0,485) e dos índices de sensibilidade da tabela (−0,489 e +0,258). A interpretação da Parte 3 é a mais sólida do notebook: cita os valores exatos da tabela para abandono (de 47,546 para 52,300, queda de 4,891%) e scroll (de 62,449 para 68,694, alta de 2,578%) com sinal e magnitude explicados. A recomendação de produto cita o índice −0,489 e propõe A/B test. A limitação aponta linearidade e dados simulados — distingue associação de causalidade adequadamente. O Monte Carlo foi executado e os percentis citados no texto (P25 5,62%, mediana 5,85%, P75 6,13%, P90 6,38%). A nota fica em 8,5 — abaixo de 9,0 — porque a interpretação do MAE na Parte 2 não compara o erro à escala da variável alvo (diz apenas que "não parece tão alto" sem âncora quantitativa), e a exploração na Parte 1 usa apenas um scatter sem evidência visual adicional; também não há cenário comparativo no Monte Carlo, apenas a distribuição isolada.

## Evidência

### Parte 1 — Exploração

Tabela de correlação exibida. `variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Scatter sem trendline gerado. Justificativa cita correlações corretas (−0,643 para abandono, +0,485 para scroll, −0,229 para tempo descartado). Texto bem estruturado mas com única visualização.

### Parte 2 — Modelo

MAE 0,276, RMSE 0,344 obtidos. Interpretação diz que o erro é "relativamente baixo" e que RMSE "um pouco maior" considera erros maiores, mas não quantifica o erro em relação à escala (~5,87% de média da variável alvo). A interpretação é razoável mas falta a âncora numérica explícita pedida pela rubrica.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela gerada com valores corretos: índice −0,489 (abandono) e +0,258 (scroll). Resposta cita os valores numéricos da tabela com precisão (valor original, valor alterado, variação da saída e índice para ambas as variáveis). Sinal interpretado corretamente: "abandono aumenta → conversão cai, coerente com apps de compras."

### Parte 4 — Decisão

Recomendação: melhorias no carrinho e checkout, com citação do índice −0,489 vs. +0,258. Ações específicas: clareza de frete, redução de etapas, mensagens de erro, facilitar pagamento. Limitação aponta modelo linear e dados simulados, propõe A/B test — distingue associação de causalidade.

### Ao Além dos Aléns (bônus)

Presente: 1000 simulações, descrição com percentis (P10 5,37%, P25 5,62%, P50 5,85%, P75 6,13%, P90 6,38%), histograma gerado. Interpretação cita os valores dos percentis e conclui que a distribuição é concentrada, o risco da recomendação é "baixo a moderado." Não há cenário de intervenção comparativo, o que limitaria a profundidade da análise de risco.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 06: Fernanda Correia Nascimento | NOTA: 9,5
============================================================
# Avaliação - Fernanda Correia Nascimento

Estudante: Fernanda Correia Nascimento

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Entrega de altíssima qualidade. A exploração da Parte 1 é a mais rica do lote: quatro análises complementares (scatter colorido com três variáveis em painel, boxplots por tercil, perfil dos top/bottom 10% de dias). A recomendação é a mais elaborada, com três ações concretas de interface, e a limitação é a mais aprofundada (aponta que variáveis interagem entre si e que uma ação de produto pode alterar múltiplas métricas simultaneamente). O Monte Carlo usa 10.000 simulações com justificativa explícita da escolha. A única ressalva que impede nota 10,0 é uma inconsistência nos índices de sensibilidade citados no texto da Parte 3: a estudante escreve "índice de sensibilidade de −0,63" e "+0,40", mas a tabela exibida pelo próprio notebook mostra −0,489 e +0,258 — os valores textuais não coincidem com os calculados, o que introduz uma contradição interna na entrega.

## Evidência

### Parte 1 — Exploração

Quatro análises exploratórias produzidas: (1) scatter panel com três variáveis coloridas por conversão, (2) boxplots por tercil de cada variável, (3) perfil médio dos melhores e piores dias (top/bottom 10%), com tabela mostrando abandono médio de 39,48% nos melhores dias vs. 55,34% nos piores. Justificativa cita correlações corretas (−0,643 e +0,485) e descreve o que cada análise revelou. A exploração é a mais detalhada do lote.

### Parte 2 — Modelo

MAE 0,276, RMSE 0,344, coeficientes exibidos com print detalhado. Interpretação compara o MAE com a amplitude da variável alvo (~4 p.p.) e calcula que 0,28 p.p. representa "cerca de 7% da amplitude total", quantificando a qualidade do ajuste. Menciona que o RMSE pouco acima do MAE é esperado dado o processo gerador linear com ruído gaussiano.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela gerada com valores corretos: índice −0,489 (abandono) e +0,258 (scroll). Análise adicional com variações de ±10% e ±20%, confirmando linearidade e simetria dos efeitos. O texto da resposta, contudo, cita índices de "−0,63" e "+0,40" que não correspondem aos valores da tabela (−0,489 e +0,258) — inconsistência interna.

### Parte 4 — Decisão

Recomendação estruturada com três ações específicas: simplificar checkout, exibir custos totais antecipadamente, melhorar apresentação de produtos. Cita os índices (−0,63 e +0,40, com a inconsistência já apontada). Limitação é a mais sofisticada do lote: aponta que o modelo assume linearidade e independência entre variáveis, e que "uma melhoria no checkout pode reduzir o abandono e simultaneamente aumentar o scroll de confirmação — efeitos que o modelo não captura conjuntamente." Distingue associação de causalidade de forma explícita e aprofundada.

### Ao Além dos Aléns (bônus)

Presente com rigor: 10.000 simulações (justificada a escolha), estatísticas com P10/P25/P50/P75/P90, histograma com marcadores P10 e P90. Interpreta P10 (~5,38%) e P90 (~6,37%) como amplitude de ~1,7 p.p. por incerteza natural das entradas, e argumenta que o índice de sensibilidade do abandono (−0,63 no texto) tem potencial de produzir deslocamentos acima dessa variabilidade. A análise conecta a distribuição simulada ao risco da recomendação.

## Confiança

Confiança geral: Alta

Observação: a inconsistência nos índices citados no texto (−0,63 e +0,40) vs. os valores da tabela (−0,489 e +0,258) é verificável diretamente no notebook e representa o único ponto de desvio em uma entrega otherwise muito sólida.

============================================================
ESTUDANTE 07: Freddy Mester Harari | NOTA: 9,5
============================================================
# Avaliação - Freddy Mester Harari

Estudante: Freddy Mester Harari

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Entrega muito consistente em todas as quatro partes, com citação de números próprios do notebook em cada resposta. O destaque vai para a Parte 3, onde Freddy não apenas respondeu o que foi pedido (duas variáveis) mas calculou o índice das três variáveis para demonstrar com dados que as escolhidas são de fato as de maior impacto — e incluiu um raciocínio explícito sobre por que o coeficiente bruto do tempo de clique é enganoso comparado ao índice de sensibilidade. O Monte Carlo foi executado corretamente, com percenis citados e interpretação conectada ao risco da recomendação. A nota fica abaixo de 10 apenas porque a interpretação do bônus, apesar de correta, é mais descritiva do que analítica: cita os percentis (P10 = 5,37%, P90 = 6,38%) mas poderia ter quantificado o risco de a intervenção não surtir efeito, considerando que o ganho esperado (≈ 0,29 p.p.) é da mesma ordem do desvio padrão diário.

## Evidência

### Parte 1 — Exploração

`variavel_x` preenchida com uma lista de duas variáveis (`["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`) e scatter gerado em loop para ambas. Justificativa com números: cita correlações r = −0,64 e r = +0,48 da matriz, contrasta com r = −0,23 do tempo de clique e usa o scatter como evidência visual adicional.

### Parte 2 — Modelo

MAE (0,276) e RMSE (0,344) citados corretamente. Interpreta o MAE como "menos de 5% do valor típico" em relação à média da conversão e menciona que RMSE ligeiramente acima do MAE indica alguns dias com erro maior, sem outlier grave. Avalia o erro como aceitável para decisão de produto.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida. Tabela gerada com índices −0,489 (abandono) e +0,258 (scroll). Calcula também o índice do tempo de clique (−0,112) para comparação, e explica explicitamente por que o coeficiente bruto do tempo é maior que o do abandono mas seu índice é o menor: a escala da variável é pequena, então 10% dela move pouco a conversão. Raciocínio analítico claro.

### Parte 4 — Decisão

Recomenda priorizar redução do abandono, cita índice −0,49 e a variação de 47,5% para 42,8% como exemplo concreto. Propõe ações testáveis (fluxo de checkout, salvamento de carrinho). Discute scroll como alavanca secundária. Limitação relevante: hipótese de linearidade e limitação da análise OAT (perturba uma variável por vez enquanto na realidade as variáveis covariam). Não usa a palavra "causalidade" explicitamente, mas reconhece implicitamente a limitação associativa.

### Ao Além dos Aléns (bônus)

Presente e executado. Simulação de 1000 amostras com outputs corretos (média 5,869%, std 0,393, P10 = 5,37%, P90 = 6,38%). Interpreta distribuição em termos de estabilidade e cita que o ganho esperado (0,29 p.p.) é da mesma ordem do desvio padrão diário, conectando corretamente à necessidade de teste com usuários reais.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 08: Gabriela Silva | NOTA: 9,5
============================================================
# Avaliação - Gabriela Silva

Estudante: Gabriela Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Entrega completa e analiticamente rica em todas as quatro partes. Gabriela vai além do pedido mínimo em várias seções: na Parte 3, calcula os índices das três variáveis (não apenas as duas escolhidas) e elabora o argumento de que sensibilidade difere de coeficiente isolado — o que é o insight central da atividade — com clareza e precisão. Na Parte 2, além de interpretar MAE e RMSE em relação à escala, acrescenta o argumento de que o RMSE do modelo (0,344) é próximo do ruído de geração dos dados (σ = 0,35), evidenciando que o modelo capturou quase todo o sinal sistemático. A limitação na Parte 4 é específica e fundamentada em dados próprios (tabela de distribuição de resíduos que mostra 15,6% dos dias com erro acima de 0,5 p.p.). O bônus de Monte Carlo está executado e interpretado com citação de percentis e raciocínio sobre risco. A nota fica em 9,5 (e não 10) porque a resposta da Parte 4 não distingue associação de causalidade de forma explícita; o notebook menciona ações de produto mas não ressalva que a relação é observacional.

## Evidência

### Parte 1 — Exploração

Dois scatters gerados (abandono e scroll) via subplots. Justificativa numérica: cita correlação −0,643 para abandono ("relação inversa muito nítida") e +0,485 para scroll, conectando o sinal à interpretação de engajamento do usuário.

### Parte 2 — Modelo

MAE (0,276) e RMSE (0,344) citados. Argumento notável: RMSE ≈ σ do ruído de geração (0,35), indicando que o modelo não deixou sinal sistemático residual. Relação RMSE/MAE ≈ 1,25 identificada como esperada para resíduos normais. Contexto de escala (média da conversão ≈ 5,87%) mencionado.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida com as três variáveis (indo além do pedido para demonstrar ranking completo). Tabela gerada com índices: abandono −0,489, scroll +0,258, tempo −0,112. Explica a razão de o abandono ser ≈ 1,9× mais sensível que o scroll. Argumento correto sobre sensibilidade versus coeficiente bruto.

### Parte 4 — Decisão

Recomenda priorizar checkout com índice −0,489 como justificativa. Cita valores numéricos (47,5% → 42,7%, ganho de 0,29 p.p.). Propõe ações concretas ("checkout em uma página", transparência de frete, selos de confiança). Limitação específica: variáveis externas não mapeadas (sazonalidade, concorrência, perfil do tráfego) e evidência dos resíduos com tabela própria. Não distingue associação de causalidade de forma explícita.

### Ao Além dos Aléns (bônus)

Presente e executado. Estatísticas de saída corretas (média 5,87%, std 0,393, P10 = 5,37%, P90 = 6,38%). Interpreta risco: 90% dos cenários acima de 5,37%, não há caudas longas. Menciona que o ganho esperado (0,29 p.p.) é comparável ao desvio padrão simulado, mantendo a cautela analítica.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 09: Igor Sampaio Silva | NOTA: 7,5
============================================================
# Avaliação - Igor Sampaio Silva

Estudante: Igor Sampaio Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

Igor entregou as quatro partes e executou o bônus, mas a escolha de variáveis na Parte 1 é a única do lote que descarta o scroll em favor do tempo de clique, e a justificativa para isso é genérica e parcialmente inconsistente: afirma que scroll "não teria tantos insights importantes" porque o usuário pode rolar sem comprar — o que é um argumento comportamental válido, mas não está ancorado em nenhum número do notebook e contradiz a correlação observada (r = +0,485 vs r = −0,229). Essa escolha reduz a qualidade analítica das partes seguintes, já que o modelo resultante exclui a segunda variável mais relevante e apresenta MAE maior (0,348 vs 0,276). As partes 3 e 4 compensam parcialmente com citação de índices próprios e raciocínio coerente, mas ficam limitadas ao par menos informativo. A distinção associação/causalidade aparece na limitação da Parte 4.

## Evidência

### Parte 1 — Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Scatter e scatter matrix gerados. Cita correlações corretamente (r = −0,643, r = +0,485, r = −0,229). Porém escolhe `tempo_primeiro_clique_s` como segunda variável em vez de scroll, justificando com argumento comportamental não sustentado pelos números ("rolar sem comprar"). Justificativa não tem âncora numérica que distinga tempo de clique do scroll.

### Parte 2 — Modelo

MAE (0,348) e RMSE (0,452) citados e explicados com definições corretas de MAE e RMSE. Contextualiza o erro em relação à média (5,87%) e menciona que o custo de excluir o scroll foi MAE ≈ 26% maior. Interpretação adequada, mas o modelo é subótimo pela escolha de variáveis.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida com abandono e tempo de clique. Tabela gerada com índices: abandono −0,511 e tempo −0,105. Cita valores da tabela e calcula que o abandono tem impacto ≈ 4,9× maior que o tempo. Interpretação correta dentro das variáveis escolhidas. Índice do abandono ligeiramente diferente dos demais (−0,511 vs −0,489) porque o modelo exclui scroll, redistribuindo os coeficientes.

### Parte 4 — Decisão

Recomenda priorizar redução do abandono com índice −0,489 citado (nota: no corpo da resposta usa o índice do modelo completo do contexto, não o −0,511 do seu próprio modelo — inconsistência menor). Propõe ações concretas (alertas de carrinho, checkout simplificado, barra de progresso). Limitações: correlação não é causalidade (explicitamente mencionada), instabilidade do modelo com sazonalidade, e ponto de saturação da relação linear. As três limitações são específicas e relevantes.

### Ao Além dos Aléns (bônus)

Presente e executado (modelo com duas variáveis). Estatísticas corretas para o modelo escolhido (média 5,859%, P10 = 5,407%, P90 = 6,292%). Cita amplitude P10–P90 = 0,885 p.p. e interpreta risco de caudas extremas quando variáveis saem do padrão histórico. Interpretação adequada.

## Confiança

Confiança geral: Alta
Observação: a inconsistência do índice citado na Parte 4 (−0,489 em vez de −0,511) é menor e pode ser interpretada como referência ao valor da exploração pré-escolha de variáveis.

============================================================
ESTUDANTE 10: Isabelly Maia Montalvão | NOTA: 10,0
============================================================
# Avaliação - Isabelly Maia Montalvão

Estudante: Isabelly Maia Montalvão

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entrega excepcional. O notebook principal cobre as quatro partes com profundidade analítica consistente, citação de números em todas as respostas, distinção explícita entre associação e causalidade e proposta de teste A/B como validação. O bônus vai muito além do pedido: além do Monte Carlo comparativo entre cenário atual e cenário com abandono reduzido em 10% (com quantificação do risco de 1,4% → 0,1% de ficar abaixo de 5%), Isabelly entregou um segundo notebook separado (`experimento_sobol_bootstrap.ipynb`) com índices de Sobol (S1 e ST), bootstrap dos índices com IC 95%, modelo expandido com interações e uma tabela consolidada que compara quatro métricas de importância. Esse experimento é de nível de análise muito superior ao esperado, demonstra domínio real dos fundamentos de sensibilidade global e robustez estatística. A distinção entre sensibilidade local (tornado, OAT) e global (Sobol) e a confirmação de que interações são desprezíveis são contribuições analíticas independentes que fortalecem a conclusão.

## Evidência

### Parte 1 — Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Mapa de calor de correlações gerado, histogramas das variáveis de entrada e scatter de cada variável vs. conversão. Justificativa com correlações: −0,643 (abandono), +0,485 (scroll), −0,229 (tempo de clique). Argumento explícito de que as relações parecem lineares nos scatters, justificando regressão linear.

### Parte 2 — Modelo

MAE (0,276) e RMSE (0,344) citados. R² = 0,714 calculado e reportado. Coeficientes padronizados calculados (abandono −0,652, scroll +0,458, tempo −0,329). MAE representando 4,70% da média da conversão. Análise de resíduos (scatter e histograma) e checagem de generalização treino/teste (MAE teste = 0,249). Interpretação completa e coerente.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida (abandono e scroll). Tabela gerada: abandono −0,489, scroll +0,258. Ranking completo das três variáveis calculado adicionalmente (tempo −0,112). Tornado diagram gerado com variação de ±10% em pontos percentuais absolutos (abandono ±0,287 p.p., scroll ±0,151 p.p., tempo ±0,066 p.p.). Tabela de robustez confirmando que os índices são idênticos para variações de 5%, 10% e 20%. Argumento: abandono tem ≈ 1,90× o impacto do scroll.

### Parte 4 — Decisão

Recomenda experimento de interface para reduzir abandono, medindo efeito causal por teste A/B (distinção associação/causalidade explícita). Cita índice −0,489 e traduz em valor de negócio (≈ 28,7 vendas extras/dia, ≈ R$ 129 mil/mês) com suposições explícitas. Limitações específicas: linearidade, OAT ignora covariância, base simulada de 180 dias sem sazonalidade, suposições de volume e ticket médio como ordem de grandeza.

### Ao Além dos Aléns (bônus)

Presente e substancialmente expandido. Monte Carlo com dois cenários sobrepostos (referência vs. abandono −10%), com ganho médio de 0,286 p.p. e probabilidade de ficar abaixo de 5% caindo de 1,4% para 0,1%. Segundo notebook separado com índices de Sobol (S1 abandono ≈ 0,67, scroll ≈ 0,22, tempo ≈ 0,13), bootstrap de 400 iterações com IC 95% confirmando ranking sem sobreposição, modelo com interações (ganho de R² = 0,0024 — desprezível), e tabela consolidada de quatro métricas de importância.

## Confiança

Confiança geral: Alta
Observação: o segundo notebook (`experimento_sobol_bootstrap.ipynb`) é trabalho adicional relevante que vai além de qualquer critério de bônus da atividade. Constitui análise de sensibilidade global completa e estatisticamente fundamentada.

============================================================
ESTUDANTE 11: Isadora Tribst Gatto | NOTA: 10,0
============================================================
# Avaliação - Isadora Tribst Gatto

Estudante: Isadora Tribst Gatto

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entrega de nível máximo em todas as partes. Isadora vai muito além do mínimo pedido: a exploração inclui mapa de calor, histogramas e scatters facetados para justificar tanto a escolha de variáveis quanto a hipótese de linearidade; o modelo inclui R² (0,714), coeficientes padronizados, análise de resíduos e divisão treino/teste; a análise de sensibilidade inclui tornado diagram, tabela de robustez (índices constantes em 5%, 10% e 20%) e ranking completo das três variáveis; e a Parte 4 inclui distinção explícita associação/causalidade, proposta de teste A/B, tradução do ganho esperado em valor de negócio (≈ R$ 129 mil/mês) com suposições explícitas, e limitações específicas da análise. O bônus de Monte Carlo é executado com comparação de dois cenários e quantificação de risco (probabilidade de cair abaixo de 5% caindo de 1,4% para 0,1%). A resposta não poderia valer para nenhum outro dataset — cada número citado é derivado deste notebook específico.

## Evidência

### Parte 1 — Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Mapa de calor (`px.imshow`), histogramas facetados das três variáveis de entrada e scatter facetado de cada variável vs. taxa de conversão. Justificativa: cita correlações −0,643 (abandono), +0,485 (scroll) e −0,229 (tempo), observa que as três variáveis têm distribuição aproximadamente normal e que os scatters indicam relação linear — o que justifica explicitamente o uso de regressão linear.

### Parte 2 — Modelo

MAE (0,276) e RMSE (0,344) citados. R² = 0,714, MAE representando 4,70% da média da conversão. Coeficientes padronizados calculados (abandono −0,650, scroll +0,457, tempo −0,329). Análise de resíduos (scatter e histograma) e checagem de generalização treino/teste (MAE teste = 0,249 ≈ MAE treino = 0,276). Interpreta os coeficientes padronizados para comparação justa entre variáveis de escalas diferentes.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida (abandono e scroll). Tabela: abandono −0,489, scroll +0,258. Ranking completo das três variáveis calculado adicionalmente (tempo −0,112). Tornado diagram gerado com ±10% em p.p. de conversão (abandono ±0,287, scroll ±0,151, tempo ±0,066). Tabela de robustez confirmando índices estáveis para variações de 5%, 10% e 20%. Abandono tem 1,90× o impacto do scroll.

### Parte 4 — Decisão

Recomenda priorizar redução do abandono e propõe teste A/B como validação (distinção associação/causalidade explícita). Cita índice −0,489 e traduz em valor de negócio: redução de 10% no abandono → +0,287 p.p. de conversão → ≈ 28,7 vendas extras/dia → ≈ R$ 129 mil/mês (com suposições declaradas). Limitações: linearidade e OAT, base simulada sem sazonalidade, suposições de volume e ticket como ordem de grandeza. Todas as limitações são específicas e relevantes.

### Ao Além dos Aléns (bônus)

Presente e executado. Simulação com dois cenários sobrepostos (situação atual vs. abandono −10%). Estatísticas: referência média 5,865%, P10 5,374%, P90 6,371%; cenário melhorado média 6,167%, P10 5,673%, P90 6,659%. Probabilidade de conversão abaixo de 5% caindo de 1,4% para 0,1%. Interpreta que a recomendação não apenas aumenta a média mas também reduz o risco de cenários ruins.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 12: Kaio Vittor Martins Silva | NOTA: 7,5
============================================================
# Avaliação - Kaio Vittor Martins Silva

Estudante: Kaio Vittor Martins Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

Kaio entregou as quatro partes e executou o bônus, mas assim como Igor, escolheu `tempo_primeiro_clique_s` como segunda variável e descartou o scroll com justificativa comportamental não fundamentada numericamente ("o engajamento dele é menor e a chance de converter cai" — argumento verdadeiro mas que não diferencia o tempo do clique do scroll, que tem correlação maior). As partes 3 e 4 citam valores da tabela corretamente dentro das variáveis escolhidas, e a Parte 4 menciona explicitamente que correlação não é causalidade. A limitação de sazonalidade e linearidade também é válida. O bônus está presente com estatísticas corretas e interpretação adequada de risco. A nota reflete entrega completa com lacuna analítica na justificativa de escolha de variáveis, que é o ponto central da Parte 1.

## Evidência

### Parte 1 — Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Scatter com `trendline="ols"` gerado. Scatter matrix adicional. Correlações citadas corretamente (r = −0,643, r = +0,485, r = −0,229). Escolhe `taxa_abandono_carrinho_pct` e `tempo_primeiro_clique_s`, descartando o scroll com argumento comportamental ("usuário rola sem comprar") que contradiz a força da correlação observada (+0,485 vs −0,229) sem evidência numérica adicional.

### Parte 2 — Modelo

MAE (0,348) e RMSE (0,452) citados com definições corretas de MAE e RMSE. Contextualiza erro relativo (5,93% da média). Compara com o modelo de 3 variáveis: MAE ≈ 26% maior pela exclusão do scroll — evidência de que a escolha custou qualidade ao modelo, reconhecida pelo próprio estudante.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas` preenchida (abandono e tempo). Tabela gerada com índices: abandono −0,511, tempo −0,105. Cita valores e calcula que abandono tem impacto ≈ 4,9× maior que tempo. Tabela e gráfico de barras adicionais. Interpretação correta dentro das variáveis escolhidas.

### Parte 4 — Decisão

Recomenda priorizar redução do abandono, cita índice −0,489 (nota: usa o índice do modelo de 3 variáveis mencionado no contexto da atividade, mas seu próprio modelo produziu −0,511 — inconsistência menor). Propõe ações concretas (alertas de carrinho, checkout simplificado, barra de progresso). Reconhece explicitamente que "correlação não é causalidade". Limitações: variáveis externas não mapeadas, instabilidade do modelo com sazonalidade, saturação da relação linear. Específicas e relevantes.

### Ao Além dos Aléns (bônus)

Presente e executado (modelo com duas variáveis). Estatísticas corretas (média 5,859%, std 0,342, P10 = 5,407%, P90 = 6,292%, amplitude = 0,885 p.p.). Interpreta risco: mesmo no pior decil a conversão fica bem acima do mínimo histórico. Menciona risco de variáveis saírem totalmente do padrão histórico. Interpretação adequada.

## Confiança

Confiança geral: Alta
Observação: a inconsistência no índice de sensibilidade citado na Parte 4 (−0,489 vs −0,511 do próprio modelo) é menor e provavelmente reflexo de ter lido o número do enunciado do problema.

============================================================
ESTUDANTE 13: Leonardo Nigri Griner | NOTA: 10,0
============================================================
# Avaliação - Leonardo Nigri Griner

Estudante: Leonardo Nigri Griner

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entrega exemplar em todas as dimensões. As quatro partes foram respondidas com números concretos do notebook — correlações (-0,643 e +0,485), MAE (0,276) e RMSE (0,344) interpretados em relação à escala da conversão, índices de sensibilidade (-0,489 e +0,258) citados e explicados com sinal e magnitude. O bônus de Monte Carlo foi executado e interpretado com risco quantificado: 17% de chance de conversão abaixo de 5,5%, percentis P10 (5,38%) e P90 (6,35%) usados para delimitar a faixa provável. A nota máxima se sustenta também pelas extensões voluntárias: ranking das três variáveis para validar a priorização e cálculo de inversão de objetivo (redução necessária no abandono para ganhar 0,25 p.p. de conversão).

## Evidência

### Parte 1 — Exploração

`variavel_x = "profundidade_scroll_pct"` preenchida e scatter gerado. Tabela de correlação exibida com todos os valores. Justificativa explícita: abandonou o tempo do primeiro clique por correlação fraca (-0,229) e escolheu abandono (-0,643) e scroll (+0,485) por maior força de sinal — raciocínio ancorado nos números.

### Parte 2 — Modelo

MAE = 0,276 e RMSE = 0,344 citados explicitamente. Interpretação relativa à escala da conversão presente ("erro médio ficou perto de 0,28 ponto percentual"). Observou que o RMSE > MAE indica erros assimétricos, e reconheceu que o erro é aceitável para decisão de produto.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida corretamente; `tabela_sensibilidade` gerada com output visível. Citou valores precisos da tabela: abandono de 5,869 → 5,582 (variação -4,891%, índice -0,489); scroll de 5,869 → 6,020 (+2,578%, índice +0,258). Interpretou sinal e magnitude comparativos.

### Parte 4 — Decisão

Recomendação concreta de produto (simplificar checkout, reduzir etapas, clareza de frete) ancorada no índice -0,489 do abandono. Limitação específica e não genérica: modelo linear sobre dados simulados ignora fatores externos (promoções, preço, campanhas), coeficientes dependem da relação linear entre as variáveis, e a variação de 10% é local. Não declarou causalidade: "o número deve ser lido como estimativa de direção, não garantia."

### Ao Além dos Aléns (bônus)

Presente e completo. Simulação de Monte Carlo executada (1000 amostras), tabela de percentis exibida, histograma gerado. Interpretação com risco quantificado: 17% de chance de conversão < 5,5%, faixa P10–P90 de 5,38%–6,35%. Recomendou rollout gradual ou teste A/B dado o risco. Adicionou cálculo extra de inversão de objetivo (redução de 4,14 p.p. no abandono ≈ 8,71% relativo para ganhar 0,25 p.p. de conversão) e ranking completo das três variáveis.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 14: Leonardo Souza Martins | NOTA: 9,5
============================================================
# Avaliação - Leonardo Souza Martins

Estudante: Leonardo Souza Martins

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Entrega de alto nível com análise analiticamente autoral. O estudante foi o único do lote a explorar a distinção entre coeficiente bruto (β) e índice de sensibilidade por escala de variável, identificando corretamente que o tempo do primeiro clique tem maior impacto por unidade, mas que o scroll domina em variação percentual relativa — raciocínio que transcende o template da atividade. Monte Carlo executado e interpretado com percentis. A nota fica ligeiramente abaixo de 10 por dois pontos: na Parte 3, escolheu scroll e tempo (não abandono) como as duas variáveis analisadas, deixando de fora a de maior impacto absoluto; e a Parte 4 (decisão de produto e limitação) foi inserida em uma única célula, com a recomendação de produto presente mas sem citar os números da tabela de sensibilidade da Parte 3 diretamente no texto de decisão.

## Evidência

### Parte 1 — Exploração

`variavel_x = ["profundidade_scroll_pct", "tempo_primeiro_clique_s"]` preenchida com lista (comportamento não padrão, mas que gerou os gráficos). Correlações citadas corretamente: scroll r = +0,485, tempo r = -0,229. Justificativa rica: comparou coeficiente bruto (β = -0,085 do tempo vs β = +0,026 do scroll) com a amplitude de variação das variáveis, concluindo que o scroll explica mais variância total enquanto o tempo tem maior impacto unitário.

### Parte 2 — Modelo

MAE = 0,276 e RMSE = 0,344 exibidos. Interpretação profunda: identificou o ruído injetado (σ = 0,35) e comparou com o RMSE (0,344), concluindo que o modelo atingiu "virtualmente o limite teórico". Contextualizou o erro relativo (~5% da média). Distinção MAE/RMSE explicada corretamente.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas = ["profundidade_scroll_pct", "tempo_primeiro_clique_s"]`. Tabela gerada com output. Índices citados: scroll +0,258, tempo -0,112. Análise comparativa detalhada com explicação de por que o impacto relativo (índice) difere do impacto por unidade (coeficiente bruto). Variável de maior impacto absoluto (abandono, índice -0,489) não foi incluída na análise das duas variáveis escolhidas.

### Parte 4 — Decisão

Recomendação presente: priorizar scroll com ações concretas de UI (sticky CTAs, barras de progresso, conteúdo acima da dobra). Citou índice +0,258 e ganho de +2,578% para 10% de melhora no scroll. Distinguiu associação de causalidade com clareza ("usuário que já tem intenção de compra naturalmente rola mais"). Limitação específica: risco de causalidade reversa, premissa de linearidade e necessidade de teste A/B — todas não genéricas.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras, percentis exibidos (P10 = 5,369%, P90 = 6,379%). Interpretação com risco: comparou o ganho esperado do scroll (~0,15 p.p.) com a variação natural da distribuição (desvio padrão ~0,39), concluindo que o sinal pode ser "engolido" pela flutuação do dia a dia sem teste A/B controlado.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 15: Marcelo Faska Sitton | NOTA: 8,5
============================================================
# Avaliação - Marcelo Faska Sitton

Estudante: Marcelo Faska Sitton

Rubrica: `../../../rubrica_s10.md`

Nota: 8,5

Feedback:

Entrega completa com todas as quatro partes respondidas e Monte Carlo executado. As correlações foram citadas com valores corretos (-0,643 e +0,485), a tabela de sensibilidade foi gerada, e a Parte 4 distinguiu associação de causalidade com cuidado. O que reduz a nota em relação ao teto é a escolha de treinar o modelo apenas com duas features (abandono e scroll, sem o tempo do primeiro clique), o que alterou os índices de sensibilidade — -0,461 e +0,250 em vez dos valores de referência -0,489 e +0,258 — sem que o estudante tenha apontado essa diferença ou justificado a escolha de excluir a terceira variável do modelo. A interpretação do Monte Carlo, embora presente e coerente, não citou percentis concretos da tabela descritiva.

## Evidência

### Parte 1 — Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Gráfico de barras adicional de correlação (seaborn) e scatter secundário para scroll. Justificativa com valores concretos: abandono r = -0,643 ("maior impacto na queda da conversão") e scroll r = +0,485 ("maior correlação positiva"). Raciocínio ancorado nos dados.

### Parte 2 — Modelo

Modelo ajustado apenas com duas features (abandono e scroll), gerando MAE = 0,317 e RMSE = 0,402 — valores ligeiramente superiores ao modelo com três features. A interpretação reconhece os valores como "baixos e seguros, inferiores a meio ponto percentual", e compara MAE com RMSE para afirmar consistência do modelo. Não contextualizou o erro relativo à média da conversão (~5,87%) nem comparou com o modelo de três features.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida; `tabela_sensibilidade` gerada. Índices: abandono -0,461, scroll +0,250 (diferem dos valores de referência pois o modelo da Parte 2 usa apenas 2 features). Análise comparativa presente: "magnitude do impacto do abandono supera consideravelmente o scroll", com valores da tabela citados (saída de 5,869 → 5,598 para abandono; → 6,015 para scroll).

### Parte 4 — Decisão

Recomendação concreta: one-page checkout e compra como convidado. Citou índice -0,461 e variação de -4,612% na conversão para 10% de aumento no abandono. Distinguiu associação de causalidade: "a taxa de abandono é apenas o sintoma do problema"; discutiu viés de variável omitida (frete, prazo de entrega, opções de pagamento). Limitação específica e bem desenvolvida.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras sobre as duas features do modelo. Percentis exibidos (P10 = 5,449%, P90 = 6,307%). Interpretação qualitativa presente ("risco baixo e cenário altamente previsível"), mas não citou os percentis numericamente nem comparou o ganho esperado com o desvio da distribuição.

## Confiança

Confiança geral: Alta
Observação: os índices de sensibilidade diferem dos valores de referência porque o modelo foi treinado apenas com duas variáveis (sem o tempo do primeiro clique). A análise é internamente consistente, mas o estudante não justificou essa escolha.

============================================================
ESTUDANTE 16: Marcelo Rubim Rossignolli | NOTA: 9,0
============================================================
# Avaliação - Marcelo Rubim Rossignolli

Estudante: Marcelo Rubim Rossignolli

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Entrega completa e sólida em todas as quatro partes, com Monte Carlo executado e interpretado. Os números concretos estão presentes em todas as seções: correlações (-0,643 e +0,485), MAE (0,276) e RMSE (0,344) interpretados em relação à média da conversão (5,87%) e ao ruído do dataset, índices de sensibilidade (-0,489 e +0,258) citados e conectados à decisão, percentis do Monte Carlo discutidos em termos de risco. A Parte 4 distingue associação de causalidade com clareza e propõe limitação específica (modelo linear ignora interações e a variação de 10% é local). O que distingue da nota 10 é que a exploração adicional foi mais enxuta do que nos dois Leonardos — sem extensões voluntárias — e a interpretação do Monte Carlo, embora correta, não quantificou a probabilidade de cenários adversos.

## Evidência

### Parte 1 — Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Scatter secundário para scroll adicionado. Justificativa com correlações citadas numericamente: abandono r = -0,643, scroll r = +0,485, tempo r = -0,229 (excluído por correlação fraca). Raciocínio direto e ancorado.

### Parte 2 — Modelo

MAE = 0,276 e RMSE = 0,344 exibidos. Interpretação em relação à média da conversão (5,87%): "erro médio representa menos de 5% do valor". Comparação MAE vs RMSE: "não há outliers dominando o ajuste". Observação extra: RMSE próximo ao desvio padrão do ruído (0,35) sugere que o modelo recuperou quase toda a estrutura dos dados — raciocínio correto e específico.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida; `tabela_sensibilidade` gerada com output correto. Índices -0,489 e +0,258 citados. Análise: "o módulo de -0,489 é quase o dobro do de +0,258, então a taxa de abandono é a variável com maior impacto". Valores da tabela (saída original, nova e variação %) citados na resposta. Célula extra de ranking por magnitude adicionada.

### Parte 4 — Decisão

Recomendação com números: reduzir abandono em 10% (de 47,55 → 42,79) elevaria a conversão prevista em ~4,9%, de 5,869 para ~6,16. Ações concretas: reduzir etapas do checkout, mostrar frete antecipadamente, reduzir campos obrigatórios. Limitação não genérica: variação de 10% é perturbação local, o modelo assume linearidade, a interação entre variáveis é ignorada, e fatores externos (preço, estoque, confiança) não estão no modelo. Célula extra de código calculando o efeito de reduzir abandono em 10% com output numérico.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras, percentis exibidos (P10 = 5,369%, P90 = 6,379%, mínimo = 4,654%). Interpretação: faixa P10–P90 estreita (~1 p.p.), ganho esperado ao reduzir abandono (~0,29 p.p.) é da "mesma ordem do desvio da simulação", portanto perceptível. Observação extra: o Monte Carlo só propaga incerteza das entradas, não o erro do modelo (RMSE = 0,34), então o P10 real é mais pessimista do que o simulado.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 17: Mariana de Paula Barbosa Souza | NOTA: 9,0
============================================================
# Avaliação - Mariana de Paula Barbosa Souza

Estudante: Mariana de Paula Barbosa Souza

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Entrega completa em todas as quatro partes, com Monte Carlo executado e interpretado. Os valores concretos estão presentes: correlações (-0,643 e +0,485), MAE (0,276) e RMSE (0,344) contextualizados em relação à média da conversão (~5,87%), índices de sensibilidade (-0,489 e +0,258) citados com sinal e magnitude, e distribuição Monte Carlo discutida em termos de risco. A Parte 4 distingue associação de causalidade e propõe limitação específica (modelo linear ignora interações entre variáveis e fatores externos). O que separa da nota 10 é que as respostas textuais são mais concisas e diretas sem extensões analíticas voluntárias, e a interpretação do Monte Carlo — embora correta — não quantificou probabilidades de risco (como chance de ficar abaixo de um limiar) nem comparou o ganho esperado com o desvio da distribuição.

## Evidência

### Parte 1 — Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Scatter secundário para scroll adicionado. Justificativa com valores numéricos: abandono r = -0,643 ("maior impacto na queda"), scroll r = +0,485 ("maior correlação positiva"). Excluiu tempo do primeiro clique por correlação fraca (-0,229). Evidência ancorada nos dados.

### Parte 2 — Modelo

MAE = 0,276 e RMSE = 0,344 citados. Interpretação: "erro médio inferior a 5% da média" e "RMSE próximo ao MAE indica ausência de erros extremos". Acrescentou que o RMSE é próximo ao ruído do dataset (σ = 0,35), reconhecendo que o modelo atingiu o limite do que é recuperável — raciocínio avançado e específico.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida; `tabela_sensibilidade` gerada com output. Índices -0,489 e +0,258 citados. Análise comparativa: "abandono é quase o dobro do scroll". Saídas da tabela referenciadas (5,869 → 5,582 para abandono; → 6,020 para scroll). Interpretação de sinal e magnitude presente.

### Parte 4 — Decisão

Recomendação concreta: simplificar checkout (menos etapas, frete transparente, login/convidado facilitado). Citou índice -0,489 e ganho de ~4,9% para redução de 10% no abandono. Limitação específica: "modelo linear ignora interações entre as variáveis e fatores externos como sazonalidade, campanhas e preço"; afirmou que "a sensibilidade mostra associação dentro do modelo, não causalidade garantida" — distinção explícita e precisa.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras, percentis exibidos (P10 = 5,369%, P90 = 6,379%). Interpretação: distribuição estreita com desvio padrão ~0,39; faixa P10–P90 de ~1 p.p.; robustez "alta". Não quantificou probabilidade de cenários adversos abaixo de um limiar nem comparou o ganho esperado (~0,29 p.p.) com o desvio da simulação.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 18: Matheus Fernandes Guimarães de Sousa | NOTA: 8,0
============================================================
# Avaliação - Matheus Fernandes Guimaraes de Sousa

Estudante: Matheus Fernandes Guimaraes de Sousa

Rubrica: `../../../rubrica_s10.md`

Nota: 8,0

Feedback:

Entrega completa com todas as quatro partes e Monte Carlo executado. Os valores concretos estão presentes nas partes que mais importam: correlações citadas (-0,643 e +0,485), índices de sensibilidade (-0,489 e +0,258) comparados com sinal e magnitude, recomendação ancorada no índice maior. A Parte 2 contextualiza o MAE em relação à média da conversão e distingue MAE de RMSE. A Parte 4 menciona associação versus causalidade e propõe limitação relevante. O que reduz a nota é a superficialidade da interpretação do Monte Carlo — a resposta ("fica quase toda entre 5,4% e 6,4%") não cita os percentis da tabela descritiva gerada pelo código nem discute o que a dispersão implica para o risco da recomendação. Algumas respostas (especialmente Parte 3 e Monte Carlo) são as mais curtas e menos aprofundadas do lote.

## Evidência

### Parte 1 — Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Também adicionou matriz de correlação visual (heatmap) e tabela de conversão média por quartil do abandono (Q1 = 6,41%, Q4 = 5,38%) — esforço exploratório acima do mínimo. Justificativa com correlações citadas: abandono r = -0,643, scroll r = +0,485, tempo r = -0,229 (excluído por correlação fraca). Concisa mas ancorada em evidências.

### Parte 2 — Modelo

MAE = 0,276 e RMSE = 0,344 citados. Interpretação: "erra só 0,28 ponto em média (MAE), menos de 5% disso" — relação percentual com a média presente. Distinguiu que RMSE próximo ao MAE indica ausência de erros grandes. Resposta correta mas a mais curta do lote na Parte 2.

### Parte 3 — Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida; `tabela_sensibilidade` gerada com output correto. Índices -0,489 e +0,258 mencionados na resposta. Comparação: "abandono é quase o dobro do scroll". Valores da tabela citados numericamente (5,87% → 5,58% para abandono; → 6,02% para scroll). Análise correta e suficiente, sem aprofundamento adicional.

### Parte 4 — Decisão

Recomendação: focar em reduzir abandono, simplificar checkout, mostrar frete mais cedo. Citou índice -0,489 e ganho de ~4,9% para redução de 10% no abandono. Limitação mencionada explicitamente: "correlação não prova causa" e "modelo linear ignora interações entre as variáveis". Distinguiu associação de causalidade de forma direta e concisa.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras, tabela de percentis gerada com output (P10 = 5,369%, P90 = 6,379%). Interpretação superficial: "fica quase toda entre 5,4% e 6,4%, com mediana ~5,85%. A distribuição é estreita, então a recomendação é segura." Não citou os percentis numericamente da tabela, não quantificou probabilidade de risco abaixo de limiar, e não conectou a dispersão ao ganho esperado da recomendação.

## Confiança

Confiança geral: Alta
Observação: o notebook está completo e os outputs são consistentes. A avaliação reflete a profundidade analítica das respostas textuais, não eventuais dificuldades de execução.

============================================================
ESTUDANTE 19: Mirella Borim Lima | NOTA: 8,0
============================================================
# Avaliação - Mirella Borim Lima

Estudante: Mirella Borim Lima

Rubrica: `../../../rubrica_s10.md`

Nota: 8,0

Feedback:

A entrega cobre as quatro partes obrigatórias com citação de valores concretos do notebook — correlações, MAE/RMSE e índices de sensibilidade. A Parte 3 está bem executada: variaveis_escolhidas preenchida corretamente, tabela gerada, índices citados com sinal e magnitude. A Parte 4, porém, mistura a resposta de "recomendação com índice" e a resposta de "limitação" em células separadas trocadas — a célula de limitação descreve uma ação de produto (simplificar checkout), e a célula de recomendação cita o índice sem apontar explicitamente a direção inversa (reduzir o abandono). A interpretação do MAE/RMSE na Parte 2 reconhece que os erros são "relativamente baixos", mas não ancora essa afirmação na escala da variável alvo (~5–9%), o que a torna levemente genérica. O bônus de Monte Carlo foi executado (código fornecido), com estatísticas descritivas e histograma, e a interpretação menciona média (5,87%), desvio (0,35), intervalo P10–P90 (5,43%–6,32%) e risco baixo — satisfatório, mas sem profundidade analítica extra.

## Evidência

### Parte 1 — Exploração

variavel_x = "taxa_abandono_carrinho_pct" e variavel_x2 = "profundidade_scroll_pct" preenchidas; scatter e heatmap gerados. Justificativa cita correlações concretas: −0,643 para abandono e +0,485 para scroll, com explicação do sinal de cada uma. Evidência numérica presente.

### Parte 2 — Modelo

MAE = 0,317 e RMSE = 0,402 (modelo rodado apenas com 2 features em vez de 3, o que explica os valores levemente piores que o esperado). Interpretação reconhece erros "relativamente baixos" e diferença MAE vs. RMSE, mas não compara explicitamente à média da conversão (~5,87%) ou à amplitude da escala — falta âncora quantitativa.

### Parte 3 — Análise de Sensibilidade

variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]. Tabela gerada com índice −0,461 (abandono) e +0,250 (scroll) — valores ligeiramente diferentes do esperado por usar modelo com 2 features. Cita ambos os índices e conclui corretamente que o abandono tem maior impacto absoluto. Sinal e magnitude interpretados.

### Parte 4 — Decisão

A célula de recomendação cita o índice de −0,461 e conclui que o abandono deve ser priorizado, mencionando queda de ~4,6% na conversão. A célula de "limitação" descreve uma ação de produto (checkout mais simples), invertendo as células — ausência de limitação analítica explícita (sem distinção de causalidade, sem limitação específica ao modelo ou aos dados).

### Ao Além dos Aléns (bônus)

Presente e executado. Código do Monte Carlo rodado, estatísticas descritivas geradas (média 5,87%, std 0,35, P10 5,43%, P90 6,32%), histograma plotado. Interpretação cita esses valores e conclui que o risco é baixo. Não vai além do código fornecido, mas a interpretação é satisfatória.

## Confiança

Confiança geral: Alta
Nota reduzida em relação à faixa 9,0 por: (1) modelo da Parte 2 e 3 usando apenas 2 features, gerando índices fora do intervalo de referência; (2) Parte 4 com células invertidas — limitação ausente e recomendação incompleta quanto à causalidade.

============================================================
ESTUDANTE 20: Moyses Birman Anijar | NOTA: 9,0
============================================================
# Avaliação - Moyses Birman Anijar

Estudante: Moyses Birman Anijar

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Entrega consistente e bem ancorada numericamente em todas as quatro partes. Parte 1 justifica a escolha das duas variáveis com ranking de correlações em módulo, gráfico de barras e scatter com OLS. Parte 2 interpreta MAE (0,276) e RMSE (0,344) em relação à média da conversão (5,87%), calcula R² (0,714) e razão MAE/média (4,7%) — análise claramente acima do esperado. Parte 3 cita os índices exatos (−0,489 e +0,258) com sinal, magnitude e comparação relativa (quase 1,9× de diferença). Parte 4 aponta ação concreta, cita os índices, e a limitação aborda tanto linearidade quanto independência das variáveis — duas restrições específicas ao modelo, não genéricas. O bônus do Monte Carlo foi executado com todas as 3 features, estatísticas descritivas geradas e interpretação que menciona P10 (5,37%), P90 (6,38%), chance de cair abaixo de 5% (~1%) e abaixo de 5,5% (~17,5%). A única lacuna é não distinguir explicitamente associação de causalidade em linguagem direta na Parte 4 — a limitação de linearidade é mencionada, mas a distinção correlação/causalidade aparece apenas de forma implícita.

## Evidência

### Parte 1 — Exploração

variavel_x = "taxa_abandono_carrinho_pct", scatter com OLS gerado. Justificativa cita r = −0,643, +0,485 e −0,229, com gráfico de barras das correlações em módulo. Escolha justificada com evidência numérica e raciocínio sobre sinal.

### Parte 2 — Modelo

MAE = 0,276, RMSE = 0,344 (modelo com 3 features, valores dentro do intervalo de referência). Interpreta em relação à média (4,7% do valor médio), calcula R² = 0,714 e razão RMSE/desvio = 0,534. Conclui que o modelo é suficiente para análise de sensibilidade, não para previsão de precisão.

### Parte 3 — Análise de Sensibilidade

variaveis_escolhidas corretas. Tabela mostra índice −0,489 (abandono) e +0,258 (scroll). Cita ambos com sinal, compara em módulo (0,489 vs. 0,258, diferença de ~1,9×), interpreta a direção de cada um e calcula explicitamente o ganho absoluto (conversão 5,87% → 6,16% com redução de 10% no abandono).

### Parte 4 — Decisão

Recomendação de reduzir abandono citando índice −0,489 e ganho de +0,287 p.p. (+4,89%). Limitações específicas: (1) linearidade pode não valer (saturação); (2) análise ceteris paribus ignora interações entre variáveis. Não usa a palavra "causalidade" explicitamente, mas a limitação de confundimento está presente de forma implícita.

### Ao Além dos Aléns (bônus)

Presente e bem executado. Monte Carlo com 3 features, estatísticas descritivas completas, cálculo de P(conversão < 5,0%) = 1%, P(< 5,5%) = 17,5%, intervalo P10–P90. Interpretação integra o risco à recomendação e menciona que o downside simulado é limitado.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 21: Paulo Octavio de Paula | NOTA: 7,5
============================================================
# Avaliação - Paulo Octavio de Paula

Estudante: Paulo Octavio de Paula

Rubrica: `../../../rubrica_s10.md`

Nota: 7,5

Feedback:

A entrega cobre as quatro partes obrigatórias e executa o bônus de Monte Carlo, com as variáveis corretas e tabelas geradas. Os números concretos estão presentes (correlações, MAE/RMSE, índices), mas as respostas discursivas tendem a parafrasear os resultados sem conectá-los a uma conclusão analítica própria. A Parte 2 menciona MAE (0,276) e RMSE (0,344), diferença entre as duas métricas, mas não ancora os valores na escala da conversão (~5,87%) de forma explícita — diz "erros são relativamente baixos" sem comparação quantitativa. A Parte 4 apresenta recomendação razoável e cita o índice de sensibilidade, mas a célula de limitação é genérica (fatores externos não capturados, ceteris paribus), sem apontar uma restrição específica ao modelo ou ao dataset. O bônus foi executado, mas a interpretação não vai além de reproduzir as estatísticas descritivas e concluir que "não há grande concentração de cenários extremos" — sem quantificar o risco em probabilidades concretas.

## Evidência

### Parte 1 — Exploração

variavel_x = "taxa_abandono_carrinho_pct" preenchida, scatter gerado. Justificativa cita correlações −0,643 e +0,485, menciona o terceiro valor (−0,229) como critério de exclusão. Evidência numérica presente, raciocínio claro.

### Parte 2 — Modelo

MAE = 0,276 e RMSE = 0,344 exibidos. Interpretação menciona que MAE indica margem de erro de 0,28 p.p. e que RMSE penaliza erros maiores, e conclui que o modelo é "adequado". Falta comparar 0,276 com a média da taxa de conversão (5,87%) ou com a amplitude da escala para quantificar a adequação.

### Parte 3 — Análise de Sensibilidade

variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]. Tabela gerada com índice −0,489 e +0,258. Interpretação cita os dois valores em módulo, conclui que o abandono tem maior impacto e recomenda prioridade. Sinal e direção corretos.

### Parte 4 — Decisão

Recomendação cita índice de sensibilidade e aponta ações (simplificar checkout, reduzir etapas). Limitação menciona fatores externos não capturados e que a análise assume ceteris paribus — válido, mas genérico; não aponta limitação específica ao modelo linear ou ao processo gerador dos dados.

### Ao Além dos Aléns (bônus)

Presente. Código do Monte Carlo executado com 3 features. Estatísticas descritivas geradas (média 5,87%, std 0,39, P10–P90: 5,37%–6,38%). Interpretação menciona formato próximo ao normal e conclui que há "baixo risco", mas sem quantificar probabilidades concretas (e.g., P(conversão < 5%) ou P(> 6%)). Satisfatório mas superficial.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 22: Pedro El Haouli Faria | NOTA: 10,0
============================================================
# Avaliação - Pedro El Haouli Faria

Estudante: Pedro El Haouli Faria

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entrega de nível máximo. Todas as quatro partes estão completas com números concretos do notebook, raciocínio analítico explícito e conclusões que não poderiam valer para qualquer outro dataset. A Parte 1 vai além do mínimo: scatter com OLS, heatmap, três scatter plots lado a lado com linha de tendência e impressão do ranking de correlações no console. A Parte 2 calcula R² (0,714), MAPE (4,77%) e valida temporalmente (treino/teste com MAE estável em 0,264 no teste). A Parte 3 apresenta tornado chart com as três variáveis, compara amplitude de variação (±0,574 p.p. para abandono vs. ±0,303 para scroll vs. ±0,131 para tempo) e tabela de cenários de melhoria. A Parte 4 distingue explicitamente associação de causalidade, propõe teste controlado e quantifica o ganho esperado. O bônus implementa Monte Carlo comparando cenário base vs. cenário de recomendação (abandono −10%), calcula probabilidades concretas (P(< 5,5%) cai de 23,89% para 10,64%; P(> 6%) sobe de 39,96% para 61,82%) e usa n=10.000 amostras com erro residual do modelo incluído — análise de risco bem acima do esperado.

## Evidência

### Parte 1 — Exploração

variavel_x = "taxa_abandono_carrinho_pct" preenchida. Três scatter com linha de tendência, heatmap, ranking de correlações impresso (−0,643; +0,485; −0,229). Justificativa usa tabela markdown com correlações e r² individual. Evidência sólida, sem frases genéricas.

### Parte 2 — Modelo

MAE = 0,276, RMSE = 0,344, R² = 0,714, MAPE = 4,77%. Validação temporal (treino 80%/teste 20%) com MAE no teste = 0,264 — modelo estável. Interpreta que o erro é ~4,7% da média da conversão e conclui com distinção clara entre uso para comparação de sensibilidade vs. previsão de precisão.

### Parte 3 — Análise de Sensibilidade

variaveis_escolhidas corretas. Tabela com índice −0,489 e +0,258. Tornado chart adicionado com todas as 3 variáveis. Tabela estendida com cenário de "melhoria esperada" (reduzir abandono: +0,287 p.p.; aumentar scroll: +0,151 p.p.; reduzir tempo: +0,066 p.p.). Interpretação compara os três índices com magnitudes e sinais corretos.

### Parte 4 — Decisão

Recomendação cita índice −0,489, quantifica ganho (5,87% → 6,16%, +0,287 p.p.), propõe ações concretas (fluxo de carrinho, transparência de frete). Limitação distingue explicitamente associação de causalidade, menciona variáveis de confusão e propõe validação por experimento controlado — não genérico.

### Ao Além dos Aléns (bônus)

Presente e exemplar. Monte Carlo com n=10.000, cenário base vs. recomendação comparados. P(conversão < 5,5%) cai de 23,89% para 10,64%; P(> 6%) sobe de 39,96% para 61,82%. Inclui erro residual do modelo na simulação. Histograma comparativo com sobreposição. Ganho médio simulado calculado (0,283 p.p.). Interpretação conecta o risco à recomendação e menciona a necessidade de teste A/B.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 23: Ricardo de Toledo Planas | NOTA: 10,0
============================================================
# Avaliação - Ricardo de Toledo Planas

Estudante: Ricardo de Toledo Planas

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entrega completa, com alto nível analítico em todas as partes. A Parte 1 inclui exploração por quartis além da correlação, o que demonstra compreensão da relação entre as variáveis além do coeficiente linear. A Parte 2 calcula R² (0,714), MAPE (4,77%), coeficientes padronizados (beta normalizados) e faz validação temporal, indo bem além do mínimo. A Parte 3 inclui tornado chart com as 3 variáveis, tabela de cenários isolados e combinados, e identifica que reduzir abandono em 10% eleva a conversão de 5,87% para 6,16% (+0,287 p.p.). A Parte 4 distingue explicitamente associação de causalidade, propõe teste A/B e aponta quatro limitações específicas: causalidade vs. correlação, linearidade, dados sintéticos e independência das variáveis. O bônus de Monte Carlo foi executado comparando cenário base vs. recomendação (abandono −10%), com probabilidades quantificadas, sobreposição das distribuições e ganho mediano calculado (0,283 p.p.) — nível máximo de execução.

## Evidência

### Parte 1 — Exploração

variavel_x = "taxa_abandono_carrinho_pct". Scatter com OLS, heatmap, scatter das 3 features lado a lado, análise por quartis (conversão média de 6,41% no Q1 vs. 5,38% no Q4 do abandono). Justificativa usa tabela markdown com correlações e r² individuais. Evidência numérica múltipla e coerente.

### Parte 2 — Modelo

MAE = 0,276, RMSE = 0,344, R² = 0,714, MAPE = 4,77%. Coeficientes padronizados calculados (beta abandono = −0,650, scroll = +0,457, tempo = −0,328). Validação temporal treino/teste (MAE no teste = 0,264). Interpreta cada métrica em relação à escala da conversão e conclui que o modelo é adequado para comparação de sensibilidade.

### Parte 3 — Análise de Sensibilidade

variaveis_escolhidas corretas. Tabela com índice −0,489 e +0,258. Tornado chart com 3 variáveis (amplitude: abandono ±0,574 p.p., scroll ±0,303 p.p., tempo ±0,131 p.p.). Tabela de cenários: redução isolada e combinada de 10% e 5%. Comparativo correlação × coeficiente × sensibilidade em tabela.

### Parte 4 — Decisão

Recomendação cita índice −0,489, ganho de +0,287 p.p. (+4,89%), ações concretas (simplificar checkout, frete transparente, recuperação de carrinho). Limitação aponta 4 restrições específicas: (1) causalidade, (2) linearidade, (3) dados sintéticos, (4) independência das variáveis. Propõe validação por experimento controlado. Distinção associação/causalidade explícita.

### Ao Além dos Aléns (bônus)

Presente e exemplar. Monte Carlo com n=10.000 comparando base vs. recomendação. P(< 5,5%) cai de 23,89% para 10,64%; P(> 6%) sobe de 39,96% para 61,82%. Inclui erro residual do modelo na simulação. Histograma comparativo sobreposto. Ganho médio e mediano calculados (0,283 p.p.). Interpretação conecta risco à recomendação e menciona necessidade de teste A/B.

## Confiança

Confiança geral: Alta

============================================================
ESTUDANTE 24: Stefano Tamer Parente | NOTA: 9,0
============================================================
# Avaliação - Stefano Tamer Parente

Estudante: Stefano Tamer Parente

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Entrega sólida em todas as quatro partes, com citação consistente de valores concretos e raciocínio bem conectado. A Parte 1 apresenta correlações, scatter com OLS e ranking impresso no console. A Parte 2 interpreta MAE (0,276) e RMSE (0,344) em relação à amplitude da taxa de conversão (4,35%–7,75%) e calcula coeficientes padronizados — análise acima do mínimo. A Parte 3 cita os índices (−0,489 e +0,258), compara em módulo e inclui gráfico de barras dos índices. A Parte 4 recomenda reduzir o abandono citando o índice e estima o ganho (5,87% → ~6,16%); a limitação aponta corretamente a hipótese de linearidade e a análise ceteris paribus. O bônus foi executado com o código fornecido e a interpretação quantifica o risco via intervalo P10–P90 (5,37%–6,38%) e menciona o pior cenário (4,65%). A nota não alcança 10,0 porque a Parte 4 não distingue explicitamente associação de causalidade em linguagem direta — a limitação está presente mas não usa esse enquadramento — e a interpretação do Monte Carlo não calcula probabilidades concretas além dos percentis descritos.

## Evidência

### Parte 1 — Exploração

variavel_x = "taxa_abandono_carrinho_pct", scatter com OLS gerado. Justificativa cita r = −0,643, +0,485 e −0,229, com print do ranking e descarte do tempo de clique justificado pela relação "mais espalhada, menos clara visualmente". Evidência numérica presente.

### Parte 2 — Modelo

MAE = 0,276, RMSE = 0,344. Interpreta em relação à faixa 4,35%–7,75% (~8% da amplitude). Calcula coeficientes padronizados (beta abandono = −0,650, scroll = +0,457, tempo = −0,328). Conclui que o modelo é suficiente para análise de sensibilidade mas não para previsão de alta precisão.

### Parte 3 — Análise de Sensibilidade

variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]. Tabela com índice −0,489 e +0,258. Gráfico de barras dos índices gerado. Interpretação cita "quase o dobro" de diferença em módulo e explica o sinal de cada variável com raciocínio de negócio. Print da tabela de sensibilidade incluso.

### Parte 4 — Decisão

Recomendação cita índice −0,489, estima que redução de 10% no abandono eleva conversão de 5,87% para ~6,16%. Menciona ações concretas (simplificar checkout, salvar carrinho entre sessões). Limitação aponta linearidade e interações entre variáveis — específicas ao modelo, não genéricas. Não distingue explicitamente associação de causalidade.

### Ao Além dos Aléns (bônus)

Presente. Código fornecido executado com 3 features. Estatísticas descritivas geradas (média 5,87%, std 0,39, P10 5,37%, P90 6,38%). Histograma plotado. Interpretação menciona pior cenário (4,65%) e melhor (7,19%), conclui que downside é limitado e conecta à recomendação. Não calcula probabilidades explícitas além dos percentis.

## Confiança

Confiança geral: Alta
```

---

## O que entregar

Um relatório estruturado com seções:

### 1. Problemas de calibração
Pares ou grupos de estudantes onde a diferença de nota não é sustentada pelas evidências descritas. Para cada caso: quem são, qual a diferença, e o que nas avaliações contradiz ou não justifica o gap.

### 2. Possíveis alucinações
Afirmações nas avaliações que parecem não se sustentar — números citados que divergem do esperado sem explicação, elogios a elementos que a rubrica não prevê como diferencial, ou penalizações por algo que provavelmente o estudante fez corretamente.

### 3. Inconsistências de critério
Situações em que o mesmo comportamento foi tratado de forma diferente entre estudantes. Liste o padrão observado e os estudantes afetados.

### 4. Lacunas graves não sinalizadas
Erros conceituais ou de método que aparecem nas evidências mas não foram mencionados no feedback — e que representam falhas de aprendizado reais, não erros de forma.

### 5. Veredito geral
Em 3 a 5 frases: a correção é confiável como está, ou há casos que precisam ser revistos antes de publicar as notas? Quais são os 2 ou 3 ajustes de maior impacto?

Seja direto. Omita o que for trivial. Cada achado deve ser acionável — deve levar a uma nota diferente ou a um feedback mais útil para o estudante.
