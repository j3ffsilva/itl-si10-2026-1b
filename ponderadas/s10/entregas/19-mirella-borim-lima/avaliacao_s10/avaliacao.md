# Avaliação - Mirella Borim Lima

Estudante: Mirella Borim Lima

Rubrica: `../../../rubrica_s10.md`

Nota: 8,0

Feedback:

Respondeu as quatro partes com valores concretos: correlações, MAE/RMSE e índices de sensibilidade citados. A Parte 3 tem variaveis_escolhidas preenchida, tabela gerada e índices com sinal e magnitude (−0,461 para abandono, +0,250 para scroll). A Parte 4 está com as células trocadas: a célula de limitação descreve uma ação de produto (simplificar checkout) e a célula de recomendação cita o índice sem apontar a direção da intervenção. A Parte 2 afirma que os erros são "relativamente baixos" sem comparar 0,317 ou 0,402 com a média da conversão (~5,87%), o que deixa a conclusão sem base quantitativa. O modelo foi treinado com 2 features em vez de 3, o que explica os índices da Parte 3 fora do intervalo de referência. O bônus foi executado com estatísticas descritivas (média 5,87%, P10 5,43%, P90 6,32%) e histograma, sem quantificar probabilidades de cenários (ex.: P(conversão < 5%)).

## Evidência

### Parte 1: Exploração

variavel_x = "taxa_abandono_carrinho_pct" e variavel_x2 = "profundidade_scroll_pct" preenchidas; scatter e heatmap gerados. Justificativa cita correlações concretas: −0,643 para abandono e +0,485 para scroll, com explicação do sinal de cada uma. Evidência numérica presente.

### Parte 2: Modelo

MAE = 0,317 e RMSE = 0,402 (modelo rodado apenas com 2 features em vez de 3, o que explica os valores levemente piores que o esperado). Interpretação reconhece erros "relativamente baixos" e diferença MAE vs. RMSE, mas não compara explicitamente à média da conversão (~5,87%) ou à amplitude da escala. falta âncora quantitativa.

### Parte 3: Análise de Sensibilidade

variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]. Tabela gerada com índice −0,461 (abandono) e +0,250 (scroll). valores ligeiramente diferentes do esperado por usar modelo com 2 features. Cita ambos os índices e conclui corretamente que o abandono tem maior impacto absoluto. Sinal e magnitude interpretados.

### Parte 4: Decisão

A célula de recomendação cita o índice de −0,461 e conclui que o abandono deve ser priorizado, mencionando queda de ~4,6% na conversão. A célula de "limitação" descreve uma ação de produto (checkout mais simples), invertendo as células. ausência de limitação analítica explícita (sem distinção de causalidade, sem limitação específica ao modelo ou aos dados).

### Ao Além dos Aléns (bônus)

Presente e executado. Código do Monte Carlo rodado, estatísticas descritivas geradas (média 5,87%, std 0,35, P10 5,43%, P90 6,32%), histograma plotado. Interpretação cita esses valores e conclui que o risco é baixo. Não vai além do código fornecido, mas a interpretação é satisfatória.

## Confiança

Confiança geral: Alta
Nota reduzida em relação à faixa 9,0 por: (1) modelo da Parte 2 e 3 usando apenas 2 features, gerando índices fora do intervalo de referência; (2) Parte 4 com células invertidas. limitação ausente e recomendação incompleta quanto à causalidade.
