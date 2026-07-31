# Data Source Documentation: Finnhub Stock API

## 1. Clear Understanding of the Source
Finnhub is a comprehensive real-time financial data provider. We utilize its REST API endpoints to capture non-pricing master records, specifically deep corporate profiles and standardized primary financial statements (Balance Sheets, Income Statements, and Cash Flow Statements).

## 2. Business Purpose & Value Add
* **Company Master Ledger:** Serves as our absolute source of truth for categorizing companies into distinct sectors and industries.
* **Fundamental Anchoring:** Ingests raw reported financial line items to map long-term corporate health underneath moving stock prices.
* **Cross-Sectional Filtering:** Allows analysts to filter peer groups (e.g., comparing all companies in the "Technology" sector).

## 3. Data Schema & Columns (Silver Layer Target)
### Block A: Corporate Profiles (`dim_company`)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `ticker` | VARCHAR(10) | The unique stock symbol identifier. |
| `company_name` | VARCHAR(255)| The full registered legal name of the corporation. |
| `sector` | VARCHAR(100)| The broad economic sector classification. |
| `industry` | VARCHAR(100)| The specific industry niche mapping. |
| `country` | VARCHAR(50) | The country where the company headquarters is located. |
| `currency` | VARCHAR(10) | The primary reporting currency (e.g., USD, EUR). |
| `market_cap_m` | DECIMAL(18, 2) | Total market capitalization in millions of reporting currency. |

### Block B: Financial Statements (`fact_financial_statements`)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `ticker` | VARCHAR(10) | The unique stock symbol identifier. |
| `fiscal_year` | INT | The financial reporting year (e.g., 2025). |
| `fiscal_period` | VARCHAR(10) | Period type: FY (Full Year), Q1, Q2, Q3, or Q4. |
| `total_revenue` | BIGINT | Gross revenue generated during the period. |
| `net_income` | BIGINT | Total net profit after all expenses, taxes, and interest. |
| `total_assets` | BIGINT | Total economic resources owned by the corporation. |
| `total_liabilities`| BIGINT | Total financial obligations owed to external parties. |
| `operating_cash_flow`| BIGINT | Total cash generated strictly from core business operations. |
