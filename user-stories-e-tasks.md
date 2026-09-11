# Sistema de Dimensionamento Energético Residencial
## MVP v2 — User Stories e Tasks (com base no feedback de uso)

---

## 1. Problemas identificados na versão anterior

| ID | Problema | Relato do usuário | Prioridade |
|----|---|---|---|
| P01 | Resultado pouco claro | "Não sei o que significa essa média." | Alta |
| P02 | Cálculo limitado | "Meu consumo não depende apenas da quantidade de aparelhos." | Alta |
| P03 | Não existe histórico | "Não consigo comparar meu consumo ao longo dos meses." | Alta |
| P04 | Não mostra maior consumo | "Quero saber qual foi meu pior mês." | Alta |
| P05 | Não mostra o mês do pico | "Quando eu mais consumi energia?" | Média |
| P06 | Não há resumo | "Quero entender meu resultado rapidamente." | Alta |
| P07 | Não há gráfico | "Queria visualizar meu consumo." | Baixa |
| P08 | Entradas podem gerar erro | "E se eu colocar 0 ou um valor inválido?" | Alta |
| P09 | Dados são perdidos | "Se eu fechar o programa, perdi tudo?" | Alta |
| P10 | Não há usuário/imóvel | "Onde ficam salvos meus dados?" | Alta |
| P11 | Não há visibilidade | "Queria visualizar meu consumo." | Baixa |
| P12 | Entradas podem gerar erro | "E se eu colocar 0 ou um valor inválido?" | Alta |

## 2. Mudança de abordagem no cálculo

A versão anterior estimava o consumo a partir de equipamentos cadastrados
(potência × quantidade × tempo de uso). O feedback (P02) mostrou que isso
não reflete o consumo real do usuário. **A partir desta versão, o consumo
mensal é informado diretamente pelo usuário, em kWh**, mês a mês, e o
sistema passa a trabalhar sobre esse histórico.

---

## 3. Novo Product Backlog

| ID | Prioridade | User Story | Problema(s) atendido(s) |
|----|---|---|---|
| PB01 | Alta | Cadastro do imóvel e do usuário responsável | P10 |
| PB02 | Alta | Registro do consumo mensal real, mês a mês | P02, P03 |
| PB03 | Alta | Cálculo do consumo médio mensal, com explicação clara do cálculo | P01, P06 |
| PB04 | Alta | Identificação automática do maior consumo mensal registrado | P04 |
| PB05 | Média | Identificação do mês/ano em que ocorreu o maior consumo | P05 |
| PB06 | Alta | Resumo energético completo do imóvel | P06 |
| PB07 | Alta | Validação de todas as entradas de consumo | P08, P12 |
| PB08 | Baixa | Representação visual (gráfico em texto) do consumo mensal | P07, P11 |
| PB09 | Alta (implementada por último) | Persistência dos dados do imóvel/usuário e do histórico de consumo | P09 |

> PB01 cobre o cadastro básico do imóvel/usuário em memória, necessário
> desde o início para que os demais itens funcionem. PB09 cobre tornar
> esses dados **persistentes** entre execuções (arquivo/banco de dados) —
> por decisão da equipe, essa parte é implementada por último, depois que
> o cálculo, a validação e a visualização estiverem estáveis.

---

## 4. Decomposição das User Stories em Tasks

