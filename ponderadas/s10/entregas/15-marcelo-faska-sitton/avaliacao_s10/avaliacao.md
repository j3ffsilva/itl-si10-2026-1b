# Avaliação - Marcelo Faska Sitton

Estudante: Marcelo Faska Sitton

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Respondeu as quatro partes com os valores de referência do modelo com 3 features: MAE 0,276 e RMSE 0,344. Na Parte 2, observou que RMSE ≈ σ do ruído de geração (0,35) e concluiu que o modelo recuperou quase toda a estrutura disponível. Na Parte 3, gerou os índices -0,489 e +0,258 e os citou com interpretação de sinal e magnitude ("módulo do abandono é quase o dobro do scroll"). Na Parte 4, ancorou a recomendação no índice -0,489, nomeou variáveis omitidas (frete, prazo, pagamento) e distinguiu causalidade de correlação com argumento específico. O bônus cita P10 (5,37%) e P90 (6,38%) no texto, compara o ganho esperado (+0,29 pp) com o desvio da simulação (0,39 pp) e observa que o RMSE não está propagado na incerteza do Monte Carlo. Não atinge 10,0 porque o bônus não inclui cenário comparativo entre baseline e a recomendação aplicada.

## Evidência

### Parte 1: Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Scatter adicional para scroll. Ranking de correlações calculado (abandono −0,643, scroll +0,485, tempo −0,229). Justificativa cita os três valores e explica a exclusão do tempo por sinal mais fraco.

### Parte 2: Modelo

3 features (`features = [abandono, scroll, tempo]`). MAE = 0,276 / RMSE = 0,344. valores de referência. Interpretação compara MAE com média (4,7%) e desvio padrão dos dados. Insight sobre RMSE ≈ σ do ruído de geração (0,35): "o modelo recuperou quase toda a estrutura que dava para recuperar".

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`. Tabela gerada com índices −0,489 e +0,258. Texto cita valores exatos e interpreta sinal e magnitude: "o módulo de −0,489 é quase o dobro do de +0,258". Célula extra com ranking por magnitude.

### Parte 4: Decisão

Recomendação concreta (one-page checkout, compra como convidado) com citação do índice −0,489 e do ganho calculado (+4,89%). Distinção de causalidade específica: "a taxa de abandono é apenas o sintoma do problema", com variáveis omitidas nomeadas (frete, prazo, pagamento, confiança no site). Célula de código calculando o efeito estimado da meta.

### Ao Além dos Aléns (bônus)

Monte Carlo executado (1.000 amostras, 3 features). P10 = 5,369% e P90 = 6,379% citados no texto. Comparação ganho esperado (+0,29 pp) vs. desvio da simulação (0,39 pp). Observação extra sobre RMSE não propagado: "o P10 real é mais pessimista". Sem cenário comparativo (baseline vs. recomendação).

## Confiança

Confiança geral: Alta
Observação: a avaliação original e o agente de re-avaliação cometeram erro factual ao descrever o modelo com 2 features. O notebook usa explicitamente `features = [abandono, scroll, tempo]` na Parte 2, gerando MAE 0,276 e RMSE 0,344. valores de referência do modelo completo.
