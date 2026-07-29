# Fabric Git Integration

## Objective

Integrate Microsoft Fabric with GitHub to enable version control, collaboration, and CI/CD.

---

## Repository

Repository Name:
emap-platform

Branch:
develop

Git Folder:
fabric/

---

## Connected Workspace

Workspace:
EMAP-DEV

Type:
Development Workspace

---

## Git Strategy

- main
    Production

- develop
    Active development

- feature/*
    Individual features

- release/*
    Release stabilization

- hotfix/*
    Production fixes

---

## Fabric Artifacts

The following artifacts are version controlled:

- Lakehouses
- Warehouse
- Data Pipelines
- Notebooks
- Semantic Models
- Reports

---

## Synchronization

Changes in Fabric are committed to GitHub.

Changes from GitHub are synchronized back into the Fabric workspace.

---

## Benefits

- Version history
- Collaboration
- Rollback capability
- Pull Requests
- CI/CD deployment