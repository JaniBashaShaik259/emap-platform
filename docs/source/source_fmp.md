# Data Source Documentation: Financial Modeling Prep (FMP)

## 1. Clear Understanding of the Source
Financial Modeling Prep (FMP) is an institutional REST API targeting fundamental analysis. We use their free tier to extract advanced, pre-calculated financial ratios and metrics, removing the need to manually compute complex equations over raw balance sheets.

## 2. Business Purpose & Value Add
* **Solvency & Liquidity Monitoring:** Tracks whether companies maintain safe debt loads and healthy working capital.
* **Efficiency Benchmarking:** Rates management performance by measuring how effectively they use capital to generate returns.
* **Automated Screening:** Powers investment filters to locate undervalued stocks automatically (e.g., screening for low PE ratios with high ROE).

## 3. Data Schema & Columns (Silver Layer Target)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `ticker` | VARCHAR(10) | The unique stock symbol identifier. |
| `reporting_date` | DATE | The filing date associated with the ratios. |
| `pe_ratio` | DECIMAL(10, 4) | Price-to-Earnings Ratio (Current Price / Earnings Per Share). |
| `pb_ratio` | DECIMAL(10, 4) | Price-to-Book Ratio (Current Price / Book Value Per Share). |
| `debt_to_equity` | DECIMAL(10, 4) | Total Liabilities / Total Shareholders' Equity. |
| `return_on_equity`| DECIMAL(10, 4) | ROE percentage (Net Income / Shareholders' Equity). |
| `current_ratio` | DECIMAL(10, 4) | Liquidity measure (Current Assets / Current Liabilities). |
| `free_cash_flow_yield`| DECIMAL(10, 4)| Free Cash Flow per share divided by the current market price. |
