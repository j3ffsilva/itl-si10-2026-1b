# Avaliação - Leonardo Souza Martins

Estudante: Leonardo Souza Martins

Rubrica: `../../../rubrica_s10.md`

Nota: 8,5

Feedback:

Na Parte 2, identificou o ruído injetado (σ = 0,35) e comparou com o RMSE (0,344), concluindo que o modelo atingiu o limite teórico. O raciocínio sobre β bruto vs. índice de sensibilidade por escala é analiticamente válido. O problema central está na Parte 1 e na Parte 3: `taxa_abandono_carrinho_pct` foi excluída da análise de sensibilidade, apesar de ter correlação maior em módulo (−0,643) do que scroll (+0,485). A justificativa de que scroll "explica mais variância total" contradiz os próprios números da tabela de correlações que Leonardo gerou. A variável de maior impacto ficou fora do núcleo da análise sem base nos dados apresentados. A Parte 4 cita índice +0,258 e ganho de +2,578%, distingue causalidade de correlação com argumento específico (causalidade reversa, risco de linearidade, necessidade de teste A/B) e propõe ações concretas. O Monte Carlo gerou percentis P10 = 5,369% e P90 = 6,379% com leitura de risco conectada ao ganho esperado do scroll. A nota 8,5 reflete o raciocínio analítico acima da média nas Partes 2 e 4, descontado pela exclusão injustificada da variável dominante da análise de sensibilidade.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com lista `["profundidade_scroll_pct", "tempo_primeiro_clique_s"]`. gerou scatters para essas duas variáveis, não para abandono. Correlações impressas corretamente (abandono −0,643, scroll +0,485, tempo −0,229). Justificativa compara β bruto (tempo −0,085 > scroll +0,026 por unidade) com amplitude de variação das variáveis, argumentando que scroll explica mais variância total. mas a correlação do abandono (0,643) é superior à do scroll (0,485), contradizendo a premissa. O abandono não foi plotado nem discutido como candidato.

### Parte 2: Modelo

MAE = 0,276, RMSE = 0,344. Identificou o ruído injetado (σ = 0,35) e comparou com RMSE (0,344), concluindo que o modelo atingiu "virtualmente o limite teórico". Contextualizou erro relativo (~5% da média). Distinção MAE/RMSE explicada corretamente. Análise acima do mínimo.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["profundidade_scroll_pct", "tempo_primeiro_clique_s"]`. Tabela gerada corretamente para as variáveis escolhidas: scroll +0,258, tempo −0,112. Análise comparativa detalhada. `taxa_abandono_carrinho_pct` (índice −0,489 em módulo) ausente da análise.

### Parte 4: Decisão

Recomendação: priorizar scroll com ações concretas (sticky CTAs, barras de progresso, conteúdo above-the-fold). Cita índice +0,258 e ganho de +2,578% para 10% de melhora no scroll. Distinção explícita e bem fundamentada de causalidade vs. correlação: "usuário que já tem intenção de compra naturalmente rola mais". aponta risco de causalidade reversa. Limitação específica: linearidade, retornos decrescentes, necessidade de teste A/B. Qualidade da parte 4 é alta.

### Ao Além dos Aléns (bônus)

Presente e executado. 1000 amostras, percentis P10 = 5,369%, P90 = 6,379%. Interpretação conecta o ganho esperado do scroll (~0,15 p.p.) com o desvio padrão da simulação (~0,39), concluindo que o sinal pode ser "engolido" pela flutuação natural sem teste A/B. Raciocínio de risco correto.

## Confiança

Confiança geral: Alta

Observação: a nota 8,5 (e não 8,0 como Igor/Kaio) reflete que o raciocínio de Leonardo é substancialmente mais sofisticado. a distinção β bruto vs. índice é analiticamente válida, e a Parte 4 tem a melhor qualidade de análise de risco/causalidade entre os casos revisados. A penalização vem da falha factual na premissa de exclusão do abandono (a afirmação de que scroll tem maior correlação está errada nos dados) e da ausência da variável de maior impacto no núcleo da análise.
