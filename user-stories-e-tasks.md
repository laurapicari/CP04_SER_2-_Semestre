# Sistema de Dimensionamento Energético Residencial
## Definição do MVP, User Stories e Tasks

---

## 1. Escopo do MVP

O objetivo do MVP é estimar o **consumo médio mensal de energia elétrica** de uma
residência a partir dos equipamentos que ela possui. O sistema deve permitir:

1. Cadastrar um **imóvel** (identificação básica).
2. Manter uma **base de equipamentos elétricos** (nome, categoria e potência
   nominal em watts).
3. **Associar equipamentos a um imóvel**, informando a quantidade de cada um e o
   tempo médio diário de uso.
4. **Calcular o consumo mensal estimado de cada equipamento**, considerando
   potência, quantidade e tempo de uso.
5. **Somar o consumo de todos os equipamentos** e apresentar o consumo total
   médio mensal do imóvel, em **kWh/mês**.

> Fórmula utilizada: `consumo (kWh/mês) = (potência_W × quantidade × horas_de_uso_por_dia × 30) / 1000`

Itens como histórico de meses anteriores, comparação entre meses, maior
consumo registrado e gráficos **não fazem parte deste MVP** — eles dependem de
um recurso (registro de consumo real mês a mês) que ainda não foi solicitado
no escopo atual e podem ser tratados como evolução futura do produto.

---

## 2. Product Backlog (User Stories)

| ID | User Story |
|----|------------|
| PB01 | Cadastro do imóvel |
| PB02 | Cadastro de equipamentos elétricos (catálogo) |
| PB03 | Associação de equipamentos ao imóvel |
| PB04 | Cálculo do consumo mensal por equipamento |
| PB05 | Cálculo do consumo total mensal do imóvel |

---

## 3. Decomposição das User Stories em Tasks

### PB01 — Cadastro do imóvel

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero cadastrar um imóvel com suas informações básicas, para identificar a residência que terá seu consumo energético estimado. |
| **Critérios de aceite** | 1. Registrar identificação (nome/apelido) do imóvel.<br>2. Registrar endereço/localidade do imóvel.<br>3. Impedir o cadastro caso algum campo obrigatório esteja vazio. |
| **Componentes envolvidos** | Interface / dados / validação / testes |
| **Tasks** | T01 — Definir a estrutura de dados da entidade Imóvel (id, nome, endereço).<br>T02 — Implementar a rotina de cadastro do imóvel.<br>T03 — Implementar validação dos campos obrigatórios.<br>T04 — Implementar mensagem de confirmação do cadastro.<br>T05 — Criar testes com dados válidos e inválidos. |
| **Dependências** | T01 é pré-requisito de T02; T02 é pré-requisito de T03 e T04. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB02 — Cadastro de equipamentos elétricos (catálogo)

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero cadastrar equipamentos elétricos com nome, categoria e potência nominal, para montar uma base de equipamentos disponíveis para associar aos imóveis. |
| **Critérios de aceite** | 1. Registrar nome e categoria do equipamento.<br>2. Registrar a potência nominal em watts (W).<br>3. Rejeitar potência igual a zero ou negativa.<br>4. Permitir listar os equipamentos já cadastrados. |
| **Componentes envolvidos** | Interface / dados / validação / testes |
| **Tasks** | T06 — Definir a estrutura de dados da entidade Equipamento (id, nome, categoria, potência).<br>T07 — Implementar a rotina de cadastro de equipamento.<br>T08 — Implementar validação numérica e positiva da potência.<br>T09 — Implementar a listagem do catálogo de equipamentos.<br>T10 — Criar testes com valores válidos e inválidos de potência. |
| **Dependências** | T06 é pré-requisito das demais; T07 e T09 podem ser feitas em paralelo após T06. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB03 — Associação de equipamentos ao imóvel

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero selecionar equipamentos do catálogo e informar a quantidade e o tempo médio diário de uso para um imóvel, para registrar como a residência consome energia. |
| **Critérios de aceite** | 1. Permitir selecionar um equipamento já existente no catálogo.<br>2. Informar a quantidade (número inteiro maior que zero).<br>3. Informar o tempo médio diário de uso em horas, entre 0 e 24.<br>4. Permitir associar vários equipamentos ao mesmo imóvel. |
| **Componentes envolvidos** | Interface / dados / validação / testes |
| **Tasks** | T11 — Implementar seleção de imóvel e de equipamento do catálogo.<br>T12 — Implementar entrada da quantidade do equipamento.<br>T13 — Implementar entrada do tempo médio diário de uso.<br>T14 — Validar quantidade (positiva) e horas de uso (0–24).<br>T15 — Persistir a associação equipamento–imóvel.<br>T16 — Criar testes com combinações válidas e inválidas. |
| **Dependências** | Depende de PB01 (imóvel cadastrado) e PB02 (equipamento cadastrado); T11 antes de T12/T13; T14 antes de T15. |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB04 — Cálculo do consumo mensal por equipamento

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero que o sistema calcule o consumo mensal estimado de cada equipamento associado ao imóvel, para saber quanto cada aparelho contribui no consumo total. |
| **Critérios de aceite** | 1. Calcular o consumo mensal em kWh considerando potência, quantidade e tempo de uso diário.<br>2. Exibir o consumo individual de cada equipamento associado ao imóvel. |
| **Componentes envolvidos** | Regra de negócio / dados / interface / testes |
| **Tasks** | T17 — Implementar a fórmula de cálculo (potência × quantidade × horas × 30 dias / 1000).<br>T18 — Formatar o resultado em kWh/mês.<br>T19 — Exibir o consumo de cada equipamento na interface.<br>T20 — Criar testes com diferentes combinações de potência, quantidade e horas. |
| **Dependências** | Depende de PB03 (associação equipamento–imóvel concluída). |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

