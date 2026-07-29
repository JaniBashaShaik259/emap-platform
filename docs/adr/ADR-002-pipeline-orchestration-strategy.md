# ADR-002

## Title

Adoption of Fabric Pipelines for orchestration and Notebooks for data processing

---

## Status

Accepted

---

## Date

2026-07-28

---

## Context

The Enterprise Market Analytics Platform (EMAP) requires a scalable and maintainable ingestion framework capable of processing data from multiple source systems.

The orchestration layer must manage execution flow, metadata lookup, logging, retries, and scheduling, while the processing layer should focus solely on data extraction, transformation, and loading.

---

## Decision

The platform will separate orchestration from processing.

### Fabric Pipelines

Responsible for:

- Reading metadata
- Orchestrating workflow execution
- Executing notebooks
- Passing runtime parameters
- Logging execution status
- Handling retries
- Scheduling
- Error handling

### Notebooks

Responsible for:

- Calling REST APIs
- Reading source data
- Transforming data
- Writing to Lakehouse
- Returning execution metrics

---

## Rationale

This separation provides:

- Better maintainability
- Reusable notebooks
- Metadata-driven orchestration
- Easier testing
- Better monitoring
- Simpler CI/CD deployment
- Separation of responsibilities

---

## Consequences

### Advantages

- Generic orchestration
- Reusable processing logic
- Easier debugging
- Enterprise architecture
- Reduced duplication

### Disadvantages

- Slightly more initial development effort
- Parameter passing between pipeline and notebook

---

## Alternatives Considered

### Notebook-only solution

Rejected because notebooks become responsible for orchestration, scheduling, logging, and business logic, making them difficult to maintain.

### Pipeline-only solution

Rejected because Fabric pipelines are not designed for complex data transformations or JSON processing.

---

## Implementation

The architecture will follow this execution pattern.

Fabric Pipeline

↓

Read Metadata

↓

ForEach Source

↓

ForEach Entity

↓

Execute Notebook

↓

Notebook loads Bronze

↓

Pipeline updates Audit Tables

↓

Pipeline completes

# ADR-002

## Title

Fabric Pipelines for Orchestration

---

## Status

Accepted

---

## Context

The EMAP platform requires a centralized orchestration layer.

---

## Decision

Microsoft Fabric Pipelines will be used only for orchestration.

Business logic will be implemented inside Notebooks.

---

## Consequences

Advantages

- Reusable Pipelines
- Simpler Maintenance
- Metadata Driven
- Better Error Handling

Disadvantages

- Additional Notebook dependency