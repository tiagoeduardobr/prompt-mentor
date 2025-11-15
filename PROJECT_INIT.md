# PROJECT_INIT.md

## Nome do Projeto

Prompt Mentor — Engenharia de Software e Projetos

## Descrição

O Prompt Mentor é um sistema modular de *prompt engineering* que simula um **mentor sênior de engenharia de software**, especializado em ensinar boas práticas, segurança, versionamento e desenvolvimento profissional de software.  
O objetivo é transformar o aprendizado técnico em um processo orientado por projetos, com qualidade e metodologia de engenharia real.

---

## Missão

Desenvolver um mentor baseado em IA que:

- Ensina engenharia de software de forma prática e profissional.
- Garante segurança, clareza e valor de portfólio.
- Orienta estudantes e desenvolvedores a criar projetos completos e documentados.

---

## Visão

Criar o primeiro **framework open source de engenharia de prompt** aplicado ao ensino técnico, combinando:

- Padrões de engenharia de software.
- Processos educacionais estruturados.
- Modularidade e escalabilidade de agentes.

---

## Público-Alvo

| Perfil      | Descrição                               | Objetivo                                 |
| ----------- | --------------------------------------- | ---------------------------------------- |
| Estudantes  | Aprendendo desenvolvimento full-stack   | Aprender boas práticas e segurança       |
| Devs Júnior | Já dominam a sintaxe, buscam maturidade | Evoluir qualidade técnica e profissional |
| Educadores  | Professores e mentores técnicos         | Estruturar projetos guiados              |
| Autônomos   | Profissionais construindo portfólio     | Criar projetos completos e documentados  |

---

## Estrutura Inicial do Repositório

prompt-mentor/
│
├── README.md
├── LICENSE
├── mentor/
│   ├── MENTOR_SENIOR_ENGINEERING_GUIDE.md
│   ├── prompt_config.yaml
│   ├── specializations/
│   │   ├── security_mentor.md
│   │   ├── clean_code_mentor.md
│   │   ├── devops_mentor.md
│   ├── examples/
│   │   ├── example_request.md
│   │   ├── example_output.md
│   └── templates/
│       ├── default_prompt.txt
│       ├── portfolio_prompt.txt
│
├── guided-projects/
│   ├── api_fastapi_todo/
│   ├── frontend_react_portfolio/
│
├── tests/
│   ├── test_prompt_format.py
│   └── test_output_quality.py
│
├── cli/
│   └── mentor_cli.py
│
├── docs/
│   ├── PROJECT_OVERVIEW.md
│   ├── PROMPT_ENGINEERING_GUIDE.md
│   ├── ROADMAP.md
│   └── ARCHITECTURE.md
│
├── .vscode/
│   ├── extensions.json
│   └── settings.json
│
└── .github/
    ├── workflows/
    │   ├── validate_prompts.yml
    │   └── deploy_gh_pages.yml
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md

---

## Arquitetura Conceitual

Usuário ─▶ Prompt Principal (MENTOR_SENIOR_ENGINEERING_GUIDE.md)
       └▶ Configuração (prompt_config.yaml)
       └▶ Contextos (exemplos, templates, histórico)
       └▶ Modelo LLM (GPT, Claude, Mistral, etc.)
       └▶ Output estruturado (Markdown, diffs, commits, testes)

**Camadas:**

- **Core Prompt:** define a identidade e diretrizes fixas do mentor.  
- **Config Layer:** controla tom, formato e comportamento.  
- **Context Layer:** armazena histórico, exemplos e templates.  
- **Output Layer:** garante formato profissional e padronizado.

---

## Fases do Projeto e Roadmap

| Fase   | Nome       | Foco                              | Entregáveis                                                             |
| ------ | ---------- | --------------------------------- | ----------------------------------------------------------------------- |
| Fase 1 | Fundação   | Estrutura e guia principal        | PROJECT_INIT.md, MENTOR_SENIOR_ENGINEERING_GUIDE.md, prompt_config.yaml |
| Fase 2 | Expansão   | Modularização e testes de prompts | /specializations/, /tests/                                              |
| Fase 3 | Integração | CLI e workflows automáticos       | mentor_cli.py, .github/workflows/                                       |
| Fase 4 | Educação   | Projetos guiados e trilhas        | /guided-projects/, /docs/roadmap.md                                     |
| Fase 5 | Comunidade | Portal e contribuições abertas    | CONTRIBUTING.md, GitHub Pages                                           |

---

## Filosofia de Engenharia

- Clareza sobre complexidade.  
- Transparência e rastreabilidade.  
- Segurança e ética em todas as interações.  
- Reprodutibilidade e documentação contínua.  
- Evolução modular e incremental.

