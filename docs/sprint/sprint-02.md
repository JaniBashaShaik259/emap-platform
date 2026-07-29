
# Sprint 02

## Sprint Goal

Build the first end-to-end ingestion pipeline using Yahoo Finance.

---

## Planned Stories

- Create Fabric Workspace
- Create Bronze Lakehouse
- Build REST Pipeline
- Load Yahoo Finance Data
- Validate Data Load
- Store Raw Data

---

## Deliverables

- Bronze Lakehouse
- REST Pipeline
- Initial Notebook
- Audit Logging
- Documentation

---

## Definition of Done

- Data loaded successfully
- Pipeline reusable
- Documentation updated
- Code committed

# Sprint 02

## Goal

Build the metadata-driven ingestion framework.

---

## User Stories

Story 1

Connect GitHub repository with Fabric Workspace.

Status

Not Started

---

Story 2

Create Bronze Lakehouse folder structure.

Status

Not Started

---

Story 3

Create generic ingestion notebook.

Status

Not Started

---

Story 4

Create metadata-driven Pipeline.

Status

Not Started

---

Story 5

Ingest first API source.

Status

Not Started

---

Story 6

Implement pipeline logging.

Status

Not Started

Sprint 2 Deliverables

By the end of this sprint, you'll have:

GitHub
     │
     ▼
Fabric Pipeline
     │
     ▼
Read Control Metadata
     │
     ▼
ForEach Entity
     │
     ▼
Notebook
     │
     ▼
REST API
     │
     ▼
Bronze Lakehouse
     │
     ▼
Audit Log

---
## Story 7 – Audit Logging Framework

### Objective

Implement a reusable audit logging framework capable of recording execution metadata for all Fabric notebooks and pipelines.

### Implementation

- Created audit_pipeline_run table
- Implemented reusable logging utility notebook
- Used Spark DataFrame writes
- Used Delta Merge for UPSERT operations
- Recorded execution metrics
- Recorded processing status
- Recorded row counts
- Recorded execution duration

### Design Decision

Since Microsoft Fabric Lakehouse SQL Endpoints are optimized for analytical querying and are not intended for transactional write operations, audit logging is implemented using Spark Delta Merge statements.

This design avoids unnecessary dependency on Fabric Warehouse while remaining scalable and production-ready.

### Status

Completed
