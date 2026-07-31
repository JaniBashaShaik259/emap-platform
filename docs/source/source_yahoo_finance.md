# Data Source Documentation: Yahoo Finance (`yfinance`)

## 1. Clear Understanding of the Source
Yahoo Finance data is ingested via the open-source `yfinance` Python library, which handles rapid, direct HTTP requests to scrape and extract bulk financial records. Because it does not require an API key and lacks daily volume caps, it serves as our primary data-backfill engine.

## 2. Business Purpose & Value Add
* **Deep History Engine:** Downloads 10 to 20 years of daily historical price records in a single execution block without triggering rate limits.
* **Data Redundancy:** Validates and backfills missing trading sessions or historical gaps left by free REST API limits.
* **Corporate Actions Log:** Gathers historical stock split ratios to maintain accurate data cleaning models over time.

## 3. Data Schema & Columns (Silver Layer Target)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `ticker` | VARCHAR(10) | The unique stock symbol identifier. |
| `trading_date` | DATE | The calendar date of the historical record (YYYY-MM-DD). |
| `open_price` | DECIMAL(18, 4) | The historical session opening price. |
| `close_price` | DECIMAL(18, 4) | The historical session standard closing price. |
| `volume` | BIGINT | Total volume of shares exchanged. |
| `stock_splits` | VARCHAR(20) | Text format of split execution on this date (e.g., "2:1"), otherwise NULL. |
