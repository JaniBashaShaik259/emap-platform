# Notebook Framework

## Purpose

All processing logic resides inside Microsoft Fabric Notebooks.

Pipelines only orchestrate execution.

---

## Notebook Responsibilities

- Read metadata
- Read source data
- Validate schema
- Apply transformations
- Write data
- Update audit logs

---

## Naming Convention

NB_<Layer>_<Purpose>

Examples

NB_BRZ_API_INGEST

NB_SLV_STANDARDIZE

NB_GLD_BUILD_CUSTOMER

---

## Design Principles

- Reusable

- Parameterized

- Modular

- Exception Handling

- Logging

- Metadata Driven
