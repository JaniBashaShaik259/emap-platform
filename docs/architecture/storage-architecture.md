# Storage Architecture

## Workspace

EMAP-DEV

---

## Lakehouse

lh_market

Purpose:

Store all raw, curated, business, metadata, and audit tables.

---

## Warehouse

wh_reporting

Purpose:

Business reporting layer.

---

## Logical Data Layers

| Layer | Purpose |
|---------|----------|
| Control | Metadata and configuration |
| Audit | Logging and reconciliation |
| Bronze | Raw source data |
| Silver | Cleaned and standardized data |
| Gold | Business-ready analytical data |

---

## Design Decisions

- One workspace per environment.
- One Lakehouse per business domain.
- One Warehouse per domain.
- Logical separation using schemas or naming conventions.
- Metadata and audit tables remain inside the same Lakehouse.
