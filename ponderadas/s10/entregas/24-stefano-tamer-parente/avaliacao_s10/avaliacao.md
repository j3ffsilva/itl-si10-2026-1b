# Avaliação - Stefano Tamer Parente

Estudante: Stefano Tamer Parente

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Respondeu as quatro partes com evidência numérica em todas elas. A Parte 1 imprime o ranking de correlações em módulo (abandono −0,643, scroll +0,485, tempo −0,229) e gera scatter com OLS. A Parte 2 compara MAE (0,276) e RMSE (0,344) à faixa de conversão (~4,7% da média) e calcula coeficientes do modelo. A Parte 3 cita os índices −0,489 e +0,258, exibe gráfico de barras e imprime tabela comparativa entre correlação, coeficiente e sensibilidade. A Parte 4 estima o ganho (5,87% → ~6,13% com redução de 10% no abandono) e tem seção explícita "Causalidade vs. correlação" que nomeia variável de confusão não observada e necessidade de validação com dados reais, com quatro limitações enumeradas. O bônus gera P10–P90 (5,37%–6,38%) e calcula P(conversão > base) = 48,5%, conectando a variância natural ao risco de sinal falso em intervenção de produto.

## Evidência

### Parte 1: Exploração

Correlação impressa com ranking por impacto absoluto (abandono −0,643, scroll +0,485, tempo −0,229). `variavel_x = "taxa_abandono_carrinho_pct"`, scatter com OLS gerado. Gráfico de barras de correlação e três scatters comparativos adicionais. Justificativa explica r² e cita os valores.

### Parte 2: Modelo

MAE = 0,276, RMSE = 0,344. Interpreta em relação à faixa de conversão (~4,7% da média). Calcula coeficientes do modelo (abandono −0,060, scroll +0,024, tempo −0,094). Conclui que o modelo é suficiente para análise de sensibilidade mas não para previsão de alta precisão.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`. Tabela gerada com índice −0,489 (abandono) e +0,258 (scroll). Gráfico de barras dos índices. Tabela comparativa entre correlação, coeficiente e sensibilidade impressa. Texto cita os índices corretos da tabela.

### Parte 4: Decisão

Recomendação cita índice −0,489, estima ganho de 10% de redução no abandono elevando conversão de 5,87% para ~6,13%. Limitações têm quatro itens explícitos: (1) seção "Causalidade vs. correlação" com menção a variável de confusão não observada e validação com dados reais; (2) linearidade assumida; (3) dados sintéticos; (4) independência das variáveis. A distinção associação/causalidade está presente e fundamentada.

### Ao Além dos Aléns (bônus)

Presente com cálculo de probabilidade. Estatísticas descritivas: média 5,869%, std 0,393, P10 5,369%, P90 6,379%. Histograma plotado. Cálculo explícito de `prob_acima_base = 48,5%`. Interpretação conecta variância natural ao risco de sinal falso em intervenção de produto.

## Confiança

Confiança geral: Alta
