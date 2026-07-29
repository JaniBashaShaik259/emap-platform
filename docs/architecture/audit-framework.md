# Audit Framework

## Purpose

The Audit Framework records operational metadata for every pipeline execution.

It provides traceability, monitoring, troubleshooting, reconciliation, and operational reporting.

---

## Design Principles

- Metadata-driven
- Reusable
- Layer independent
- Spark-based writes
- Delta Lake storage
- Centralized logging

---

## Audit Table

audit_pipeline_run

Stores:

- Run ID
- Pipeline Name
- Notebook Name
- Source Code
- Entity Code
- Layer
- Load Type
- Start Time
- End Time
- Duration
- Rows Read
- Rows Loaded
- Rows Rejected
- Status
- Error Message
- File Path

---

## Logging Process

Pipeline

↓

Notebook Starts

↓

Capture Start Time

↓

Execute Processing

↓

Calculate Metrics

↓

Call Logging Utility

↓

Delta Merge

↓

Audit Table Updated

---

## Logging Strategy

Instead of executing SQL INSERT statements, the framework writes audit information using Spark DataFrames and Delta Merge operations.

This approach aligns with Microsoft Fabric Lakehouse capabilities while maintaining transactional consistency.

---

## Reusability

The same logging mechanism will be reused by:

- REST Ingestion
- Bronze → Silver
- Silver → Gold
- Snapshot Pipelines
- Reconciliation Framework
- Data Quality Framework

---

## Future Enhancements

- Audit Summary Views
- Pipeline Performance Dashboard
- SLA Monitoring
- Retry History
- Alert Notifications
- Execution Trend Reports
