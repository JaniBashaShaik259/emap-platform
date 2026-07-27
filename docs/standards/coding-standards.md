
# Coding Standards

## Objective

This document defines development standards for EMAP.

---

# General Principles

- Write readable code.
- Avoid duplication.
- Reuse existing components.
- Document business logic.
- Never hardcode secrets.

---

# SQL Standards

- Use uppercase SQL keywords.
- Use meaningful aliases.
- Avoid SELECT *.
- Always specify schema names.
- Use stored procedures where appropriate.

---

# Notebook Standards

- One notebook = one responsibility.
- Parameterize notebooks.
- Use Markdown cells for documentation.
- Log execution details.

---

# Pipeline Standards

- Use parameters.
- Avoid duplicate pipelines.
- Log every execution.
- Handle failures gracefully.

---

# Python Standards

- Follow PEP 8.
- Use meaningful variable names.
- Add docstrings.
- Avoid global variables.

---

# Git Standards

- Use feature branches.
- Use pull requests.
- Use Conventional Commits.

Examples:

feat:

fix:

docs:

refactor:

test:

chore:

---

# Security Standards

- Store secrets in Azure Key Vault.
- Never commit credentials.
- Never expose API keys.

---

# Documentation

Every feature must include:

- Documentation
- Testing
- Git Commit