---

## Monitoramento e Logging

- Implementar logger estruturado configurável para diferentes níveis de log (INFO, DEBUG, ERROR)
- Centralizar configurações de logging em módulo dedicado (`cli/logging_config.py`)

## Testes de Segurança Automatizados

- Incluir testes automatizados para fuzz testing e validação rigorosa de entradas
- Rodar testes em CI/CD para detectar vulnerabilidades precocemente

## Gestão e Atualização da Política de Segurança

- Estabelecer revisão periódica da política OWASP Top 10 adotada e atualizações de bibliotecas críticas

## Gestão de Tokens e Autenticação Segura

- Planejar módulo de autenticação JWT seguro, com validação e expiração claras

## Validação Estrita no CLI

- Validar entradas do usuário no `cli/mentor_cli.py` usando Pydantic para evitar vulnerabilidades

---

## Riscos e Dependências Iniciais

- **Riscos:** Dependência de modelos LLM externos (ex: OpenAI, Claude) pode introduzir custos ou limitações de API.  
  **Mitigação:** suportar modelos open-source locais.
- **Dependências:** Python 3.8+, **Poetry** para gerenciamento de dependências.
- **Segurança:** Evitar exposição de chaves API; usar variáveis de ambiente.  
  **Mitigação adicional:** configurar script de validação de `.env` e ignorar chaves API em `.gitignore`.  
  **Governança:** adicionar verificação automática em workflow CI (`validate_env.yml`) para confirmar variáveis sensíveis ausentes no código. (Ver TODO P1-07)

---

## Diretrizes de Qualidade (Definition of Done)

Uma tarefa (TODO) só é considerada concluída quando:

- **[Processo]** Passa por revisão técnica e didática.
- **[Processo]** Está integrada ao fluxo de versionamento (branch `feature/ID-XX` e commit semântico).
- **[Processo]** Gera um PR simulado com descrição e checklist (conforme `MENTOR_GUIDE.md` e `PULL_REQUEST_TEMPLATE.md`).
- **[Documentação]** Possui documentação atualizada (README.md, docstrings, .env.example, CONTRIBUTING.md e docs/).
- **[Código]** O código segue os padrões de Lint (black, isort, flake8) sem erros.
- **[Código]** Nenhum segredo (chaves, senhas) está hardcoded (validação via `bandit`).
- **[Testes]** Todos os testes (`pytest`) passam.
- **[Testes]** A cobertura de testes (Coverage) é maior ou igual a 70%.
- **[Testes]** Apresenta exemplo funcional e validado.
- **[Logs]** A aplicação possui logging estruturado para observabilidade.

---

## TODOs Profissionais (Backlog Inicial)

### 🟢 P0 — Prioridade Alta (Fundação)

- [x] **[P0-01]** Criar o repositório GitHub prompt-mentor.
- [x] **[P0-02]** Adicionar LICENSE (MIT).
- [x] **[P0-03]** Adicionar PROJECT_INIT.md com escopo definido (este arquivo).
- [x] **[P0-04]** Criar MENTOR_SENIOR_ENGINEERING_GUIDE.md como guia central.
- [x] **[P0-05]** Criar prompt_config.yaml com parâmetros ajustáveis.
  
      *Incluir campos de configuração de segurança (tokens, modelo, endpoint) com placeholders e leitura via variáveis de ambiente.*
