# Technology Stack

## Overview

The Enterprise Market Analytics Platform (EMAP) is built using Microsoft Fabric and follows a modern Lakehouse architecture with metadata-driven ingestion.

---

# Core Platform

| Component | Technology |
|-----------|------------|
| Analytics Platform | Microsoft Fabric |
| Storage | OneLake |
| Lakehouse | Fabric Lakehouse |
| Data Warehouse | Fabric Warehouse |
| Version Control | GitHub |
| CI/CD | GitHub Actions (Planned) |
| Deployment | Fabric Deployment Pipelines (Planned) |

---

# Data Processing

| Component | Technology |
|-----------|------------|
| Orchestration | Fabric Pipelines |
| Data Processing | Fabric Notebooks |
| Language | PySpark |
| SQL Development | Spark SQL / T-SQL (Warehouse) |

---

# Storage Architecture

| Layer | Prefix |
|-------|--------|
| Control | ctl_ |
| Audit | audit_ |
| Bronze | br_ |
| Silver | sl_ |
| Gold | gd_ |

---

# Metadata Framework

Current Tables

| Table |
|-------|
| ctl_source_system |
| ctl_pipeline_config |
| ctl_entity_config |
| audit_pipeline_run |

Future Tables

- ctl_watermark
- ctl_api_headers
- ctl_api_parameters
- ctl_column_mapping
- ctl_snapshot_config
- ctl_data_quality_rules
- audit_error_log
- audit_reconciliation

---

# Source Systems

Current

- Yahoo Finance REST API

Future

- News API
- Reddit API
- SEC EDGAR
- SQL Server
- CSV Files
- Azure Storage

---

# Security

Current

- Public REST API

Future

- Azure Key Vault
- Managed Identity
- OAuth
- API Keys

---

# Development Tools

| Tool | Purpose |
|------|----------|
| GitHub | Source Control |
| Visual Studio Code | Local Development |
| Microsoft Fabric | Data Platform |
| Git | Version Control |

---

# Testing

Future

- Unit Testing
- Integration Testing
- Data Validation
- Reconciliation
- End-to-End Testing

---

# Monitoring

Current

- audit_pipeline_run

Future

- Fabric Monitoring
- Pipeline Dashboard
- Data Quality Dashboard
- Operational Dashboard

---

# Design Principles

- Metadata-driven architecture
- Configuration over code
- Reusable pipelines
- Separation of orchestration and processing
- Enterprise naming conventions
- Git-first development
- CI/CD-ready solution
