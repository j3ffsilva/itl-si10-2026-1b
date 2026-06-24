# Avaliação - Ricardo de Toledo Planas

Estudante: Ricardo de Toledo Planas

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Respondeu as quatro partes com o maior nível de detalhe do conjunto. A Parte 1 acrescenta análise por quartis (conversão média de 6,41% no Q1 vs. 5,38% no Q4 do abandono) à correlação. A Parte 2 calcula R² (0,714), MAPE (4,77%), coeficientes padronizados e faz validação temporal com MAE no teste de 0,264. A Parte 3 inclui tornado chart das 3 variáveis com amplitudes, tabela de cenários isolados e combinados, e calcula que reduzir o abandono em 10% eleva a conversão de 5,87% para 6,16% (+0,287 p.p.). A Parte 4 distingue associação de causalidade em linguagem direta, propõe teste A/B e nomeia quatro limitações específicas: causalidade vs. correlação, linearidade, dados sintéticos e independência das variáveis. O bônus compara o cenário base com o cenário de abandono −10% usando n=10.000: P(< 5,5%) cai de 23,89% para 10,64%, P(> 6%) sobe de 39,96% para 61,82%, ganho mediano de 0,283 p.p. O erro residual do modelo foi incluído na simulação.

## Evidência

### Parte 1: Exploração

variavel_x = "taxa_abandono_carrinho_pct". Scatter com OLS, heatmap, scatter das 3 features lado a lado, análise por quartis (conversão média de 6,41% no Q1 vs. 5,38% no Q4 do abandono). Justificativa usa tabela markdown com correlações e r² individuais. Evidência numérica múltipla e coerente.

### Parte 2: Modelo

MAE = 0,276, RMSE = 0,344, R² = 0,714, MAPE = 4,77%. Coeficientes padronizados calculados (beta abandono = −0,650, scroll = +0,457, tempo = −0,328). Validação temporal treino/teste (MAE no teste = 0,264). Interpreta cada métrica em relação à escala da conversão e conclui que o modelo é adequado para comparação de sensibilidade.

### Parte 3: Análise de Sensibilidade

variaveis_escolhidas corretas. Tabela com índice −0,489 e +0,258. Tornado chart com 3 variáveis (amplitude: abandono ±0,574 p.p., scroll ±0,303 p.p., tempo ±0,131 p.p.). Tabela de cenários: redução isolada e combinada de 10% e 5%. Comparativo correlação × coeficiente × sensibilidade em tabela.

### Parte 4: Decisão

Recomendação cita índice −0,489, ganho de +0,287 p.p. (+4,89%), ações concretas (simplificar checkout, frete transparente, recuperação de carrinho). Limitação aponta 4 restrições específicas: (1) causalidade, (2) linearidade, (3) dados sintéticos, (4) independência das variáveis. Propõe validação por experimento controlado. Distinção associação/causalidade explícita.

### Ao Além dos Aléns (bônus)

Presente e exemplar. Monte Carlo com n=10.000 comparando base vs. recomendação. P(< 5,5%) cai de 23,89% para 10,64%; P(> 6%) sobe de 39,96% para 61,82%. Inclui erro residual do modelo na simulação. Histograma comparativo sobreposto. Ganho médio e mediano calculados (0,283 p.p.). Interpretação conecta risco à recomendação e menciona necessidade de teste A/B.

## Confiança

Confiança geral: Alta
