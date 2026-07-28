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

GO
INSERT INTO ctl_pipeline_config (
    pipeline_id,
    pipeline_name,
    source_id,
    endpoint,
    http_method,
    target_table,
    load_type,
    schedule_type,
    is_active,
    created_date,
    created_by
) VALUES (
    'PL001',
    'pl_rest_ingest',
    1,                             -- Maps back to Yahoo Finance API in ctl_source_system
    '/v8/finance/chart',           -- yfinance internal API endpoint reference
    'GET',
    'br_stock_prices',
    'FULL',
    'MANUAL',
    1,
    current_timestamp(),
    'SparkSQL_User'
);