### PB05 — Cálculo do consumo total mensal do imóvel

| Campo | Descrição |
|---|---|
| **User Story** | Como usuário, quero visualizar o consumo total médio mensal estimado do imóvel, para entender meu gasto energético geral. |
| **Critérios de aceite** | 1. Somar o consumo mensal de todos os equipamentos associados ao imóvel.<br>2. Exibir o resultado total em kWh/mês.<br>3. Tratar o caso de um imóvel sem equipamentos associados. |
| **Componentes envolvidos** | Regra de negócio / dados / resumo geral / testes |
| **Tasks** | T21 — Consultar os consumos individuais dos equipamentos do imóvel.<br>T22 — Implementar a soma dos consumos.<br>T23 — Tratar o caso de imóvel sem equipamentos.<br>T24 — Exibir o resumo total do imóvel na interface.<br>T25 — Criar testes com diferentes quantidades de equipamentos. |
| **Dependências** | Depende de PB04 (consumo por equipamento já calculado). |
| **Condição de conclusão** | Critérios de aceite atendidos + Definition of Done. |

---

## 4. Definition of Done (DoD) do projeto

Uma User Story só é considerada concluída quando:

- [ ] O código está implementado.
- [ ] A funcionalidade está integrada ao sistema.
- [ ] Os critérios de aceite foram atendidos.
- [ ] As validações necessárias foram implementadas.
- [ ] Os testes foram executados sem erros conhecidos impeditivos.
- [ ] O código está versionado no repositório da equipe.

---

## 5. Checklist final de revisão

- [ ] Todas as tasks começam com uma ação clara (criar, implementar, validar, calcular, testar...).
- [ ] Nenhuma task é ampla demais (ex.: "fazer o cadastro").
- [ ] As dependências entre tasks estão claras.
- [ ] O conjunto de tasks de cada US atende a todos os seus critérios de aceite.
- [ ] Interface, regras de negócio, dados e testes foram considerados em cada US.