### PB01 — Cadastro do imóvel e do usuário responsável

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero cadastrar um imóvel e informar quem é o responsável por ele, para saber a quem pertence cada histórico de consumo. |
| **Critérios de aceite** | 1. Registrar identificação e endereço do imóvel.<br>2. Registrar o nome do usuário responsável.<br>3. Impedir cadastro com campos obrigatórios vazios. |
| **Componentes envolvidos** | Interface / dados / validação / testes |
| **Tasks** | T01 — Definir estrutura de dados do imóvel (id, nome, endereço, usuário).<br>T02 — Implementar rotina de cadastro do imóvel.<br>T03 — Validar campos obrigatórios.<br>T04 — Implementar listagem de imóveis cadastrados.<br>T05 — Testar cadastro com dados válidos e inválidos. |
| **Dependências** | Pré-requisito de todas as demais USs (é necessário um imóvel para registrar consumo). |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB02 — Registro do consumo mensal real

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero informar meu consumo mensal real em kWh, mês a mês, para que o sistema reflita meu consumo de energia de verdade. |
| **Critérios de aceite** | 1. Permitir informar mês, ano e consumo em kWh.<br>2. Permitir registrar vários meses para o mesmo imóvel, formando um histórico.<br>3. Ao registrar um mês/ano já existente, atualizar o valor em vez de duplicar. |
| **Componentes envolvidos** | Interface / dados de consumo / validação |
| **Tasks** | T06 — Implementar seleção do imóvel e entrada de mês/ano/consumo.<br>T07 — Associar o registro de consumo ao imóvel correto.<br>T08 — Tratar atualização de um mês/ano já registrado.<br>T09 — Persistir o registro na estrutura em memória.<br>T10 — Testar o cadastro de vários meses, inclusive repetidos. |
| **Dependências** | Depende de PB01 (imóvel já cadastrado). |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB03 — Cálculo do consumo médio mensal, com explicação clara

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero ver a média do meu consumo mensal e entender exatamente como ela foi calculada, para confiar no resultado apresentado. |
| **Critérios de aceite** | 1. Calcular a média como soma dos consumos ÷ número de meses registrados.<br>2. Exibir o total somado, a quantidade de meses e a média final.<br>3. Tratar o caso de nenhum mês registrado (evitar divisão por zero). |
| **Componentes envolvidos** | Regra de negócio / dados / interface |
| **Tasks** | T11 — Implementar o cálculo da soma dos consumos.<br>T12 — Implementar o cálculo da média (soma ÷ meses).<br>T13 — Exibir a explicação do cálculo (soma, quantidade de meses, resultado).<br>T14 — Tratar imóvel sem consumo registrado.<br>T15 — Testar com diferentes quantidades de meses. |
| **Dependências** | Depende de PB02 (histórico de consumo já registrado). |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB04 — Identificação do maior consumo mensal

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero saber qual foi meu maior consumo mensal, para identificar automaticamente meu pior mês. |
| **Critérios de aceite** | 1. Identificar o maior valor de consumo entre os meses registrados.<br>2. Tratar o caso de nenhum mês registrado. |
| **Componentes envolvidos** | Dados de consumo / regra de negócio |
| **Tasks** | T16 — Consultar os consumos registrados do imóvel.<br>T17 — Implementar a identificação do maior valor.<br>T18 — Tratar imóvel sem registros.<br>T19 — Testar com diferentes conjuntos de valores (incluindo empates). |
| **Dependências** | Depende de PB02. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB05 — Mês/ano do maior consumo

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero saber em qual mês e ano eu mais consumi energia, para identificar o período de maior consumo. |
| **Critérios de aceite** | 1. Informar o mês e o ano correspondentes ao maior consumo registrado. |
| **Componentes envolvidos** | Dados de consumo / regra de negócio / interface |
| **Tasks** | T20 — Recuperar o mês/ano associado ao maior valor identificado em PB04.<br>T21 — Exibir o mês por extenso e o ano na interface.<br>T22 — Testar com registros de diferentes meses e anos. |
| **Dependências** | Depende de PB04. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB06 — Resumo energético completo

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero entender meu resultado rapidamente, para ter uma visão geral do meu consumo de energia. |
| **Critérios de aceite** | 1. Apresentar todos os meses registrados, em ordem cronológica.<br>2. Apresentar a média mensal e o maior consumo (com mês/ano) no mesmo resumo. |
| **Componentes envolvidos** | Interface / dados / resumo geral |
| **Tasks** | T23 — Ordenar os registros de consumo por ano/mês.<br>T24 — Montar a listagem de consumos no resumo.<br>T25 — Incluir média e maior consumo no resumo.<br>T26 — Testar o resumo com diferentes quantidades de registros. |
| **Dependências** | Depende de PB02, PB03 e PB04/PB05. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB07 — Validação das entradas

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero receber um aviso quando informar 0 ou um valor inválido, para evitar erros no cálculo. |
| **Critérios de aceite** | 1. Rejeitar consumo igual a zero, negativo ou não numérico.<br>2. Rejeitar mês fora do intervalo 1–12 e ano fora de um intervalo razoável.<br>3. Exibir mensagem de erro clara e pedir a informação novamente. |
| **Componentes envolvidos** | Interface / validação / mensagens de erro |
| **Tasks** | T27 — Implementar validação do consumo (numérico e > 0).<br>T28 — Implementar validação do mês (1–12).<br>T29 — Implementar validação do ano.<br>T30 — Testar entradas com 0, texto, valores negativos e valores válidos. |
| **Dependências** | Aplica-se a PB02 (deve ser usada nas entradas de registro de consumo). |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB08 — Gráfico de consumo mensal (texto)

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero visualizar meu consumo, para conseguir comparar os valores registrados ao longo dos meses. |
| **Critérios de aceite** | 1. Representar visualmente o consumo de cada mês registrado (ex.: barras em texto).<br>2. Manter a ordem cronológica dos meses. |
| **Componentes envolvidos** | Interface / histórico de consumo / dados |
| **Tasks** | T31 — Ordenar os registros cronologicamente.<br>T32 — Calcular a escala das barras em relação ao maior valor.<br>T33 — Exibir o gráfico em texto (barras + valor em kWh).<br>T34 — Testar com diferentes quantidades de meses cadastrados. |
| **Dependências** | Depende de PB02. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB09 — Persistência dos dados

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero que meus dados não se percam ao fechar o programa, para não precisar recadastrar tudo a cada uso. |
| **Critérios de aceite** | 1. Salvar imóveis, usuários e histórico de consumo em um arquivo.<br>2. Carregar os dados automaticamente ao iniciar o sistema.<br>3. Tratar erros de leitura/escrita do arquivo sem travar o sistema. |
| **Componentes envolvidos** | Dados / persistência / testes |
| **Tasks** | T35 — Implementar a gravação dos dados em arquivo (JSON).<br>T36 — Implementar o carregamento dos dados ao iniciar o sistema.<br>T37 — Tratar falhas de leitura/escrita do arquivo.<br>T38 — Testar persistência entre execuções (fechar e reabrir o programa). |
| **Dependências** | Depende de todas as USs anteriores estarem estáveis; implementada por último. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

