-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "411ccd07-679c-42f8-920d-149693c3a239",
-- META       "default_lakehouse_name": "lh_market",
-- META       "default_lakehouse_workspace_id": "f8b434ab-5f87-42e7-995a-7913dd0a3abf",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "411ccd07-679c-42f8-920d-149693c3a239"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Welcome to your new notebook
-- Type here in the cell editor to add code!


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

-- MAGIC %%pyspark
-- MAGIC import notebookutils
-- MAGIC 
-- MAGIC 


-- METADATA ********************

-- META {
-- META   "language": "python",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

-- MAGIC %%pyspark
-- MAGIC # Get your actual signed-in account email
-- MAGIC user_email = notebookutils.env.


-- METADATA ********************

-- META {
-- META   "language": "python",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

# Save it to a Spark configuration variable
spark.conf.set("my_current_user", user_email)

print(f"Logged in as: {user_email}")

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************


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
    SESSION_USER
);


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

SELECT CURRENT_USER;

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

-- MAGIC %%sql
-- MAGIC INSERT INTO ctl_pipeline_config (
-- MAGIC     pipeline_id,
-- MAGIC     pipeline_name,
-- MAGIC     source_id,
-- MAGIC     endpoint,
-- MAGIC     http_method,
-- MAGIC     target_table,
-- MAGIC     load_type,
-- MAGIC     schedule_type,
-- MAGIC     is_active,
-- MAGIC     created_date,
-- MAGIC     created_by
-- MAGIC ) VALUES (
-- MAGIC     'PL001',
-- MAGIC     'pl_rest_ingest',
-- MAGIC     1,                             -- Maps back to Yahoo Finance API in ctl_source_system
-- MAGIC     '/v8/finance/chart',           -- yfinance internal API endpoint reference
-- MAGIC     'GET',
-- MAGIC     'br_stock_prices',
-- MAGIC     'FULL',
-- MAGIC     'MANUAL',
-- MAGIC     1,
-- MAGIC     current_timestamp(),
-- MAGIC     'SparkSQL_User'
-- MAGIC );


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

CREATE TABLE ctl_entity_config
(
    entity_id INT,
    source_id INT,
    entity_type STRING,
    entity_code STRING,
    entity_name STRING,
    entity_group STRING,
    exchange_code STRING,
    is_active BOOLEAN,
    created_date TIMESTAMP,
    created_by STRING,
    modified_date TIMESTAMP,
    modified_by STRING
);

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

-- MAGIC %%sql
-- MAGIC INSERT INTO ctl_entity_config (
-- MAGIC     source_id,
-- MAGIC     entity_type,
-- MAGIC     entity_code,
-- MAGIC     entity_name,
-- MAGIC     entity_group,
-- MAGIC     exchange_code,
-- MAGIC     is_active,
-- MAGIC     created_date,
-- MAGIC     created_by
-- MAGIC ) VALUES 
-- MAGIC (1, 'Stock', 'AAPL', 'Apple Inc.', 'US_Equities', 'NASDAQ', 1, current_timestamp(), 'SparkSQL_User'),
-- MAGIC (1, 'Stock', 'MSFT', 'Microsoft Corporation', 'US_Equities', 'NASDAQ', 1, current_timestamp(), 'SparkSQL_User'),
-- MAGIC (1, 'Stock', 'NVDA', 'NVIDIA Corporation', 'US_Equities', 'NASDAQ', 1, current_timestamp(), 'SparkSQL_User'),
-- MAGIC (1, 'Crypto', 'BTC-USD', 'Bitcoin USD', 'Cryptocurrency', 'CCY', 1, current_timestamp(), 'SparkSQL_User');


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

-- MAGIC %%sql
-- MAGIC SELECT 
-- MAGIC     s.source_name,
-- MAGIC     p.pipeline_name,
-- MAGIC     p.target_table,
-- MAGIC     e.entity_code AS ticker,
-- MAGIC     e.entity_group,
-- MAGIC     e.exchange_code
-- MAGIC FROM ctl_pipeline_config p
-- MAGIC INNER JOIN ctl_source_system s ON p.source_id = s.source_id
-- MAGIC INNER JOIN ctl_entity_config e ON p.source_id = e.source_id
-- MAGIC WHERE p.is_active = true 
-- MAGIC   AND e.is_active = true;


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
