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
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

# --- PARAMETERS CELL ---
p_entity_code = "FEDFUNDS"  # Overridden by pipeline loop (e.g., GS2, CPIAUCSL)
p_source_id = 2

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

print(f"Starting FRED Ingestion for Metric: {p_entity_code} via Pipeline: {p_source_id}")

# 1. Fetch paths dynamically from the metadata framework
metadata_query = f"""
    SELECT 
        s.base_url, 
        p.endpoint, 
        p.target_table
    FROM ctl_pipeline_config p
    INNER JOIN ctl_source_system s ON p.source_id = s.source_id
    WHERE p.source_id = '{p_source_id}'
    AND s.is_active = 'true'
"""

meta_df = spark.sql(metadata_query).collect()

if not meta_df:
    raise Exception(f"No active metadata configuration found for pipeline: {p_source_id}")

base_url = meta_df[0]['base_url']
endpoint = meta_df[0]['endpoint']
target_table = meta_df[0]['target_table']

# 2. Configure FRED-specific API Parameters
target_url = f"{base_url.rstrip('/')}/{endpoint.strip('/')}"
api_headers = {"User-Agent": "Mozilla/5.0"}
api_params = {
    "series_id": p_entity_code,
    "api_key": "0e63015563dc1f2690953e2beebc1574",  # <--- Paste your real FRED API key string here
    "file_type": "json",
    "limit": 100  # Fetches the latest 100 historical data points
}

print(f"Hitting URL: {target_url} for Series Indicator: {p_entity_code}")

try:
    # 3. Execute HTTP Call
    response = requests.get(target_url, params=api_params, headers=api_headers, timeout=60)
    response.raise_for_status()
    json_data = response.json()
    
    # 4. Parse FRED's native flat JSON observation array
    observations = json_data.get('observations', [])
    parsed_records = []
    
    for obs in observations:
        # FRED returns '.' for missing days or holiday closures. Skip them safely.
        if obs['value'] == '.' or obs['value'] is None: 
            continue
            
        parsed_records.append({
            "Date": obs['date'],
            "Ticker": p_entity_code,
            "Value": float(obs['value'])
        })
        
    # 5. Write to the Target Table specified in Metadata
    if parsed_records:
        spark_df = spark.createDataFrame(pd.DataFrame(parsed_records))
        # Add tracking metadata column
        spark_df = spark_df.withColumn("IngestedAt", current_timestamp())
        
        # Saves to 'bronze_macro_indicators' dynamically based on metadata configuration
        spark_df.write \
            .mode("append") \
            .format("delta") \
            .saveAsTable(target_table)
            
        print(f"Success! Data for {p_entity_code} written to target table: {target_table}")
    else:
        print(f"No valid data points found in response for: {p_entity_code}")

except Exception as e:
    print(f"Ingestion process failed for {p_entity_code}: {str(e)}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
