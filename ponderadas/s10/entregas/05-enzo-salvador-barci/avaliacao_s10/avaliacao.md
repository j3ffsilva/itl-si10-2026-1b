# Avaliação - Enzo Salvador Barci

Estudante: Enzo Salvador Barci

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Fez as quatro partes. Na Parte 1, citou as correlações -0,643 e +0,485. Na Parte 3, detalhou os valores de entrada e saída: abandono de 47,546 para 52,300 (queda de 4,891%) e scroll de 62,449 para 68,694 (alta de 2,578%). A Parte 4 cita o índice -0,489, propõe ações concretas e A/B test. O bônus cita P10 5,37%, P25 5,62%, mediana 5,85%, P75 6,13% e P90 6,38% no texto. Não atinge 9,5 por três motivos: a Parte 2 diz que o MAE "não parece tão alto" sem comparar com a escala da variável alvo (~5,87%); a Parte 1 tem um único scatter; o bônus não implementa cenário comparativo nem calcula ganho médio simulado.
## Evidência

### Parte 1: Exploração

Tabela de correlação exibida. `variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Scatter sem trendline gerado. Justificativa cita correlações corretas (−0,643 para abandono, +0,485 para scroll, −0,229 para tempo descartado). Texto bem estruturado mas com única visualização.

### Parte 2: Modelo

MAE 0,276, RMSE 0,344 obtidos. Interpretação diz que o erro é "relativamente baixo" e que RMSE "um pouco maior" considera erros maiores, mas não quantifica o erro em relação à escala (~5,87% de média da variável alvo). A interpretação é razoável mas falta a âncora numérica explícita pedida pela rubrica.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela gerada com valores corretos: índice −0,489 (abandono) e +0,258 (scroll). Resposta cita os valores numéricos da tabela com precisão (valor original, valor alterado, variação da saída e índice para ambas as variáveis). Sinal interpretado corretamente: "abandono aumenta → conversão cai, coerente com apps de compras."

### Parte 4: Decisão

Recomendação: melhorias no carrinho e checkout, com citação do índice −0,489 vs. +0,258. Ações específicas: clareza de frete, redução de etapas, mensagens de erro, facilitar pagamento. Limitação aponta modelo linear e dados simulados, propõe A/B test. distingue associação de causalidade.

### Ao Além dos Aléns (bônus)

Presente: 1000 simulações, descrição com percentis (P10 5,37%, P25 5,62%, P50 5,85%, P75 6,13%, P90 6,38%), histograma gerado. Interpretação cita os valores dos percentis e conclui que a distribuição é concentrada, o risco da recomendação é "baixo a moderado." Não há cenário de intervenção comparativo, o que limitaria a profundidade da análise de risco.

## Confiança

Confiança geral: Alta
