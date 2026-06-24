# Avaliação - Pedro El Haouli Faria

Estudante: Pedro El Haouli Faria

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Fez as quatro partes com bônus. A Parte 1 inclui scatter das 3 variáveis, heatmap e tornado chart. A Parte 2 usa 3 features (MAE 0,276, RMSE 0,344) e acrescenta coeficientes padronizados (beta: abandono -0,650, scroll +0,457, tempo -0,328). A Parte 3 cita os índices -0,489 e +0,258 e o tornado chart exibe as 3 variáveis. A Parte 4 quantifica o ganho (5,87% → ~6,16%, +4,9%) e aponta limitações de linearidade, interações e natureza sintética dos dados. O bônus define zonas de risco (P(conversão < 5,5%) = 17,5%, P(> 6,3%) = 13,8%) e calcula contribuição de variância por variável (abandono 64,2%, scroll 26,9%, tempo 10,0%). A nota 10,0 decorre das quatro partes com números e do bônus com risco quantificado por probabilidades de cenário.
## Evidência

### Parte 1: Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida. Três scatter plots com linhas de tendência manuais, heatmap de correlação e ranking impresso no console (−0,643; +0,485; −0,229). Justificativa com r de abandono e scroll vs. tempo, comparação visual mencionada. Exploração substancialmente acima do mínimo.

### Parte 2: Modelo

3 features (`features = [abandono, scroll, tempo]`). MAE = 0,276, RMSE = 0,344 (valores de referência). Interpretação compara MAE com amplitude dos dados (~3,4 p.p.) e nota que RMSE próximo ao MAE indica ausência de erros extremos. Célula adicional com coeficientes padronizados (beta): −0,650 (abandono), +0,457 (scroll), −0,328 (tempo). Não faz validação temporal nem calcula MAPE.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`. Tabela com índices −0,489 e +0,258. Tornado chart adicional com as 3 variáveis e amplitudes (abandono ±0,574; scroll ±0,303; tempo ±0,131). Resposta compara magnitudes e sinais com clareza.

### Parte 4: Decisão

Recomendação cita índice −0,489 e quantifica ganho (5,87% → ~6,16%, +4,9%). Ações concretas: simplificar checkout, salvar carrinho entre sessões. Limitação aponta hipótese de linearidade, possíveis interações entre variáveis e natureza simulada dos dados. Célula de código que simula o efeito passo a passo (redução de 0% a 30%).

### Ao Além dos Aléns (bônus)

Presente e com análise de risco quantificada. Monte Carlo com n=1.000 amostras e percentis P10=5,369%, P90=6,379%. Zonas de risco definidas: P(conversão < 5,5%) = 17,5%, P(conversão > 6,3%) = 13,8%. Histograma com zonas coloridas. Análise de contribuição de variância por variável (abandono 64,2%, scroll 26,9%, tempo 10,0%). Não implementa cenário comparativo (baseline vs. abandono reduzido) nem inclui erro residual do modelo na simulação.

## Confiança

Confiança geral: Alta
