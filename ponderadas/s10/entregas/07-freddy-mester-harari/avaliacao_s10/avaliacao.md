# Avaliação - Freddy Mester Harari

Estudante: Freddy Mester Harari

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Respondeu as quatro partes com citação de números do notebook em cada seção. Na Parte 3, calculou os índices das três variáveis (não apenas as duas pedidas) e explicou por que o coeficiente bruto do tempo de clique é maior em magnitude absoluta mas seu índice de sensibilidade é o menor: a escala da variável é pequena, então 10% dela move pouco a conversão. O bônus tem Monte Carlo com P10/P90 citados e menção de que o ganho esperado (≈ 0,29 p.p.) é da mesma ordem do desvio padrão diário. A nota fica em 9,5 porque o bônus não quantifica o risco de a intervenção não surtir efeito, ficando na observação descritiva dos percentis sem traduzir a comparação ganho/desvio em probabilidade.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com uma lista de duas variáveis (`["taxa_abandono_carrinho_pct", "profundidade_scroll_pct"]`) e scatter gerado em loop para ambas. Justificativa com números: cita correlações r = −0,64 e r = +0,48 da matriz, contrasta com r = −0,23 do tempo de clique e usa o scatter como evidência visual adicional.

### Parte 2: Modelo

MAE (0,276) e RMSE (0,344) citados corretamente. Interpreta o MAE como "menos de 5% do valor típico" em relação à média da conversão e menciona que RMSE ligeiramente acima do MAE indica alguns dias com erro maior, sem outlier grave. Avalia o erro como aceitável para decisão de produto.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida. Tabela gerada com índices −0,489 (abandono) e +0,258 (scroll). Calcula também o índice do tempo de clique (−0,112) para comparação, e explica explicitamente por que o coeficiente bruto do tempo é maior que o do abandono mas seu índice é o menor: a escala da variável é pequena, então 10% dela move pouco a conversão. Raciocínio analítico claro.

### Parte 4: Decisão

Recomenda priorizar redução do abandono, cita índice −0,49 e a variação de 47,5% para 42,8% como exemplo concreto. Propõe ações testáveis (fluxo de checkout, salvamento de carrinho). Discute scroll como alavanca secundária. Limitação relevante: hipótese de linearidade e limitação da análise OAT (perturba uma variável por vez enquanto na realidade as variáveis covariam). Não usa a palavra "causalidade" explicitamente, mas reconhece implicitamente a limitação associativa.

### Ao Além dos Aléns (bônus)

Presente e executado. Simulação de 1000 amostras com outputs corretos (média 5,869%, std 0,393, P10 = 5,37%, P90 = 6,38%). Interpreta distribuição em termos de estabilidade e cita que o ganho esperado (0,29 p.p.) é da mesma ordem do desvio padrão diário, conectando corretamente à necessidade de teste com usuários reais.

## Confiança

Confiança geral: Alta
