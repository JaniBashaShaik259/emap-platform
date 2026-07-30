# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "411ccd07-679c-42f8-920d-149693c3a239",
# META       "default_lakehouse_name": "lh_market",
# META       "default_lakehouse_workspace_id": "f8b434ab-5f87-42e7-995a-7913dd0a3abf",
# META       "known_lakehouses": [
# META         {
# META           "id": "411ccd07-679c-42f8-920d-149693c3a239"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

# --- PARAMETERS CELL ---
p_entity_code = "MSFT"  # This will be overridden by the pipeline later
p_pipeline_name = "pl_rest_ingest"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
import pandas as pd
from datetime import datetime
from pyspark.sql.functions import current_timestamp

print(f"🎬 Starting dynamic metadata run for Entity: {p_entity_code} using Pipeline: {p_pipeline_name}")

# 1. Query your Control Tables using Spark SQL to get paths dynamically
metadata_query = f"""
    SELECT 
        s.base_url, 
        p.endpoint, 
        p.target_table
    FROM ctl_pipeline_config p
    INNER JOIN ctl_source_system s ON p.source_id = s.source_id
    WHERE p.pipeline_name = '{p_pipeline_name}' 
      AND p.is_active = true
"""

# Fetch the metadata configuration row
meta_df = spark.sql(metadata_query).collect()

if not meta_df:
    raise Exception(f" No active metadata configuration found for pipeline: {p_pipeline_name}")

# Extract values from our metadata database row
base_url = meta_df[0]['base_url']
endpoint = meta_df[0]['endpoint']
target_table = meta_df[0]['target_table']

# 2. Dynamically build the full API connection link using metadata parameters
# This strips any accidental extra slashes and cleanly glues the target entity
target_url = f"{base_url.rstrip('/')}/{endpoint.strip('/')}/{p_entity_code}"

api_params = {"range": "1mo", "interval": "1d"}
api_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print(f" Dynamically built URL from metadata: {target_url}")

try:
    # 3. Execute the API Call
    response = requests.get(target_url, params=api_params, headers=api_headers, timeout=15)
    response.raise_for_status()
    json_data = response.json()

    # 4. Parse the standard Yahoo Finance nested structure
    result = json_data['chart']['result'][0]
    timestamps = result['timestamp']
    indicators = result['indicators']['quote'][0]

    parsed_records = []
    for i in range(len(timestamps)):
        # Skip incomplete or missing trading days
        if indicators['close'][i] is None or indicators['open'][i] is None: 
            continue
        
        parsed_records.append({
            "Date": datetime.utcfromtimestamp(timestamps[i]).strftime('%Y-%m-%d'),
            "Ticker": p_entity_code,
            "Open": float(indicators['open'][i]),
            "High": float(indicators['high'][i]),
            "Low": float(indicators['low'][i]),
            "Close": float(indicators['close'][i]),
            "Volume": int(indicators['volume'][i])
        })

    # 5. Write to the target table defined in the metadata table
    if parsed_records:
        spark_df = spark.createDataFrame(pd.DataFrame(parsed_records))
        spark_df = spark_df.withColumn("IngestedAt", current_timestamp())
        
        # Saves directly to whatever target_table says (e.g. 'bronze_stock_prices')
        spark_df.write \
            .mode("append") \
            .format("delta") \
            .saveAsTable(target_table)
        print(f"Success! Data for {p_entity_code} written to metadata target table: {target_table}")
    else:
        print(f" No records found for entity: {p_entity_code}")

except Exception as e:
    print(f"Error during metadata run: {str(e)}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM lh_market.dbo.br_stock_prices LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
