# Pipeline Framework

## Purpose

The EMAP platform uses Microsoft Fabric Pipelines as the orchestration engine.

Pipelines are responsible for:

- Reading metadata
- Orchestrating notebook execution
- Logging execution
- Triggering notifications
- Managing retries
- Handling failures

No transformation logic is implemented inside Pipelines.

Business logic always resides inside Notebooks.

---

## Pipeline Layers

### Control

Responsible for metadata.

Example

PL_CTL_METADATA_ORCHESTRATOR

---

### Bronze

Responsible for ingestion.

Example

PL_BRZ_INGEST_GENERIC

---

### Silver

Responsible for cleansing.

Example

PL_SLV_STANDARDIZE_CUSTOMER

---

### Gold

Responsible for business models.

Example

PL_GLD_BUILD_FACT_SALES

---

## Design Principles

- Metadata Driven
- Reusable
- Idempotent
- Configurable
- Environment Agnostic
- Auditable