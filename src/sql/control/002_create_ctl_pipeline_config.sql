CREATE OR REPLACE TABLE ctl_pipeline_config
(
    pipeline_id STRING,
    pipeline_name STRING,
    source_id INT,
    endpoint STRING,
    http_method STRING,
    target_table STRING,
    load_type STRING,
    schedule_type STRING,
    is_active BOOLEAN,
    created_date TIMESTAMP,
    created_by STRING,
    modified_date TIMESTAMP,
    modified_by STRING
);
