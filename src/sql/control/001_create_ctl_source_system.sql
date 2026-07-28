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
