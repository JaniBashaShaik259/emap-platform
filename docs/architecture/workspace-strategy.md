# Workspace Strategy

## Overview

The Enterprise Market Analytics Platform (EMAP) follows an environment-based workspace strategy in Microsoft Fabric.

Each environment is isolated in its own workspace to support controlled development, testing, and production deployments.

---

# Workspace Architecture

```
                    Microsoft Fabric

        +-------------------------------+
        |         EMAP-DEV              |
        | Development Workspace         |
        +-------------------------------+
                    |
                    | Deployment Pipeline
                    |
                    ▼
        +-------------------------------+
        |        EMAP-TEST              |
        | Testing Workspace            |
        +-------------------------------+
                    |
                    | Deployment Pipeline
                    |
                    ▼
        +-------------------------------+
        |        EMAP-PROD              |
        | Production Workspace         |
        +-------------------------------+
```

---

# Environment Purpose

## EMAP-DEV

Purpose

Development and experimentation.

Current Status

✅ Active

Contains

- Lakehouse
- Warehouse
- Metadata Framework
- Pipelines (Future)
- Notebooks (Future)

---

## EMAP-TEST

Purpose

Integration testing and user acceptance testing.

Status

⏳ Planned

---

## EMAP-PROD

Purpose

Production workloads.

Status

⏳ Planned

---

# Workspace Naming Convention

| Environment | Workspace Name |
|-------------|----------------|
| Development | EMAP-DEV |
| Testing | EMAP-TEST |
| Production | EMAP-PROD |

---

# Git Integration Strategy

The Development workspace will be connected to the GitHub repository.

Branch Mapping

| Workspace | Git Branch |
|-----------|------------|
| EMAP-DEV | develop |
| EMAP-TEST | Release Deployment |
| EMAP-PROD | Release Deployment |

Development will occur in feature branches and be merged into the `develop` branch before deployment.

---

# Deployment Strategy

Development

↓

GitHub Pull Request

↓

Develop Branch

↓

Fabric Deployment Pipeline

↓

EMAP-TEST

↓

Approval

↓

EMAP-PROD

---

# Current Workspace Artifacts

## Lakehouse

- lh_market

## Warehouse

- wh_reporting

Future

- Pipelines
- Notebooks
- Environment
- Reports
- Semantic Model

---

# Design Decisions

- One workspace per environment
- One Lakehouse per business domain
- One Warehouse per business domain
- Git integration enabled only for the development workspace
- CI/CD will promote artifacts to Test and Production
