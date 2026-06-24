# Avaliação - Isabelly Maia Montalvão

Estudante: Isabelly Maia Montalvão

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Respondeu as quatro partes com citação de números em todas as seções, distinção explícita entre associação e causalidade e proposta de teste A/B. O bônus inclui Monte Carlo com dois cenários sobrepostos (atual vs. abandono −10%) e quantifica a probabilidade de cair abaixo de 5% (1,4% → 0,1%). Além disso, entregou um segundo notebook separado (`experimento_sobol_bootstrap.ipynb`) com índices de Sobol (S1 e ST), bootstrap de 400 iterações com IC 95%, modelo com interações (ganho de R² = 0,0024, confirmando que interações são desprezíveis) e tabela consolidada de quatro métricas de importância. Esse segundo notebook aplica sensibilidade global em vez de local (OAT), distingue os dois métodos e confirma o ranking sem sobreposição dos intervalos. A nota é 10,0 porque o trabalho cobre todos os critérios da rubrica com números próprios e vai além com análise estatisticamente fundamentada.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Mapa de calor de correlações gerado, histogramas das variáveis de entrada e scatter de cada variável vs. conversão. Justificativa com correlações: −0,643 (abandono), +0,485 (scroll), −0,229 (tempo de clique). Argumento explícito de que as relações parecem lineares nos scatters, justificando regressão linear.

### Parte 2: Modelo

MAE (0,276) e RMSE (0,344) citados. R² = 0,714 calculado e reportado. Coeficientes padronizados calculados (abandono −0,652, scroll +0,458, tempo −0,329). MAE representando 4,70% da média da conversão. Análise de resíduos (scatter e histograma) e checagem de generalização treino/teste (MAE teste = 0,249). Interpretação completa e coerente.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida (abandono e scroll). Tabela gerada: abandono −0,489, scroll +0,258. Ranking completo das três variáveis calculado adicionalmente (tempo −0,112). Tornado diagram gerado com variação de ±10% em pontos percentuais absolutos (abandono ±0,287 p.p., scroll ±0,151 p.p., tempo ±0,066 p.p.). Tabela de robustez confirmando que os índices são idênticos para variações de 5%, 10% e 20%. Argumento: abandono tem ≈ 1,90× o impacto do scroll.

### Parte 4: Decisão

Recomenda experimento de interface para reduzir abandono, medindo efeito causal por teste A/B (distinção associação/causalidade explícita). Cita índice −0,489 e traduz em valor de negócio (≈ 28,7 vendas extras/dia, ≈ R$ 129 mil/mês) com suposições explícitas. Limitações específicas: linearidade, OAT ignora covariância, base simulada de 180 dias sem sazonalidade, suposições de volume e ticket médio como ordem de grandeza.

### Ao Além dos Aléns (bônus)

Presente e substancialmente expandido. Monte Carlo com dois cenários sobrepostos (referência vs. abandono −10%), com ganho médio de 0,286 p.p. e probabilidade de ficar abaixo de 5% caindo de 1,4% para 0,1%. Segundo notebook separado com índices de Sobol (S1 abandono ≈ 0,67, scroll ≈ 0,22, tempo ≈ 0,13), bootstrap de 400 iterações com IC 95% confirmando ranking sem sobreposição, modelo com interações (ganho de R² = 0,0024. desprezível), e tabela consolidada de quatro métricas de importância.

## Confiança

Confiança geral: Alta
Observação: o segundo notebook (`experimento_sobol_bootstrap.ipynb`) é trabalho adicional relevante que vai além de qualquer critério de bônus da atividade. Constitui análise de sensibilidade global completa e estatisticamente fundamentada.
