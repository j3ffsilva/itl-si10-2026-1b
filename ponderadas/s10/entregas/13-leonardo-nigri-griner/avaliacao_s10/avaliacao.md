# Avaliação - Leonardo Nigri Griner

Estudante: Leonardo Nigri Griner

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Respondeu as quatro partes com valores numéricos do notebook em cada uma. Na Parte 1, citou correlações (-0,643 e +0,485) para justificar a escolha das variáveis. Na Parte 2, interpretou MAE (0,276) e RMSE (0,344) em relação à escala da conversão. Na Parte 3, citou os índices (-0,489 e +0,258) com sinal e magnitude. Na Parte 4, ancorou a recomendação no índice -0,489 e nomeou fatores externos ao modelo. O bônus vai além do mínimo: Monte Carlo com 1000 amostras, P10 (5,38%) e P90 (6,35%) citados no texto, risco quantificado (17% de chance de conversão abaixo de 5,5%), ranking das três variáveis e cálculo de inversão de objetivo (redução de 4,14 p.p. no abandono para ganhar 0,25 p.p. de conversão). A nota 10 decorre de todas as partes preenchidas com números e das extensões analíticas não solicitadas.

## Evidência

### Parte 1: Exploração

`variavel_x = "profundidade_scroll_pct"` preenchida e scatter gerado. Tabela de correlação exibida com todos os valores. Justificativa explícita: abandonou o tempo do primeiro clique por correlação fraca (-0,229) e escolheu abandono (-0,643) e scroll (+0,485) por maior força de sinal. raciocínio ancorado nos números.

### Parte 2: Modelo

MAE = 0,276 e RMSE = 0,344 citados explicitamente. Interpretação relativa à escala da conversão presente ("erro médio ficou perto de 0,28 ponto percentual"). Observou que o RMSE > MAE indica erros assimétricos, e reconheceu que o erro é aceitável para decisão de produto.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas = ["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]` preenchida corretamente; `tabela_sensibilidade` gerada com output visível. Citou valores precisos da tabela: abandono de 5,869 → 5,582 (variação -4,891%, índice -0,489); scroll de 5,869 → 6,020 (+2,578%, índice +0,258). Interpretou sinal e magnitude comparativos.

### Parte 4: Decisão

Recomendação concreta de produto (simplificar checkout, reduzir etapas, clareza de frete) ancorada no índice -0,489 do abandono. Limitação específica e não genérica: modelo linear sobre dados simulados ignora fatores externos (promoções, preço, campanhas), coeficientes dependem da relação linear entre as variáveis, e a variação de 10% é local. Não declarou causalidade: "o número deve ser lido como estimativa de direção, não garantia."

### Ao Além dos Aléns (bônus)

Presente e completo. Simulação de Monte Carlo executada (1000 amostras), tabela de percentis exibida, histograma gerado. Interpretação com risco quantificado: 17% de chance de conversão < 5,5%, faixa P10–P90 de 5,38%–6,35%. Recomendou rollout gradual ou teste A/B dado o risco. Adicionou cálculo extra de inversão de objetivo (redução de 4,14 p.p. no abandono ≈ 8,71% relativo para ganhar 0,25 p.p. de conversão) e ranking completo das três variáveis.

## Confiança

Confiança geral: Alta