- [x] **[P0-06]** Criar .gitignore com regras básicas para Python (ex: .env, `__pycache__`, .venv, .pytest_cache, *.pyc).
- [ ] **[P0-07]** Adicionar README.md inicial com propósito e estrutura.
- [ ] **[P0-08]** Montar estrutura de diretórios inicial (mentor/, docs/, examples/, .vscode/).
- [ ] **[P0-09]** Documentar filosofia e boas práticas de engenharia de prompt.
- [ ] **[P0-10]** Inicializar o projeto com `Poetry` (criando o `pyproject.toml`).
- [ ] **[P0-11]** Adicionar dependências básicas de projeto e qualidade via Poetry (ex: PyYAML, rich, typer, pytest, pytest-cov, black, isort, flake8, bandit, safety, python-dotenv, mkdocs).
- [ ] **[P0-12]** Configurar .env.example com variáveis de ambiente seguras.
- [ ] **[P0-13]** Adicionar instruções de configuração segura no README.md.
- [ ] **[P0-14]** Configurar `pytest` (com `pytest-cov`) dentro do `pyproject.toml`.
- [ ] **[P0-15]** Configurar as regras de `black`, `isort`, e `flake8` dentro do `pyproject.toml`.
- [ ] **[P0-16]** Criar script inicial de verificação de segurança (rodando `bandit` e `safety`).
- [ ] **[P0-17]** Criar `CONTRIBUTING.md` com o guia de configuração inicial do desenvolvedor (clonar, `poetry install`, `poetry shell`, `poetry run pytest`).
- [ ] **[P0-18]** Criar templates de configuração do VS Code (`.vscode/settings.json`) para formatar com Black ao salvar e usar o interpretador do Poetry.
- [ ] **[P0-19]** Criar template de extensões recomendadas (`.vscode/extensions.json`).
- [ ] **[P0-20]** Definir a estratégia de logging para a CLI (configuração do `logging` no pyproject.toml ou em um módulo de config).
- [ ] **[P0-21]** Implementar módulo de logging estruturado em `cli/logging_config.py`.
- [ ] **[P0-22]** Criar testes automatizados focados em segurança, incluindo fuzz testing em `/tests/security_tests.py`.
- [ ] **[P0-23]** Integrar novos testes de segurança no workflow CI `.github/workflows/validate_security.yml`.
- [ ] **[P0-24]** Documentar métricas de qualidade e segurança em `docs/PROJECT_OVERVIEW.md`.
- [ ] **[P0-25]** Implementar módulo para gerenciamento seguro de tokens JWT em `cli/auth.py`.
- [ ] **[P0-26]** Reforçar validação de entrada CLI utilizando Pydantic no arquivo `cli/mentor_cli.py`.
- [ ] **[P0-27]** Adicionar documentação para processo de deploy seguro e rollback em `docs/DEPLOYMENT.md`.
- [ ] **[P0-28]** Estabelecer revisão periódica da política de segurança e atualização do OWASP Top 10 (documentação e cronogramas).
*[P1-12]** Integrar badges (Shields.io) de status do CI, code coverage e licença no README.md.

### 🔵 P2 — Prioridade Baixa (Integração e Educação)

- [ ] **[P2-01]** Desenvolver `cli/mentor_cli.py` como uma CLI Tool robusta (usando Typer) com sub-comandos (ex: `init`, `ask`, `review`, `next-task`).
- [ ] **[P2-02]** Adicionar repositórios guiados em /guided-projects/.
- [ ] **[P2-03]** Criar trilhas educacionais no docs/ROADMAP.md.
- [ ] **[P2-04]** Adicionar mentor/review_prompt.md para simular code review.
- [ ] **[P2-05]** Integrar testes de prompt ao CI/CD.
- [ ] **[P2-06]** Formalizar processo de contribuição (além do `CONTRIBUTING.md` inicial):
  - [ ] **[P2-06a]** Criar templates de Issues (bug_report.md, feature_request.md) no `.github/ISSUE_TEMPLATE/`
  - [ ] **[P2-06b]** Criar template de Pull Request (`PULL_REQUEST_TEMPLATE.md`) no `.github/` (alinhado com a DoD).
  - [ ] **[P2-06c]** Refinar o `CONTRIBUTING.md` com guias de estilo de código e processo de revisão.
- [ ] **[P2-07]** Criar o workflow `.github/workflows/deploy_gh_pages.yml` para publicar automaticamente o site do MkDocs (do /docs) no GitHub Pages.

### ⚪ P3 — Futuro (Comunidade e Expansão)

- [ ] **[P3-01]** Implementar benchmarking de prompts (/benchmarks/).
- [ ] **[P3-02]** (Ver P2-07) Refinar e expandir o portal GitHub Pages com temas e busca.
- [ ] **[P3-03]** Adicionar logs de progresso de estudantes.
- [ ] **[P3-04]** Permitir integração com outras IAs (LangChain, CrewAI, etc.).
- [ ] **[P3-05]** Adicionar mentor de voz (TTS) experimental.
- [ ] **[P3-06]** Iniciar diretório de casos de sucesso e exemplos da comunidade.

---

## Métricas de Sucesso

- **Adoção:** quantidade de forks e stars no GitHub.  
- **Confiabilidade:** consistência das respostas em testes de prompt.  
- **Utilidade:** número de projetos guiados criados pela comunidade.  
- **Didática:** clareza e padronização das respostas.  
- **Evolução:** número de contribuições externas (PRs aceitos).

---

## Licença

MIT License — uso livre e aberto com atribuição ao autor original.

---

## Contato e Governança

- Repositório: github.com/SEU_USUARIO/prompt-mentor
- Comunidade: em construção  
- Canal de contribuições: via Pull Requests e Issues documentadas.

---
