# Avaliação - Isadora Tribst Gatto

Estudante: Isadora Tribst Gatto

Rubrica: `../../../rubrica_s10.md`

Nota: 10,0

Feedback:

Respondeu as quatro partes com números derivados do notebook em cada seção. A Parte 1 usa mapa de calor, histogramas facetados e scatters para justificar a escolha de variáveis e a hipótese de linearidade. O modelo reporta R² (0,714), coeficientes padronizados, análise de resíduos e divisão treino/teste (MAE teste = 0,249). A Parte 3 tem tornado diagram, ranking completo das três variáveis e tabela de robustez com índices idênticos para variações de 5%, 10% e 20%. A Parte 4 distingue associação de causalidade, propõe teste A/B e traduz o ganho em valor de negócio (≈ R$ 129 mil/mês) com suposições declaradas. O bônus compara dois cenários Monte Carlo e quantifica a probabilidade de cair abaixo de 5% (1,4% → 0,1%). A nota é 10,0 porque todos os critérios da rubrica estão cobertos com números próprios e sem lacunas analíticas.

## Evidência

### Parte 1: Exploração

`variavel_x` preenchida com `taxa_abandono_carrinho_pct`. Mapa de calor (`px.imshow`), histogramas facetados das três variáveis de entrada e scatter facetado de cada variável vs. taxa de conversão. Justificativa: cita correlações −0,643 (abandono), +0,485 (scroll) e −0,229 (tempo), observa que as três variáveis têm distribuição aproximadamente normal e que os scatters indicam relação linear. o que justifica explicitamente o uso de regressão linear.

### Parte 2: Modelo

MAE (0,276) e RMSE (0,344) citados. R² = 0,714, MAE representando 4,70% da média da conversão. Coeficientes padronizados calculados (abandono −0,650, scroll +0,457, tempo −0,329). Análise de resíduos (scatter e histograma) e checagem de generalização treino/teste (MAE teste = 0,249 ≈ MAE treino = 0,276). Interpreta os coeficientes padronizados para comparação justa entre variáveis de escalas diferentes.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida (abandono e scroll). Tabela: abandono −0,489, scroll +0,258. Ranking completo das três variáveis calculado adicionalmente (tempo −0,112). Tornado diagram gerado com ±10% em p.p. de conversão (abandono ±0,287, scroll ±0,151, tempo ±0,066). Tabela de robustez confirmando índices estáveis para variações de 5%, 10% e 20%. Abandono tem 1,90× o impacto do scroll.

### Parte 4: Decisão

Recomenda priorizar redução do abandono e propõe teste A/B como validação (distinção associação/causalidade explícita). Cita índice −0,489 e traduz em valor de negócio: redução de 10% no abandono → +0,287 p.p. de conversão → ≈ 28,7 vendas extras/dia → ≈ R$ 129 mil/mês (com suposições declaradas). Limitações: linearidade e OAT, base simulada sem sazonalidade, suposições de volume e ticket como ordem de grandeza. Todas as limitações são específicas e relevantes.

### Ao Além dos Aléns (bônus)

Presente e executado. Simulação com dois cenários sobrepostos (situação atual vs. abandono −10%). Estatísticas: referência média 5,865%, P10 5,374%, P90 6,371%; cenário melhorado média 6,167%, P10 5,673%, P90 6,659%. Probabilidade de conversão abaixo de 5% caindo de 1,4% para 0,1%. Interpreta que a recomendação não apenas aumenta a média mas também reduz o risco de cenários ruins.

## Confiança

Confiança geral: Alta
