# Kanban Board — Sistema de Dimensionamento Energético Residencial

## 1. Estrutura do board

Colunas, da esquerda para a direita:

**Product Backlog → To Do → Doing (In Progress) → Review/Test → Done**

| Coluna | Finalidade |
|---|---|
| **Product Backlog** | User Stories já refinadas e prontas para virar tasks (não são movidas ao longo da Sprint). |
| **To Do** | Tasks selecionadas para a Sprint, prontas para começar. |
| **Doing** | Tasks em execução no momento. |
| **Review/Test** | Tasks implementadas, aguardando revisão/teste. |
| **Done** | Tasks concluídas e validadas conforme a Definition of Done. |

> Regra de WIP: cada integrante mantém, em geral, apenas **uma task principal** em "Doing" por vez.

---

## 2. Estado inicial do board (início da Sprint)

### 📋 Product Backlog

- **PB01** — Cadastro do imóvel
- **PB02** — Cadastro de equipamentos elétricos (catálogo)
- **PB03** — Associação de equipamentos ao imóvel
- **PB04** — Cálculo do consumo mensal por equipamento
- **PB05** — Cálculo do consumo total mensal do imóvel

### 🟦 To Do

- T01 — Definir estrutura de dados da entidade Imóvel *(PB01)*
- T06 — Definir estrutura de dados da entidade Equipamento *(PB02)*
- T11 — Implementar seleção de imóvel e de equipamento do catálogo *(PB03)*
- T17 — Implementar fórmula de cálculo do consumo por equipamento *(PB04)*
- T21 — Consultar consumos individuais dos equipamentos do imóvel *(PB05)*

### 🟨 Doing

*(vazio — será preenchido conforme as tasks acima forem iniciadas)*

### 🟧 Review/Test

*(vazio)*

### ✅ Done

*(vazio)*

---

## 3. Cartões — modelo de preenchimento

Cada task vira um cartão com os seguintes campos:

- **Título:** identificador + ação objetiva (ex.: `T03 — Implementar validação dos campos obrigatórios do imóvel`)
- **Descrição:** o que deve ser implementado.
- **User Story relacionada:** ex. PB01.
- **Responsável:** integrante que conduz a task.
- **Labels:** classificação do tipo de trabalho (ver tabela abaixo).
- **Checklist:** pequenos passos internos, quando existirem.

### Labels sugeridas

| Label | Uso |
|---|---|
| `frontend` | Interface/menu |
| `backend` | Regras e cálculo |
| `data` | Estrutura de dados |
| `test` | Testes |
| `bug` | Correção |
| `documentation` | Documentação |

---

## 4. Fluxo de movimentação dos cartões

- **Product Backlog → To Do:** a US já foi decomposta e a task foi selecionada para a Sprint.
- **To Do → Doing:** o trabalho foi efetivamente iniciado.
- **Doing → Review/Test:** a implementação terminou e aguarda revisão ou teste.
- **Review/Test → Done:** a task foi validada e atende à condição de conclusão.

O board deve refletir o estado real do projeto a cada dia — não deve ser atualizado apenas no momento da entrega.

---

## 5. Implementação no Trello

1. Crie um board chamado **Sistema de Dimensionamento Energético**.
2. Crie as listas, exatamente nesta ordem: `Product Backlog`, `To Do`, `Doing`, `Review/Test`, `Done`.
3. Adicione um cartão por US na lista **Product Backlog** (PB01 a PB05).
4. Adicione um cartão por task nas demais listas, começando em **To Do**, seguindo a seção 2 acima.
5. Preencha cada cartão com descrição, US relacionada, responsável e labels.
6. Movimente os cartões diariamente conforme o fluxo da seção 4.

## 6. Implementação no GitHub Projects

1. Crie um Project em modo **Board** no repositório da equipe.
2. Configure o campo **Status** com os valores: `Product Backlog`, `To Do`, `Doing`, `Review/Test`, `Done`.
3. Crie uma **Issue** para cada task (ex.: `T03 — Implementar validação dos campos obrigatórios do imóvel`), com a US relacionada na descrição.
4. Associe cada Issue ao Project e posicione-a na coluna correspondente.
5. Use **Assignees** para indicar o responsável e **Labels** para classificar o tipo de trabalho.
6. Referencie a Issue nos commits/Pull Requests relacionados, para manter a rastreabilidade entre planejamento e código.

---

## 7. Checklist de uso do Kanban

- [ ] Todas as tasks têm títulos objetivos.
- [ ] Todas as tasks estão associadas à User Story correspondente.
- [ ] O board possui as 5 colunas definidas.
- [ ] Tasks em "Doing" têm responsável definido.
- [ ] O número de tasks simultâneas em "Doing" está controlado (WIP).
- [ ] O board reflete o estado real do projeto.
- [ ] Tasks em "Done" foram de fato validadas (não apenas codificadas).
