CREATE OR REPLACE TABLE ctl_source_system
(
    source_id INT,
    source_name STRING,
    source_code STRING,
    source_category STRING,
    source_type STRING,
    base_url STRING,
    auth_type STRING,
    description STRING,
    is_active BOOLEAN,
    created_date TIMESTAMP,
    created_by STRING,
    modified_date TIMESTAMP,
    modified_by STRING
);

GO


INSERT INTO ctl_source_system (
    source_id,
    source_name,
    source_code,
    source_category,
    source_type,
    base_url,
    auth_type,
    description,
    is_active,
    created_date,
    created_by
) VALUES (
    1,
    'Yahoo Finance API',
    'YFINANCE',
    'Financial Market Data',
    'Python API Web Scraper',
    'https://yahoo.com',
    'None',
    'Public stock market data ingestion using the yfinance library',
    true,
    current_timestamp(),
    'SparkSQL_User'
);
