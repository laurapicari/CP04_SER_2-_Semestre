## 1. Estrutura do board

**Product Backlog → To Do → Doing (In Progress) → Review/Test → Done**

| Coluna | Finalidade |
|---|---|
| **Product Backlog** | User Stories já refinadas e prontas para virar tasks (não são movidas ao longo da Sprint). |
| **To Do** | Tasks selecionadas para a Sprint atual, prontas para começar. |
| **Doing** | Tasks em execução no momento. |
| **Review/Test** | Tasks implementadas, aguardando revisão/teste. |
| **Done** | Tasks concluídas e validadas conforme a Definition of Done. |

---

## 2. Estado inicial do board 

A ordem de execução segue as metas definidas pela equipe a partir do
feedback de uso (ver seção 5 do documento de User Stories e Tasks).

### 📋 Product Backlog

- **PB01** — Cadastro do imóvel e do usuário responsável
- **PB02** — Registro do consumo mensal real, mês a mês
- **PB03** — Cálculo do consumo médio mensal, com explicação clara
- **PB04** — Identificação automática do maior consumo mensal
- **PB05** — Identificação do mês/ano do maior consumo
- **PB06** — Resumo energético completo
- **PB07** — Validação das entradas de consumo
- **PB08** — Gráfico de consumo mensal (texto)
- **PB09** — Persistência dos dados (implementada por último)

### 🟦 To Do (primeira leva de tasks, seguindo a ordem de prioridade)

- T01 — Definir estrutura de dados do imóvel *(PB01)*
- T06 — Implementar seleção do imóvel e entrada de mês/ano/consumo *(PB02)*
- T11 — Implementar o cálculo da soma dos consumos *(PB03)*
- T27 — Implementar validação do consumo (numérico e > 0) *(PB07)*

> As demais tasks de cada US (T02–T05, T07–T10, T12–T15, T16–T34...) entram
> em **To Do** à medida que a Sprint avança, na ordem das metas 1 a 8. As
> tasks de **PB09** (T35–T38) só entram em To Do depois que PB02 a PB08
> estiverem concluídas.

### 🟨 Doing

*(vazio — será preenchido conforme as tasks acima forem iniciadas)*

### 🟧 Review/Test

*(vazio)*

### ✅ Done

*(vazio)*

---

## 3. Cartões — modelo de preenchimento

Cada task vira um cartão com os seguintes campos:

- **Título:** identificador + ação objetiva (ex.: `T27 — Implementar validação do consumo`)
- **Descrição:** o que deve ser implementado.
- **User Story relacionada:** ex. PB07.
- **Responsável:** integrante que conduz a task.
- **Labels:** classificação do tipo de trabalho (ver tabela abaixo).
- **Checklist:** pequenos passos internos, quando existirem.


## Checklist 

- [ ] Todas as tasks têm títulos objetivos.
- [ ] Todas as tasks estão associadas à User Story correspondente.
- [ ] O board possui as 5 colunas definidas.
- [ ] Tasks em "Doing" têm responsável definido.
- [ ] O número de tasks simultâneas em "Doing" está controlado (WIP).
- [ ] O board reflete o estado real do projeto.
- [ ] Tasks em "Done" foram de fato validadas (não apenas codificadas).
- [ ] PB09 (persistência) só entra em execução depois das demais USs estarem estáveis.
