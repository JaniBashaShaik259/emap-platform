# Data Source Documentation: Federal Reserve Economic Data (FRED)

## 1. Clear Understanding of the Source
Maintained by the Federal Reserve Bank of St. Louis, FRED is the absolute authority on macroeconomic indicators. Its REST API allows automated extraction of time-series data covering interest rates, economic output, and national price indexes.

## 2. Business Purpose & Value Add
* **Macro Regime Mapping:** Ingests baseline economic conditions to determine if markets are in an expansionary inflationary phase or a contractionary recession.
* **Discount Rate Inputs:** Supplies current risk-free interest rates (US Treasury Yields) to power internal Discounted Cash Flow (DCF) valuation models.
* **Purchasing Power Benchmarks:** Ingests CPI metrics to adjust corporate revenue growth trends against real-world inflation.

## 3. Data Schema & Columns (Silver Layer Target)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `series_id` | VARCHAR(20) | The official FRED tracking code (e.g., GS10 for 10-Yr Treasury, CPIAUCSL for CPI). |
| `indicator_name` | VARCHAR(100)| Descriptive name of the metric (e.g., "10-Year Treasury Constant Maturity Rate"). |
| `observation_date`| DATE | The date of the economic release or record (YYYY-MM-DD). |
| `metric_value` | DECIMAL(18, 4) | The actual recorded numerical value of the indicator. |
