# Avaliação - Moyses Birman Anijar

Estudante: Moyses Birman Anijar

Rubrica: `../../../rubrica_s10.md`

Nota: 9,0

Feedback:

Respondeu as quatro partes com ancoragem numérica em todas elas. A Parte 1 justifica a escolha das variáveis com ranking de correlações em módulo, gráfico de barras e scatter com OLS. A Parte 2 relaciona MAE (0,276) e RMSE (0,344) à média da conversão (5,87%), calcula R² (0,714) e razão MAE/média (4,7%). A Parte 3 cita os índices −0,489 e +0,258 com sinal, compara as magnitudes (razão de ~1,9×) e calcula o ganho absoluto de uma redução de 10% no abandono (5,87% → 6,16%). A Parte 4 aponta ações concretas e nomeia duas restrições ao modelo: hipótese de linearidade e análise ceteris paribus (sem interações entre variáveis). A distinção entre associação e causalidade não aparece em linguagem direta, só de forma implícita. O bônus do Monte Carlo usa as 3 features, gera P10 (5,37%), P90 (6,38%), P(conversão < 5%) = 1% e P(< 5,5%) = 17,5%, e conecta o risco à recomendação.

## Evidência

### Parte 1: Exploração

variavel_x = "taxa_abandono_carrinho_pct", scatter com OLS gerado. Justificativa cita r = −0,643, +0,485 e −0,229, com gráfico de barras das correlações em módulo. Escolha justificada com evidência numérica e raciocínio sobre sinal.

### Parte 2: Modelo

MAE = 0,276, RMSE = 0,344 (modelo com 3 features, valores dentro do intervalo de referência). Interpreta em relação à média (4,7% do valor médio), calcula R² = 0,714 e razão RMSE/desvio = 0,534. Conclui que o modelo é suficiente para análise de sensibilidade, não para previsão de precisão.

### Parte 3: Análise de Sensibilidade

variaveis_escolhidas corretas. Tabela mostra índice −0,489 (abandono) e +0,258 (scroll). Cita ambos com sinal, compara em módulo (0,489 vs. 0,258, diferença de ~1,9×), interpreta a direção de cada um e calcula explicitamente o ganho absoluto (conversão 5,87% → 6,16% com redução de 10% no abandono).

### Parte 4: Decisão

Recomendação de reduzir abandono citando índice −0,489 e ganho de +0,287 p.p. (+4,89%). Limitações específicas: (1) linearidade pode não valer (saturação); (2) análise ceteris paribus ignora interações entre variáveis. Não usa a palavra "causalidade" explicitamente, mas a limitação de confundimento está presente de forma implícita.

### Ao Além dos Aléns (bônus)

Presente e bem executado. Monte Carlo com 3 features, estatísticas descritivas completas, cálculo de P(conversão < 5,0%) = 1%, P(< 5,5%) = 17,5%, intervalo P10–P90. Interpretação integra o risco à recomendação e menciona que o downside simulado é limitado.

## Confiança

Confiança geral: Alta