---

## 5. Metas para a próxima versão (ordem de execução)

1. Corrigir/clarear o cálculo → **PB03**
2. Permitir cadastrar consumo de vários meses → **PB02**
3. Calcular média e maior consumo → **PB03 / PB04**
4. Mostrar o mês de maior consumo → **PB05**
5. Criar um resumo do resultado → **PB06**
6. Adicionar validações → **PB07**
7. Adicionar gráfico → **PB08**
8. Implementar usuário, imóvel e persistência dos dados → **PB01 (base) / PB09 (persistência, por último)**

---

## 6. Definition of Done (DoD) do projeto

Uma User Story só é considerada concluída quando:

- [ ] O código está implementado.
- [ ] A funcionalidade está integrada ao sistema.
- [ ] Os critérios de aceite foram atendidos.
- [ ] As validações necessárias foram implementadas.
- [ ] Os testes foram executados sem erros conhecidos impeditivos.
- [ ] O código está versionado no repositório da equipe.

---

## 7. Checklist final de revisão

- [ ] Todas as tasks começam com uma ação clara (criar, implementar, validar, calcular, testar...).
- [ ] Nenhuma task é ampla demais (ex.: "fazer o cálculo").
- [ ] As dependências entre tasks estão claras.
- [ ] O conjunto de tasks de cada US atende a todos os seus critérios de aceite.
- [ ] Interface, regras de negócio, dados e testes foram considerados em cada US.
