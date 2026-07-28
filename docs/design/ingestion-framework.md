# Ingestion Framework

## Overview

The Enterprise Market Analytics Platform (EMAP) follows a metadata-driven ingestion framework designed to support multiple source systems with minimal code changes.

The framework separates orchestration, processing, metadata management, and auditing into independent components.

The primary objective is to build reusable ingestion pipelines that can onboard new source systems through metadata rather than custom development.

---

# Design Principles

The ingestion framework is based on the following principles:

- Metadata-driven execution
- Configuration over code
- Reusable pipelines
- Separation of orchestration and processing
- Auditability
- Scalability
- Extensibility
- Idempotent processing
- Enterprise-ready architecture

---

# High-Level Architecture
               Source Systems

 REST APIs | SQL | Files | Streaming

                 │
                 ▼

        Fabric Pipeline (Orchestration)

                 │
                 ▼

        Read Control Metadata

                 │
                 ▼

     Determine Active Pipelines

                 │
                 ▼

      Determine Active Entities

                 │
                 ▼

      Execute Processing Notebook

                 │
                 ▼

         Source Data Extraction

                 │
                 ▼

         Data Validation

                 │
                 ▼

       Bronze Layer (Raw Data)

                 │
                 ▼

       Pipeline Audit Logging

---

# Framework Components

## Source Layer

Responsible for external systems.

Examples

- Yahoo Finance
- News API
- Reddit API
- SEC EDGAR
- SQL Databases
- CSV Files
- Azure Storage

---

## Metadata Layer

The framework is controlled using metadata.

### Control Tables

| Table | Purpose |
|---------|----------|
| ctl_source_system | Source system information |
| ctl_pipeline_config | Pipeline configuration |
| ctl_entity_config | Business entities |

Future metadata tables

- ctl_watermark
- ctl_column_mapping
- ctl_api_headers
- ctl_api_parameters
- ctl_snapshot_config
- ctl_data_quality_rules

---

## Orchestration Layer

Technology

Microsoft Fabric Pipeline

Responsibilities

- Read metadata
- Determine execution order
- Iterate through entities
- Execute notebooks
- Handle scheduling
- Handle retries
- Pass runtime parameters
- Write audit logs

---

## Processing Layer

Technology

Microsoft Fabric Notebook

Responsibilities

- Connect to source system
- Retrieve data
- Parse response
- Validate response
- Standardize data
- Write Bronze tables
- Return execution metrics

---

## Storage Layer

Technology

Microsoft Fabric Lakehouse

Logical Layers

| Layer | Prefix |
|---------|---------|
| Control | ctl_ |
| Audit | audit_ |
| Bronze | br_ |
| Silver | sl_ |
| Gold | gd_ |

---

# Metadata Driven Execution

The ingestion pipeline never contains source-specific logic.

Execution is controlled through metadata.

Example
Read ctl_pipeline_config

↓

Find active pipelines

↓

Read ctl_source_system

↓

Get source information

↓

Read ctl_entity_config

↓

Loop through active entities

↓

Execute notebook

↓

Load Bronze

↓

Write audit


---

# Runtime Parameters

The Fabric Pipeline passes runtime parameters to the notebook.

| Parameter | Description |
|------------|-------------|
| pipeline_id | Pipeline identifier |
| source_id | Source identifier |
| source_name | Source system |
| endpoint | REST endpoint |
| entity_code | Business entity |
| target_table | Bronze destination |
| pipeline_run_id | Unique execution identifier |

Future parameters

- watermark
- load_type
- api_key
- retry_count

---

# Processing Flow
Start

↓

Read Metadata

↓

Validate Metadata

↓

Read Source

↓

Validate Response

↓

Transform

↓

Load Bronze

↓

Return Metrics

↓

Update Audit

↓

Complete

---

# Error Handling Strategy

Current Phase

- Stop execution on failure
- Capture error message
- Update audit table

Future Enhancements

- Retry framework
- Dead-letter handling
- Email notifications
- Teams notifications
- Error log table
- Automatic recovery

---

# Logging Strategy

Every execution must be logged.

Current

audit_pipeline_run

Future

audit_pipeline_activity

audit_error_log

audit_reconciliation

audit_data_quality

---

# Data Validation

Phase 1

- API availability
- HTTP response code
- Empty response validation

Future

- Schema validation
- Duplicate detection
- Null checks
- Business rule validation
- Data quality framework

---

# Load Strategy

Current

Full Load

Future

- Incremental Load
- Watermark Processing
- Change Data Capture (CDC)
- Snapshot Loading

---

# Reconciliation Strategy

Future implementation

Pipeline reconciliation will compare:

Source Record Count

↓

Rows Read

↓

Rows Loaded

↓

Rows Rejected

↓

Final Status

Results will be stored in reconciliation audit tables.

---

# Snapshot Strategy

Future implementation

Selected entities will support Point-in-Time snapshots.

Example
Portfolio

2026-07-28

↓

Portfolio Snapshot

↓

Historical Analysis

---

# Security Strategy

Secrets will never be stored inside notebooks.

Authentication will use:

- Azure Key Vault
- Managed Identity (where applicable)
- Metadata-driven authentication configuration

Future support

- OAuth
- API Keys
- Basic Authentication
- Bearer Tokens

---

# Monitoring Strategy

Current

- audit_pipeline_run

Future

- Pipeline dashboards
- Execution history
- Success rate
- Failure analysis
- Performance metrics

---

# CI/CD Strategy

Source Control

GitHub

Development Flow
Feature Branch

↓

Pull Request

↓

Develop Branch

↓

Main Branch

↓

Deploy DEV

↓

Deploy TEST

↓

Deploy PROD

Deployment automation

- GitHub Actions
- Microsoft Fabric Deployment Pipelines

---

# Future Roadmap

## Phase 1

✅ Metadata Framework

✅ Control Tables

✅ Audit Framework

✅ Generic Architecture

---

## Phase 2

- Generic REST Pipeline
- Notebook Processing
- Bronze Ingestion

---

## Phase 3

- Silver Layer
- Gold Layer
- Data Quality Framework
- Watermark Framework

---

## Phase 4

- Reconciliation Framework
- Snapshot Framework
- Azure Key Vault
- Azure Functions
- Notification Framework

---

## Phase 5

- CI/CD
- Test Environment
- Production Environment
- Monitoring Dashboards
- Performance Optimization

---

# Guiding Principle

> **Build the platform once. Onboard new data sources through metadata, not by creating new pipelines.**

Every architectural decision in EMAP should support reusability, maintainability, and scalability while minimizing code changes.
