CREATE OR REPLACE TABLE audit_pipeline_run
(
    run_id STRING,
    pipeline_name STRING,
    source_name STRING,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    duration_seconds INT,
    trigger_type STRING,
    status STRING,
    rows_read INT,
    rows_loaded INT,
    error_message STRING,
    created_date TIMESTAMP
);
