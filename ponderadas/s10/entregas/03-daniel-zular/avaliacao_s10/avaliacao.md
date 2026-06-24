# Avaliação - Daniel Zular

Estudante: Daniel Zular

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Fez as quatro partes com citação de números do notebook em cada seção. Na Parte 1, citou correlações corretas (abandono -0,643, scroll +0,485, tempo -0,229) e descartou tempo com justificativa numérica. Na Parte 2, comparou MAE com a escala do alvo. Na Parte 3, citou os índices -0,489 e +0,258 com gráfico de barras. Na Parte 4, propõe A/B test e distingue associação de causalidade no texto. O bônus tem dois cenários Monte Carlo (atual vs. abandono 10% menor), ganho médio de 0,288 p.p., P10 e P90 comparados lado a lado (5,339%→5,665% e 6,338%→6,598%) e boxplot comparativo. A nota 10,0 decorre de todas as partes com números e do bônus com dois cenários e ganho quantificado.
## Evidência

### Parte 1: Exploração

Tabela de correlação exibida, `variavel_x = "taxa_abandono_carrinho_pct"`, scatter com trendline OLS. Justificativa cita correlações corretas: abandono −0,643, scroll +0,485, tempo −0,229 descartado explicitamente. Exploração numericamente fundamentada, mas restrita a um único gráfico.

### Parte 2: Modelo

MAE 0,276, RMSE 0,344. Interpretação compara MAE com escala do alvo ("entre 4% e 8%"), conclui que o erro é "relativamente baixo". RMSE penaliza erros maiores. âncora numérica presente e correta.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela gerada com valores corretos: índice −0,489 (abandono) e +0,258 (scroll). Texto cita os valores exatos da tabela, explica sinal e magnitude, conclui pela prioridade do abandono. Gráfico de barras dos índices gerado.

### Parte 4: Decisão

Recomendação: reduzir abandono do carrinho, cita índice −0,489 vs. +0,258, propõe ações específicas (fluxo de finalização, frete mais claro, reduzir etapas). Limitação aponta dados simulados e modelo linear, propõe A/B test. Distinção explícita de associação vs. causalidade presente no texto.

### Ao Além dos Aléns (bônus)

Dois cenários comparativos com rng_sim separado (seed 2026). Cenário atual: média 5,848%, P10 5,339%, P90 6,338%. Cenário melhoria (abandono 10% menor): média 6,136%, P10 5,665%, P90 6,598%, ganho médio 0,288 p.p. Boxplot lado a lado gerado. Texto interpreta os percentis e o ganho médio, conectando à recomendação. Monte Carlo comparativo mais completo do lote revisado.

## Confiança

Confiança geral: Alta
