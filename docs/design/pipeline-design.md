
# Pipeline Design

## Objective

Design a reusable, metadata-driven ingestion framework for the Enterprise Market Analytics Platform (EMAP).

The framework should support multiple REST APIs without requiring new pipelines for every source.

---

# Design Principles

The pipeline must be:

- Metadata driven
- Reusable
- Parameterized
- Configurable
- Auditable
- Extensible

---

# High Level Flow

```
                Fabric Pipeline

                        │

                        ▼

           Read ctl_pipeline_config

                        │

                        ▼

            Read ctl_source_system

                        │

                        ▼

            Read ctl_entity_config

                        │

                        ▼

                For Each Entity

                        │

                        ▼

             Execute Notebook

                        │

                        ▼

              Call REST API

                        │

                        ▼

              Parse JSON Data

                        │

                        ▼

         Write Bronze Delta Table

                        │

                        ▼

        Return Status to Pipeline

                        │

                        ▼

       Update audit_pipeline_run
```

---

# Responsibilities

## Fabric Pipeline

Responsible for:

- Reading metadata
- Determining execution order
- Looping through entities
- Calling notebooks
- Passing parameters
- Logging execution
- Handling failures
- Scheduling

---

## Notebook

Responsible for:

- Calling REST APIs
- Reading JSON responses
- Validating responses
- Transforming data
- Writing Bronze tables
- Returning execution metrics

---

# Runtime Parameters

The pipeline will pass the following parameters to the notebook.

| Parameter | Description |
|------------|-------------|
| source_id | Source identifier |
| source_name | Source system |
| endpoint | REST endpoint |
| entity_code | Business entity |
| target_table | Bronze table |
| pipeline_run_id | Execution identifier |

---

# Metadata Dependencies

The pipeline depends on:

- ctl_source_system
- ctl_pipeline_config
- ctl_entity_config

---

# Audit Framework

Every execution must insert a record into:

audit_pipeline_run

The pipeline is responsible for updating:

- Start Time
- End Time
- Status
- Rows Read
- Rows Loaded
- Error Message

---

# Error Handling

Future implementation will support:

- Retry logic
- Dead-letter handling
- Notification framework
- Error logging

---

# Future Enhancements

Phase 2

- Authentication metadata
- API headers
- Dynamic query parameters
- Watermark framework

Phase 3

- Reconciliation framework
- Snapshot framework
- Data quality rules
- Notification framework

Phase 4

- Multi-source orchestration
- Parallel execution
- Event-driven ingestion
