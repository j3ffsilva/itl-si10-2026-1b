# Avaliação - Mariana de Paula Barbosa Souza

Estudante: Mariana de Paula Barbosa Souza

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Fez as quatro partes com valores numéricos do notebook. Na Parte 1, citou correlações (-0,643 e +0,485) e excluiu tempo (-0,229). Na Parte 2, contextualizou MAE (0,276) e RMSE (0,344) em relação à média da conversão (~5,87%) e observou que RMSE ≈ σ do ruído (0,35). Na Parte 3, citou os índices (-0,489 e +0,258) com interpretação de sinal e magnitude. Na Parte 4, estimou ganho de ~4,9% para redução de 10% no abandono, distinguiu associação de causalidade e nomeou fatores externos (sazonalidade, campanhas, preço). O bônus gerou P10 (5,369%) e P90 (6,379%) com leitura de risco conectada à recomendação. Não atinge 10,0 porque o bônus não calcula probabilidade de cenário adverso nem compara o ganho esperado com o desvio da simulação.
## Evidência

### Parte 1: Exploração

`variavel_x = "taxa_abandono_carrinho_pct"` preenchida; scatter gerado. Scatter secundário para scroll adicionado. Justificativa com valores numéricos: abandono r = -0,643 ("maior impacto na queda"), scroll r = +0,485 ("maior correlação positiva"). Excluiu tempo do primeiro clique por correlação fraca (-0,229). Evidência ancorada nos dados.

### Parte 2: Modelo

MAE = 0,276 e RMSE = 0,344 citados. Interpretação: "erro médio inferior a 5% da média" e "RMSE próximo ao MAE indica ausência de erros extremos". Acrescentou que o RMSE é próximo ao ruído do dataset (σ = 0,35), reconhecendo que o modelo atingiu o limite do que é recuperável. raciocínio avançado e específico.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida; `tabela_sensibilidade` gerada com output. Índices -0,489 e +0,258 citados. Análise comparativa: "abandono é quase o dobro do scroll". Saídas da tabela referenciadas (5,869 → 5,582 para abandono; → 6,020 para scroll). Interpretação de sinal e magnitude presente.

### Parte 4: Decisão

Recomendação concreta: simplificar checkout (menos etapas, frete transparente, login/convidado facilitado). Citou índice -0,489 e ganho de ~4,9% para redução de 10% no abandono. Limitação específica: "modelo linear ignora interações entre as variáveis e fatores externos como sazonalidade, campanhas e preço"; afirmou que "a sensibilidade mostra associação dentro do modelo, não causalidade garantida". distinção explícita e precisa.

### Ao Além dos Aléns (bônus)

Presente e executado. Monte Carlo com 1000 amostras, percentis exibidos (P10 = 5,369%, P90 = 6,379%). Interpretação: distribuição estreita com desvio padrão ~0,39; faixa P10–P90 de ~1 p.p.; robustez "alta". Não quantificou probabilidade de cenários adversos abaixo de um limiar nem comparou o ganho esperado (~0,29 p.p.) com o desvio da simulação.

## Confiança

Confiança geral: Alta
