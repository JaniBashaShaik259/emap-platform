# ADR-003: Audit Logging Strategy

## Status

Accepted

---

## Date

2026-07-29

---

## Context

The EMAP platform requires an enterprise-grade audit framework to capture execution metadata for all ingestion, transformation, reconciliation, and reporting pipelines.

Audit information includes:

- Pipeline execution status
- Notebook execution details
- Source and entity information
- Record counts
- Processing duration
- Error messages
- File locations

Initially, the audit tables were designed in the Lakehouse SQL Endpoint.

---

## Problem

Microsoft Fabric Lakehouse SQL Endpoints are optimized for analytical querying and currently provide read-only SQL capabilities for Delta tables.

This prevents traditional transactional INSERT and UPDATE operations from being executed directly through SQL.

Since audit logging requires frequent write operations, using SQL statements against the Lakehouse SQL Endpoint is not suitable.

Migrating the audit framework to a Fabric Warehouse would solve the issue but would introduce additional complexity and consume Warehouse resources that are unnecessary during the Development phase.

---

## Decision

The audit framework will remain in the Lakehouse.

Audit records will be written using Spark DataFrame operations and Delta Merge statements executed from a reusable utility notebook.

The reusable logging notebook will be invoked by all processing notebooks.

---

## Architecture

Pipeline

↓

Notebook

↓

Utility Logging Notebook

↓

Spark Delta Merge

↓

Audit Delta Table

---

## Benefits

- No dependency on Warehouse for transactional logging
- Uses native Delta Lake capabilities
- Fully compatible with Microsoft Fabric Lakehouse architecture
- Reusable across all pipelines
- Supports UPSERT operations
- Easily extensible
- Production-ready design

---

## Consequences

Positive

- Centralized audit framework
- Reusable implementation
- Better scalability
- Consistent logging across all notebooks

Negative

- Audit writes must be implemented through Spark instead of SQL
- Slightly more implementation effort than direct SQL INSERT statements

---

## Future Enhancements

- Central Logging Notebook
- Logging Utility Functions
- Pipeline Execution Dashboard
- Monitoring Reports
- Alert Framework
- Retry Logging
- Execution Metrics
