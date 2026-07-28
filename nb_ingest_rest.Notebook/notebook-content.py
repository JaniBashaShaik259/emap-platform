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
p_ticker = "AAPL"
p_lookback = "1mo"
p_interval = "1d"


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
%pip install yfinance

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import yfinance as yf
import pandas as pd
from datetime import datetime

# Fabric will now automatically overwrite these with pipeline values
print(f"🚀 Starting dynamic ingestion for Ticker: {p_ticker}")

# 1. Download data for a SINGLE ticker fed by the parameters
raw_data = yf.download(
    tickers=p_ticker, 
    period=p_lookback, 
    interval=p_interval
)

# 2. Flatten and format the single ticker dataframe
if not raw_data.empty:
    df = raw_data.reset_index()
    df['Ticker'] = p_ticker
    df['IngestedAt'] = datetime.utcnow()
    
    # Clean up column names for Delta safety
    df.columns = df.columns.str.replace(' ', '_')
    
    # 3. Write to Bronze
    spark_df = spark.createDataFrame(df)
    spark_df.write \
        .mode("append") \
        .format("delta") \
        .saveAsTable("bronze_stock_prices")
        
    print(f"✅ Data for {p_ticker} appended to bronze_stock_prices!")
else:
    print(f"⚠️ No data found for {p_ticker}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Query your new Delta table to see the results
display(spark.sql("SELECT COUNT(*) FROM Br_Stock_Prices))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
