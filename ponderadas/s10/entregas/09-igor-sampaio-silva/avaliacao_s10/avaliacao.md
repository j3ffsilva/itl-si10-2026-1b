# Avaliação - Igor Sampaio Silva

Estudante: Igor Sampaio Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Respondeu as quatro partes e executou o bônus com interpretação. Na Parte 1, escolheu corretamente `taxa_abandono_carrinho_pct` e `profundidade_scroll_pct`, citando as correlações do próprio notebook: abandono com r = -0,643 e scroll com r = +0,485, que são as duas relações mais fortes com a conversão. A Parte 2 reporta MAE = 0,317 e RMSE = 0,402 e contextualiza o erro em relação à média da conversão (~5,87%), embora pudesse comparar mais explicitamente com a amplitude da variável alvo ou com um modelo de referência. A Parte 3 gera a tabela de sensibilidade com índices -0,461 para abandono e +0,250 para scroll, interpretando corretamente sinal, magnitude e maior impacto absoluto do abandono. A Parte 4 recomenda reduzir abandono no checkout com números da tabela, propõe ações concretas e menciona a limitação central de associação vs. causalidade. O bônus executa Monte Carlo com 1000 simulações, cita média, mediana e P10-P90 (5,423% a 6,285%) e conecta a distribuição ao risco da recomendação. A nota fica em 9,0 porque a entrega está consistente e numericamente ancorada; não vai além disso por manter uma leitura ainda moderada do erro/modelo e por não incluir cenário comparativo ou probabilidade de risco no bônus.

## Evidência

### Parte 1: Exploração

Matriz de correlação gerada para as variáveis numéricas e dois scatters criados: `taxa_abandono_carrinho_pct` vs. conversão e `profundidade_scroll_pct` vs. conversão. A resposta escolhe abandono e scroll, citando r = -0,643 para abandono e r = +0,485 para scroll. A escolha é coerente com os dados e não descarta scroll em favor de tempo de clique.

### Parte 2: Modelo

Modelo ajustado com as duas variáveis escolhidas (`taxa_abandono_carrinho_pct` e `profundidade_scroll_pct`). Métricas geradas: MAE = 0,317 e RMSE = 0,402. A resposta explica MAE/RMSE, cita ambos os valores e compara o erro médio com a conversão média (~5,87%). A contextualização é adequada, mas poderia ser mais forte se comparasse com a amplitude da variável alvo ou discutisse explicitamente a perda por não incluir `tempo_primeiro_clique_s`.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`. Tabela gerada com saída base 5,869; aumento de 10% no abandono leva a saída 5,598, variação -4,612% e índice -0,461; aumento de 10% no scroll leva a saída 6,015, variação +2,499% e índice +0,250. A resposta compara os índices em módulo e conclui corretamente que abandono tem maior impacto.

### Parte 4: Decisão

Recomenda reduzir `taxa_abandono_carrinho_pct`, citando os valores da tabela (-0,461 para abandono e +0,250 para scroll). Propõe ações concretas no checkout: simplificar etapas, esclarecer frete/taxas e tornar o processo de compra mais rápido. A limitação menciona modelo simplificado com duas variáveis, linearidade, fatores externos (preço, promoções, perfil, sazonalidade e experiência geral) e explicita que os resultados indicam associação, não prova causal.

### Ao Além dos Aléns (bônus)

Monte Carlo executado com 1000 simulações e histograma. Estatísticas geradas: média 5,855%, mediana 5,856%, P10 = 5,423%, P90 = 6,285%, mínimo 4,879% e máximo 6,956%. A interpretação cita média, mediana e faixa P10-P90, e conecta a existência de cenários mais baixos à necessidade de acompanhar e validar a mudança na prática.

## Confiança

Confiança geral: Alta
Observação: a avaliação anterior atribuía ao notebook uma escolha por `tempo_primeiro_clique_s` e MAE = 0,348, mas esses pontos não correspondem à entrega do Igor. O notebook usa abandono + scroll e reporta MAE = 0,317.
