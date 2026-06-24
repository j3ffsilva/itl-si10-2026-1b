# Avaliação - Matheus Fernandes Guimaraes de Sousa

Estudante: Matheus Fernandes Guimaraes de Sousa

Rubrica: `../../../rubrica_s10.md`

Nota: 8,0

Feedback:

Respondeu as quatro partes com valores numéricos. Na Parte 1, citou correlações (-0,643 e +0,485) e justificou a exclusão do tempo por correlação fraca (-0,229); adicionou heatmap e tabela de conversão por quartil (Q1 = 6,41%, Q4 = 5,38%), além do scatter mínimo. Na Parte 2, contextualizou MAE (0,276) em relação à média (~5%) e distinguiu MAE de RMSE. Na Parte 3, citou os índices (-0,489 e +0,258) e comparou as variações da tabela (5,87% → 5,58% para abandono; → 6,02% para scroll). Na Parte 4, ancorou a recomendação no índice -0,489 com ganho estimado de ~4,9% e distinguiu correlação de causalidade. O bônus executou o Monte Carlo com a tabela de percentis gerada (P10 = 5,369%, P90 = 6,379%), mas a interpretação textual não citou esses valores e não conectou a dispersão ao ganho esperado da recomendação. A nota 8,0 decorre da interpretação do bônus sem uso dos percentis gerados pelo próprio código e das respostas da Parte 3 sem aprofundamento além dos valores mínimos.

## Evidência

### Parte 1: Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Também adicionou matriz de correlação visual (heatmap) e tabela de conversão média por quartil do abandono (Q1 = 6,41%, Q4 = 5,38%). esforço exploratório acima do mínimo. Justificativa com correlações citadas: abandono r = -0,643, scroll r = +0,485, tempo r = -0,229 (excluído por correlação fraca). Concisa mas ancorada em evidências.

### Parte 2: Modelo

MAE = 0,276 e RMSE = 0,344 citados. Interpretação: "erra só 0,28 ponto em média (MAE), menos de 5% disso". relação percentual com a média presente. Distinguiu que RMSE próximo ao MAE indica ausência de erros grandes. Resposta correta mas a mais curta do lote na Parte 2.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida; `tabela_sensibilidade` gerada com output correto. Índices -0,489 e +0,258 mencionados na resposta. Comparação: "abandono é quase o dobro do scroll". Valores da tabela citados numericamente (5,87% → 5,58% para abandono; → 6,02% para scroll). Análise correta e suficiente, sem aprofundamento adicional.

### Parte 4: Decisão

Recomendação: focar em reduzir abandono, simplificar checkout, mostrar frete mais cedo. Citou índice -0,489 e ganho de ~4,9% para redução de 10% no abandono. Limitação mencionada explicitamente: "correlação não prova causa" e "modelo linear ignora interações entre as variáveis". Distinguiu associação de causalidade de forma direta e concisa.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras, tabela de percentis gerada com output (P10 = 5,369%, P90 = 6,379%). Interpretação superficial: "fica quase toda entre 5,4% e 6,4%, com mediana ~5,85%. A distribuição é estreita, então a recomendação é segura." Não citou os percentis numericamente da tabela, não quantificou probabilidade de risco abaixo de limiar, e não conectou a dispersão ao ganho esperado da recomendação.

## Confiança

Confiança geral: Alta
Observação: o notebook está completo e os outputs são consistentes. A avaliação reflete a profundidade analítica das respostas textuais, não eventuais dificuldades de execução.
