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
p_run_id = "LOCAL_TEST"
p_pipeline_name = "test_pipeline"
p_status = "InProgress"
p_error_message = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType

current_time = datetime.utcnow()

if p_status == "InProgress":
    # 1. Insert a fresh execution row
    audit_data = [(p_run_id, p_pipeline_name, "BRONZE", "InProgress", current_time, current_time)]
    audit_schema = StructType([
        StructField("run_id", StringType(), True),
        StructField("pipeline_name", StringType(), True),
        StructField("layer_name", StringType(), True),
        StructField("status", StringType(), True),
        StructField("start_time", TimestampType(), True),
        StructField("created_date", TimestampType(), True)
    ])
    audit_df = spark.createDataFrame(audit_data, schema=audit_schema)
    audit_df.write.mode("append").format("delta").saveAsTable("audit_pipeline_run")
    print(f"📝 Run {p_run_id} marked as InProgress for pipeline {p_pipeline_name}.")

elif p_status in ["Succeeded", "Failed"]:
    # 2. Use a safe MERGE that matches on run_id 
    # If the row doesn't exist for some reason, we can safely write it here too!
    spark.sql(f"""
        MERGE INTO audit_pipeline_run AS target
        USING (SELECT '{p_run_id}' AS run_id) AS source
        ON target.run_id = source.run_id
        WHEN MATCHED THEN
            UPDATE SET 
                target.status = '{p_status}',
                target.end_time = current_timestamp(),
                target.duration_seconds = cast(unix_timestamp(current_timestamp()) - unix_timestamp(target.start_time) as int),
                target.error_message = {f"'{p_error_message}'" if p_error_message else "NULL"}
        WHEN NOT MATCHED THEN
            INSERT (run_id, pipeline_name, layer_name, status, start_time, end_time, error_message, created_date)
            VALUES ('{p_run_id}', '{p_pipeline_name}', 'BRONZE', '{p_status}', current_timestamp(), current_timestamp(), {f"'{p_error_message}'" if p_error_message else "NULL"}, current_timestamp())
    """)
    print(f"📝 Run {p_run_id} completely updated to {p_status} for pipeline {p_pipeline_name}.")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
