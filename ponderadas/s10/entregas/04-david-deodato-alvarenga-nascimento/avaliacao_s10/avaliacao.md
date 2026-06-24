# Avaliação - David Deodato Alvarenga Nascimento

Estudante: David Deodato Alvarenga Nascimento

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Entregou as quatro partes com extensões em cada etapa. Na Parte 1, formalizou três hipóteses antes da exploração e confirmou os sinais esperados vs. observados em tabela. Na Parte 2, calculou coeficientes padronizados (abandono −0,650, scroll +0,457, tempo −0,328), gerou residual plot e histograma de resíduos, e comparou MAE com a média da variável alvo (~5,87%). Na Parte 3, gerou tabela para as três variáveis (incluindo tempo −0,112), análise bidirecional ±10%, tabela de metas (quanto mudar para +0,20 p.p. e +0,50 p.p.) e cenários combinados. A Parte 4 usa matriz de decisão com prioridade, ação, evidência, métrica de validação e risco para cada variável, e distingue causalidade explicitamente. O bônus usa 5000 simulações, reporta P5/P10/P25/P50/P75/P90/P95, e compara baseline vs. intervenção conservadora (abandono −5%, tempo −5%) com ganho médio de 0,176 p.p., P10 do ganho = 0,155 p.p. e probabilidade de ganho positivo = 100%.

## Evidência

### Parte 1: Exploração

Tabela de correlações + ranking por correlação absoluta + heatmap + scatter (abandono e scroll) + tabela de confirmação de hipóteses (H1, H2, H3 com sinal esperado vs. observado). Justificativa cita correlações corretas: abandono −0,643 e scroll +0,485, com tempo (−0,229) descartado explicitamente. Hipóteses formalizadas antes da exploração. abordagem metodologicamente madura.

### Parte 2: Modelo

MAE 0,276, RMSE 0,344, coeficientes exibidos. Calcula também coeficientes padronizados (abandono −0,650, scroll +0,457, tempo −0,328). Interpreta MAE em relação à média (~5,87%): "erro é baixo o suficiente para comparar cenários locais de sensibilidade." Residual plot e histograma de resíduos produzidos. RMSE um pouco acima do MAE justificado: "não há sinal forte de que poucos erros extremos estejam dominando."

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` = abandono + scroll. Tabela principal: índice −0,489 (abandono) e +0,258 (scroll). Além disso: ranking completo das três variáveis (incluindo tempo: −0,112), análise bidirecional (±10% para todas), tabela de metas de produto (quanto mudar para +0,20 p.p. e +0,50 p.p.), e cenários combinados. Todos os índices corretamente calculados e interpretados com sinal e magnitude.

### Parte 4: Decisão

Matriz de decisão formal com prioridade 1/2/3, ação, variável alvo, evidência, métrica de validação e risco para cada variável. Recomendação principal: reduzir abandono (índice −0,489, maior impacto). Limitação explícita: "o modelo estima uma relação local em uma base simulada, não um efeito causal observado em usuários reais". distingue causalidade e propõe teste controlado com métricas de validação definidas.

### Ao Além dos Aléns (bônus)

Presente e executado com rigor: 5000 simulações, estatísticas com P5/P10/P25/P50/P75/P90/P95, probabilidade de ficar abaixo da linha base (49,1%), histograma com marcadores de P10 e P90. Cenário de intervenção conservadora (abandono −5%, tempo −5%): ganho médio de 0,176 p.p., P10 do ganho = 0,155 p.p., prob. de ganho positivo = 100%, histograma sobreposto base vs. intervenção. Interpreta a distribuição com referência ao risco: "a recomendação não deve ser lida como ganho fixo" e define próximo passo (teste controlado).

## Confiança

Confiança geral: Alta
