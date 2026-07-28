# SQL Scripts

This directory contains all SQL artifacts used by the EMAP platform.

## Folder Structure

| Folder | Purpose |
|---------|---------|
| control | DDL and DML for metadata/control tables |
| audit | DDL and DML for audit and logging tables |
| bronze | Bronze layer table definitions |
| silver | Silver layer table definitions |
| gold | Gold layer table definitions |
| warehouse | Warehouse objects (schemas, views, procedures) |

## Naming Convention

DDL scripts are prefixed with a sequence number to ensure deterministic execution order.

Example:

001_create_ctl_source_system.sql
002_create_ctl_pipeline_config.sql
003_create_ctl_entity_config.sql
