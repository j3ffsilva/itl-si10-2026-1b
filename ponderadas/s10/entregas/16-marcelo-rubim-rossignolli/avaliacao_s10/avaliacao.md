# Avaliação - Marcelo Rubim Rossignolli

Estudante: Marcelo Rubim Rossignolli

Rubrica: `../../../rubrica_s10.md`

Nota: 8,5

Feedback:

O modelo foi ajustado com 2 features (`features_escolhidas = [abandono, scroll]`), excluindo `tempo_primeiro_clique_s` sem justificativa. Isso gerou MAE 0,317 e RMSE 0,402, superiores aos valores de referência com 3 features (0,276 e 0,344), e deslocou os índices de sensibilidade (−0,461 e +0,250 em vez de −0,489 e +0,258). A Parte 2 afirma que "a margem de erro se manteve baixa e segura" sem comparar com o modelo completo nem reconhecer que a feature foi omitida. As demais partes estão dentro do esperado: a Parte 1 cita correlações numericamente e usa múltiplos gráficos; a Parte 3 gera a tabela de sensibilidade e interpreta sinal e magnitude; a Parte 4 propõe recomendação concreta com o índice -0,461 citado, nomeia causas omitidas (frete, prazo, pagamento) e distingue causalidade de correlação; o bônus cita P10 (5,449%) e P90 (6,307%) e faz leitura qualitativa da distribuição. A nota 8,5 decorre da ausência de justificativa para excluir a terceira feature e da interpretação de erro sem base comparativa na Parte 2.

## Evidência

### Parte 1: Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Gráfico de barras de correlação (seaborn) + scatter adicional para scroll. Justificativa cita correlações numericamente (abandono −0,643, scroll +0,485) e explica exclusão do tempo por menor sinal.

### Parte 2: Modelo

Modelo ajustado com 2 features (`features_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`) sem justificativa para exclusão do tempo. MAE = 0,317 / RMSE = 0,402. superiores aos valores de referência do modelo com 3 features (0,276 / 0,344). Interpretação não compara com o modelo completo; afirma precisão sem base comparativa.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`. Tabela gerada com índices −0,461 e +0,250 (diferem dos de referência porque o modelo usa apenas 2 features). Análise internamente consistente: "magnitude do impacto do abandono supera consideravelmente o engajamento por scroll", com variações percentuais da tabela citadas.

### Parte 4: Decisão

Recomendação concreta (one-page checkout, compra como convidado) com citação do índice −0,461 e das variações calculadas. Distinção causas omitidas: "o número de abandono de carrinho é apenas o sintoma do problema", com fatores nomeados (frete, prazo, pagamento). Boa limitação com argumento específico.

### Ao Além dos Aléns (bônus)

Monte Carlo executado (1.000 amostras, 2 features). P10 = 5,449% e P90 = 6,307% no output; o texto cita "entre 5.44% e 6.30%", bom alinhamento. Interpretação qualitativa sólida: estabilidade da distribuição e implicação para a recomendação. Sem cálculo de probabilidade de cenário adverso.

## Confiança

Confiança geral: Alta
Observação: a avaliação original e o agente de re-avaliação descreveram incorretamente o notebook como usando 3 features com MAE 0,276/RMSE 0,344. O notebook usa explicitamente `features_escolhidas` com 2 variáveis na Parte 2, gerando MAE 0,317 e RMSE 0,402.
