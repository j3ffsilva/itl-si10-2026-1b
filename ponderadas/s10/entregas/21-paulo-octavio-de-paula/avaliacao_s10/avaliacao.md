# Avaliação - Paulo Octavio de Paula

Estudante: Paulo Octavio de Paula

Rubrica: `../../../rubrica_s10.md`

Nota: 8,0

Feedback:

Fez as quatro partes e o bônus. Na Parte 1, citou correlações (-0,643 e +0,485) e excluiu tempo por correlação menor (-0,229). Na Parte 3, citou os índices -0,489 e +0,258 com interpretação de sinal e magnitude. O bônus cita P10 (5,37%) e P90 (6,38%) no texto e conecta ao risco. Dois pontos limitam a nota: na Parte 2, o texto diz que os erros são "relativamente baixos" sem comparar MAE (0,276) com a escala da conversão (~5,87%); na Parte 4, a recomendação não cita o valor do índice (-0,489), apenas "maior índice de sensibilidade em valor absoluto", e não distingue associação de causalidade de forma explícita.
## Evidência

### Parte 1: Exploração

variavel_x = "taxa_abandono_carrinho_pct" preenchida, scatter gerado. Justificativa cita correlações −0,643 e +0,485, menciona o terceiro valor (−0,229) como critério de exclusão. Evidência numérica presente, raciocínio claro.

### Parte 2: Modelo

MAE = 0,276 e RMSE = 0,344 exibidos. Interpretação menciona que MAE indica margem de erro de 0,28 p.p. e que RMSE penaliza erros maiores, e conclui que o modelo é "adequado". Falta comparar 0,276 com a média da taxa de conversão (5,87%) ou com a amplitude da escala para quantificar a adequação.

### Parte 3: Análise de Sensibilidade

variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]. Tabela gerada com índice −0,489 e +0,258. Interpretação cita os dois valores em módulo, conclui que o abandono tem maior impacto e recomenda prioridade. Sinal e direção corretos.

### Parte 4: Decisão

Recomendação cita índice de sensibilidade e aponta ações (simplificar checkout, reduzir etapas). Limitação menciona fatores externos não capturados e que a análise assume ceteris paribus. válido, mas genérico; não aponta limitação específica ao modelo linear ou ao processo gerador dos dados.

### Ao Além dos Aléns (bônus)

Presente. Código do Monte Carlo executado com 3 features. Estatísticas descritivas geradas (média 5,87%, std 0,39, P10–P90: 5,37%–6,38%). Interpretação menciona formato próximo ao normal e conclui que há "baixo risco", mas sem quantificar probabilidades concretas (e.g., P(conversão < 5%) ou P(> 6%)). Satisfatório mas superficial.

## Confiança

Confiança geral: Alta
