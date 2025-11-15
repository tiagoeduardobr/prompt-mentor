# Prompt Mentor: Engenharia de Software e Projetos

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square">
  <img alt="Python Version" src="https://img.shields.io/badge/python-3.8%2B-blueviolet?style=flat-square">
  <img alt="Poetry" src="https://img.shields.io/badge/poetry-gerenciamento-darkgreen?style=flat-square">
</p>

*Nota: Badges de CI e cobertura serão ativados conforme o projeto avança (atualmente em fundação).*

## 1. Descrição

O **Prompt Mentor** é um framework open-source de engenharia de prompt que simula um **mentor sênior de engenharia de software**. Ele guia estudantes e desenvolvedores juniores através de projetos full-stack, enfatizando boas práticas, segurança (OWASP Top 10), testes automatizados e workflow profissional (Git, CI/CD), sem gerar código diretamente — em vez disso, ensina o processo de criação.

## 2. Tecnologias Utilizadas (Tech Stack)

- **Linguagem:** Python 3.8+
- **CLI:** Typer (interface principal)
- **LLM Providers:** OpenAI GPT, Google Generative AI (configurável via .env)
- **Gerenciamento de Dependências:** Poetry
- **Testes:** Pytest, Pytest-Cov
- **Qualidade e Segurança:** Black, Flake8, iSort, Bandit, Safety
- **Versionamento:** Git/GitHub (commits semânticos, branches feature)
- **CI/CD:** GitHub Actions (planejado)
- **Documentação:** MkDocs (planejado)

## 3. Instalação e Configuração

### Pré-requisitos

- Python 3.8+ instalado
- Poetry para gerenciamento de dependências
- Conta em provedor LLM (OpenAI ou Google) para obter API keys seguras

### Passos de Instalação

1 Clone o repositório:

```bash
   git clone https://github.com/tiagoeduardobr/prompt-mentor.git
   cd prompt-mentor
```

2 Configure variáveis de ambiente seguras:

```bash
   cp .env.example .env
```

*Preencha as variáveis no `.env` com suas chaves API (ex: OPENAI_API_KEY). Nunca commite este arquivo.*

3 Instale as dependências com Poetry:

```bash
   poetry install
```

4 Ative o ambiente virtual:

```bash
   poetry shell
```

5 (Atualmente CLI-only) Teste a configuração:

```bash
    poetry run python -c "print('Configuração completa. Aguarde futuras versões para CLI interativa.')"
```

## 4. Testes

Execute os testes para validar a configuração:

```bash
    poetry run pytest
```

Para relatório de cobertura:

```bash
    poetry run pytest --cov
```

## 5. Funcionalidades

- **Mentoria Guiada:** Respostas estruturadas com exemplos, diffs e commits simulados.
- **Foco Educacional:** Ensina engenharia, não apenas código (qualidade > velocidade).
- **Segurança por Padrão:** Validação OWASP, hashing de senhas, sanitização de entradas.
- **Configurável:** Suporte a OpenAI e Google AI via YAML.
- **Profissional:** Workflow Git real, testes obrigatórios, documentação.

## 6. Segurança

O projeto segue OWASP Top 10, com verificações automáticas (Bandit, Safety). Segredos são gerenciados via .env e nunca hardcoded. Contribuições passam por análise de segurança.

## 7. Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 8. Contribuição

Contribuições são bem-vindas! Veja o `CONTRIBUTING.md` para guias detalhados de desenvolvimento e configuração.

## 9. Status do Projeto

Este projeto está em **fase de fundação (P0 concluído até P0-06)**. Estrutura base (guia, config, README, .gitignore) estabelecida. Próximos passos: Poetry, estrutura de diretórios, testes expandidos.

Para backlog completo e roadmap, veja o `PROJECT_INIT.md`.

## 10. Roadmap

- **Fase 1 (P0 - Atual):** Fundação (guia, config, estrutura).
- **Fase 2 (P1):** Specializations, testes avançados, abstração LLM.
- **Fase 3 (P2):** CLI completa, workflows CI/CD, Docker.
- **Fase 4 (P3):** Projetos guiados, comunidade.

## 11. Suporte e Contato

Para dúvidas, abra uma issue no [GitHub](https://github.com/tiagoeduardobr/prompt-mentor/issues) ou consulte o `PROJECT_INIT.md`. Contato: tiagoeduardobr (via GitHub).

---

*README atualizado para refletir o estado atual (CLI em desenvolvimento, foco em mentoria).*

## 12. Agradecimentos

Inspirado em práticas de engenharia de software open-source. Obrigado à comunidade por contribuições futuras!
