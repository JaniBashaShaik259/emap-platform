# Data Source Documentation: Exchange Rate API

## 1. Clear Understanding of the Source
Exchange Rate API provides clean, lightweight, and highly reliable foreign exchange spot currency conversion rates. We leverage its daily endpoint to pull a comprehensive base currency matrix.

## 2. Business Purpose & Value Add
* **Global Asset Normalization:** Automatically converts global equity entries and revenues into a single reporting currency (e.g., converting London or European stock figures into USD).
* **FX Exposure Management:** Tracks volatility across currency pairs to assess foreign exchange risk inside international investment accounts.

## 3. Data Schema & Columns (Silver Layer Target)

|Column Name | Data Type | Description |
| :--- | :--- | :--- |
|base_currency |VARCHAR(10) |The anchor conversion currency (typically USD).|
|target_currency |VARCHAR(10)| The destination currency being valued (e.g., EUR, INR, GBP).|
|conversion_date| DATE |The calendar date of the recorded spot rate.|
|exchange_rate |DECIMAL(18, 6)|The multiplier needed to convert the base currency to the target currency.|
