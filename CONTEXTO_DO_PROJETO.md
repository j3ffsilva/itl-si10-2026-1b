# CONTEXTO INICIAL DO PROJETO

## O Problema

O IPT tem uma Intranet no SharePoint que funciona, mas não funciona bem. Os colaboradores usam muito (cerca de 4 mil acessos por dia, 20 mil por semana), mas a experiência é frustrante. O principal sintoma é que as pessoas passam muito tempo **procurando** coisas operacionais (links de sistemas, documentos, informações do dia a dia) e pouco tempo **lendo** os conteúdos de comunicação interna que o time de Endomarketing produz. O buscador interno é ruim e retorna muitos arquivos irrelevantes. Há muitas páginas desatualizadas. E não existe nenhum tipo de segmentação de público — todo mundo vê o mesmo conteúdo, independentemente de ser pesquisador, técnico, administrativo ou operacional.

Além disso, a área de Endomarketing enfrenta um problema estratégico mais amplo: a comunicação interna do IPT é fragmentada, com excesso de canais, comunicados de última hora, e falta de engajamento real. A Intranet é o canal com maior frequência de acesso, então ela foi escolhida como o lugar certo para atacar esse problema.

---

## O Que Esperam de Solução

Querem uma reformulação da **home page da Intranet** baseada em dados reais de comportamento. Os objetivos principais são dois, aparentemente contraditórios mas complementares: **reduzir** o tempo gasto buscando links operacionais e **aumentar** o tempo gasto lendo conteúdos de comunicação. As métricas de sucesso são as disponíveis no próprio SharePoint — tempo gasto na página e quantidade de visualizações.

O escopo técnico envolve análise de UX e arquitetura da informação da home atual, modelagem do comportamento dos usuários (incluindo Simulação de Monte Carlo para testar cenários de layout), estruturação de testes A/B, e entrega de um protótipo navegável em HTML/CSS pronto para implementação, além de um dashboard analítico e documentação técnica no GitHub.

---

## O Que Foi Combinado no Kick-off

A reunião foi bastante densa e definiu várias coisas práticas:

**Sobre o projeto em si:** foi adotada a abordagem de um "teste A/B em esteroides" — mais planejado e cirúrgico do que um teste exploratório comum. Serão criadas 4 versões diferentes da home (B, C, D, E) para testar em paralelo com a home atual (A). A ideia é que 80-85% da audiência continue vendo a home original, e os 15-20% restantes sejam distribuídos entre as versões de teste, sem que os usuários saibam que estão participando de um experimento.

**Sobre segmentação:** ficou definido que os 4 grupos de público para segmentação de conteúdo serão Pesquisadores, Administrativos, Técnicos e Operacionais. Cada grupo tem necessidades diferentes — pesquisadores querem informações técnicas de negócio, administrativos querem processos internos, técnicos querem normas e regulamentações, e operacionais precisam de informações gerais como mudanças de procedimento.

**Sobre o que funciona bem e deve ser mantido:** o carrossel de notícias (rápido e visual) e a busca de colaboradores (para encontrar nome, e-mail e ramal de colegas) foram apontados como elementos que funcionam e não devem ser mexidos.

**Sobre dados e cronograma:** o IPT se comprometeu a enviar com urgência os dados do SharePoint (planilhas ou prints), a pesquisa de comunicação interna, o relatório de clima organizacional da FIA, e o manual de marca com as novas cores (basicamente azul, sem laranja). O ambiente de testes no SharePoint — um "site espelho" com as web parts atuais — precisa ser criado e acessos individuais precisam ser gerados para cada aluno na semana seguinte.

**Sobre cronograma das Sprints:** Sprint 1 focada em análise de dados e formação de hipóteses; Sprint 2 em modelagem de hipóteses; Sprint 3 em redesenho das páginas (prazo de 23 de maio para ter as versões B, C, D, E prontas); Sprint 4 em testes (início previsto para 10 de junho, durando 15-20 dias); Sprint 5 em coleta e análise final dos dados (entre 20 e 26 de junho).


---

## O que foi enviado

O arquivo contém **4 abas** exportadas diretamente do painel analítico do SharePoint, todas referentes à home da Intranet, com janela de 90 dias (25/jan a 24/abr/2026):

**Tráfego Geral** — série temporal diária com visualizadores exclusivos e visitas ao site. **Conteúdo Popular** — ranking dos 20 itens mais acessados na última semana, separados por tipo (News Post, Site Page, Document). **Uso por Dispositivo** — volume de visitas por tipo de dispositivo ao longo dos 90 dias. **Uso por Tempo** — heatmap de acesso por dia da semana e faixa horária.

---

## O que os dados revelam

