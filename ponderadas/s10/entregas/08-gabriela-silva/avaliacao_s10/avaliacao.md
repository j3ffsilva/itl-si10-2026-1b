# Avaliação - Gabriela Silva

Estudante: Gabriela Silva

Rubrica: `../../../rubrica_s10.md`

Nota: 9,5

Feedback:

Respondeu as quatro partes com números do notebook em cada seção. Na Parte 3, calculou os índices das três variáveis e argumentou que sensibilidade difere de coeficiente isolado. Na Parte 2, acrescentou que RMSE (0,344) ≈ σ do ruído de geração (0,35), concluindo que o modelo não deixou sinal sistemático residual. A limitação da Parte 4 usa tabela própria de resíduos, mostrando que 15,6% dos dias têm erro acima de 0,5 p.p. O bônus cita P10/P90 e compara o ganho esperado (0,29 p.p.) ao desvio padrão simulado. A nota fica em 9,5 porque a Parte 4 não distingue associação de causalidade: propõe ações de produto sem ressalvar que a relação observada é associativa.

## Evidência

### Parte 1: Exploração

Dois scatters gerados (abandono e scroll) via subplots. Justificativa numérica: cita correlação −0,643 para abandono ("relação inversa muito nítida") e +0,485 para scroll, conectando o sinal à interpretação de engajamento do usuário.

### Parte 2: Modelo

MAE (0,276) e RMSE (0,344) citados. Argumento notável: RMSE ≈ σ do ruído de geração (0,35), indicando que o modelo não deixou sinal sistemático residual. Relação RMSE/MAE ≈ 1,25 identificada como esperada para resíduos normais. Contexto de escala (média da conversão ≈ 5,87%) mencionado.

### Parte 3: Análise de Sensibilidade

`variaveis_escolhidas` preenchida com as três variáveis (indo além do pedido para demonstrar ranking completo). Tabela gerada com índices: abandono −0,489, scroll +0,258, tempo −0,112. Explica a razão de o abandono ser ≈ 1,9× mais sensível que o scroll. Argumento correto sobre sensibilidade versus coeficiente bruto.

### Parte 4: Decisão

Recomenda priorizar checkout com índice −0,489 como justificativa. Cita valores numéricos (47,5% → 42,7%, ganho de 0,29 p.p.). Propõe ações concretas ("checkout em uma página", transparência de frete, selos de confiança). Limitação específica: variáveis externas não mapeadas (sazonalidade, concorrência, perfil do tráfego) e evidência dos resíduos com tabela própria. Não distingue associação de causalidade de forma explícita.

### Ao Além dos Aléns (bônus)

Presente e executado. Estatísticas de saída corretas (média 5,87%, std 0,393, P10 = 5,37%, P90 = 6,38%). Interpreta risco: 90% dos cenários acima de 5,37%, não há caudas longas. Menciona que o ganho esperado (0,29 p.p.) é comparável ao desvio padrão simulado, mantendo a cautela analítica.

## Confiança

Confiança geral: Alta
