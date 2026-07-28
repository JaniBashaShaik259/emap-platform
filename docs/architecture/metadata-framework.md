# Metadata Framework

## Overview

The Enterprise Market Analytics Platform (EMAP) uses a metadata-driven architecture to enable reusable, configurable, and scalable data ingestion pipelines.

Instead of hardcoding source-specific logic, all ingestion pipelines read their configuration from control tables stored in the Lakehouse.

This approach enables onboarding new source systems with minimal code changes.

---

# Design Principles

- Metadata-driven architecture
- Reusable pipelines
- Configuration over code
- Generic REST ingestion
- Centralized audit logging
- Extensible framework

---

# Metadata Architecture

```
                    +----------------------+
                    | ctl_source_system    |
                    +----------------------+
                               |
                               |
                               v
                    +----------------------+
                    | ctl_pipeline_config  |
                    +----------------------+
                               |
                               |
                               v
                    +----------------------+
                    | ctl_entity_config    |
                    +----------------------+
                               |
                               |
                               v
                  Generic REST Fabric Pipeline
                               |
                               |
                               v
                         Processing Notebook
                               |
                               |
                               v
                         Bronze Delta Tables
                               |
                               |
                               v
                     audit_pipeline_run
```

---

# Metadata Tables

## 1. ctl_source_system

### Purpose

Stores the master list of all source systems supported by the platform.

### Current Columns

| Column |
|----------|
| source_id |
| source_name |
| source_code |
| source_category |
| source_type |
| base_url |
| auth_type |
| description |
| is_active |
| created_date |
| created_by |
| modified_date |
| modified_by |

### Current Status

✅ Implemented

---

## 2. ctl_pipeline_config

### Purpose

Stores ingestion pipeline configuration.

The pipeline determines:

- Which source to execute
- Which endpoint to call
- Which target table to load
- Load strategy

### Current Columns

| Column |
|----------|
| pipeline_id |
| pipeline_name |
| source_id |
| endpoint |
| http_method |
| target_table |
| load_type |
| schedule_type |
| is_active |
| created_date |
| created_by |
| modified_date |
| modified_by |

### Current Status

✅ Implemented

---

## 3. ctl_entity_config

### Purpose

Stores business entities processed by pipelines.

Examples include:

- Stocks
- Cryptocurrencies
- Commodities
- Forex pairs

### Current Columns

| Column |
|----------|
| entity_id |
| source_id |
| entity_type |
| entity_code |
| entity_name |
| entity_group |
| exchange_code |
| is_active |
| created_date |
| created_by |
| modified_date |
| modified_by |

### Current Status

✅ Table Created

⏳ Metadata Seeding Pending

---

## 4. audit_pipeline_run

### Purpose

Stores execution history for every pipeline run.

### Current Columns

| Column |
|----------|
| run_id |
| pipeline_name |
| source_name |
| start_time |
| end_time |
| duration_seconds |
| trigger_type |
| status |
| rows_read |
| rows_loaded |
| error_message |
| created_date |

### Current Status

✅ Implemented

---

# Metadata Flow

```
ctl_source_system
        │
        ▼
ctl_pipeline_config
        │
        ▼
ctl_entity_config
        │
        ▼
Fabric Pipeline
        │
        ▼
Notebook
        │
        ▼
Bronze Layer
        │
        ▼
audit_pipeline_run
```

---

# Current Phase

## Phase 1

Completed

- ctl_source_system
- ctl_pipeline_config
- ctl_entity_config
- audit_pipeline_run

---

# Future Phases

## Phase 2

- ctl_watermark
- ctl_column_mapping
- ctl_api_headers
- ctl_api_parameters

## Phase 3

- audit_error_log
- audit_reconciliation
- audit_data_quality

## Phase 4

- ctl_snapshot_config
- ctl_notification_config
- ctl_reconciliation_rules
- ctl_data_quality_rules

---

# Design Decisions

- One Lakehouse per business domain
- Metadata stored in the same Lakehouse as business data
- Logical separation using naming prefixes
- Generic pipelines read metadata instead of hardcoded values
- Fabric Pipelines perform orchestration
- Notebooks perform processing
- Audit information is captured for every execution

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| Metadata Framework | ✅ |
| Source Configuration | ✅ |
| Pipeline Configuration | ✅ |
| Entity Configuration | ✅ Table Created |
| Audit Framework | ✅ |
| Generic Pipeline | ⏳ Planned |