**Volume e padrão de uso:** A intranet tem em média 4.145 visitas por dia útil, com pico de 5.818 visitas no dia 22/abr. Fins de semana são irrelevantes — média de apenas 128 visitas/dia, confirmando que o uso é estritamente profissional. Não há tendência de crescimento ou queda expressiva no período: os últimos 30 dias (média 4.203) são praticamente iguais ao período anterior (4.113), crescimento de apenas 2,2%.

**Dispositivos:** 97,6% dos acessos são feitos via desktop. Mobile somado (app + web) chega a apenas 2%, o que é uma informação valiosa de design — o redesenho não precisa se preocupar com responsividade móvel como prioridade, e pode explorar layouts mais ricos para tela grande.

**Horário de pico:** O acesso se concentra fortemente entre 8h e 11h, com pico absoluto às 8h–9h de quarta e segunda-feira. Isso sugere que a intranet funciona como um "ritual de abertura do dia de trabalho", o que tem implicações diretas para a estratégia de curadoria — comunicados publicados antes das 8h têm muito mais chance de serem lidos.

**Composição do tráfego por tipo de conteúdo:** Aqui está um dos achados mais importantes. Site Pages (páginas estruturais e funcionais) correspondem a 57,5% dos acessos, contra 32,4% de News Posts (comunicados) e apenas 10,2% de documentos. Dentro das páginas estruturais, o cardápio da semana aparece em segundo lugar entre as mais acessadas — com 293 visualizadores únicos — atrás apenas da própria Home. Organogramas, calendário de feriados e páginas da CGPe também aparecem com destaque.

**Concentração nos comunicados:** O tráfego de notícias é extremamente concentrado. Uma única notícia ("Serviços-e-Sistemas") representa 44% de todos os acessos a comunicados na semana, e as 3 primeiras juntas chegam a 77,5%. Das 20 notícias listadas, as últimas 10 têm apenas 1 a 4 visualizadores. Isso confirma empiricamente o problema da "infobesidade" apontado pelo parceiro: há muito conteúdo sendo publicado, mas a quase totalidade do engajamento se concentra em pouquíssimos itens.

---

## As dificuldades para chegar ao que o projeto precisa

Os dados enviados têm valor, mas apresentam lacunas sérias em relação ao que o projeto exige para funcionar bem.

**O problema central é a ausência de tempo de permanência na página.** Essa é a principal métrica de sucesso definida no kick-off — o projeto quer reduzir o tempo gasto buscando links e aumentar o tempo lendo conteúdos. Mas o SharePoint simplesmente não exporta isso de forma direta nesse relatório. As abas disponíveis medem visitas e visualizadores, não quanto tempo cada pessoa ficou em cada página. Sem esse dado de baseline, o teste A/B não terá como comparar se a nova versão realmente melhorou o engajamento — você sabe se mais pessoas acessaram, mas não se ficaram mais tempo.

**Não há dados por segmento de usuário.** O projeto definiu 4 grupos (Pesquisadores, Administrativos, Técnicos, Operacionais) e a segmentação é um dos objetivos centrais. Mas os dados enviados são completamente agregados — impossível saber se o cardápio da semana é acessado mais por técnicos, se os documentos normativos são buscados por pesquisadores, ou qual grupo passa mais tempo na home. Sem isso, qualquer hipótese de segmentação é especulativa.

**Os nomes dos conteúdos são URLs, não títulos.** "Serviços-e-Sistemas(1).aspx" e "Criação.aspx" não permitem entender de imediato do que se trata cada comunicado. Para modelar hipóteses sobre que tipo de conteúdo engaja mais, seria necessário mapear esses slugs para os títulos e categorias reais dos comunicados.

**Os dados de tempo são em fuso UTC, não no horário de Brasília.** O SharePoint exporta as datas com timestamp UTC (os números seriais mostram horário 20:59, que equivale a 17:59 BRT). Isso não compromete a análise de tendência diária, mas distorce o heatmap de uso por hora — os picos identificados precisam ser deslocados 3 horas para representar o comportamento real dos usuários.

**Falta contexto sobre eventos.** Não há informação sobre o que foi publicado em cada dia, o que impede identificar se os picos de acesso (como o máximo de 5.818 visitas em 22/abr) foram causados por um comunicado específico, por uma campanha, ou por fatores externos. Para a modelagem de Monte Carlo prevista na Sprint 1, seria importante cruzar o volume de acesso com o que estava sendo veiculado.

**O relatório de Conteúdo Popular cobre apenas 7 dias e lista apenas os top 20.** Para entender padrões de comportamento mais robustos e montar o baseline de comparação pós-teste, seria necessário um período mais longo e a lista completa de conteúdos — não apenas os mais acessados.

Em síntese, os dados entregues são suficientes para descrever o perfil geral de uso da intranet, mas insuficientes para construir as hipóteses comportamentais que sustentarão o design do teste A/B. As próximas ações críticas do parceiro — entregar os dados de comunicação interna, o relatório de clima, e criar o ambiente sandbox — são precisamente o que vai preencher as lacunas mais importantes.