# Data Source Documentation: Alpha Vantage

## 1. Clear Understanding of the Source
Alpha Vantage provides real-time and historical financial market data via a structured REST API. It acts as our primary engine for capturing daily equity closing prices, adjusting for splits and dividends, and providing baseline technical indicators for our core asset watchlists.

## 2. Business Purpose & Value Add
* **Market Trend Analysis:** Captures end-of-day equity prices to calculate historical volatility and momentum.
* **Portfolio Valuation:** Feeds baseline pricing data to value synthetic portfolios and backtest quantitative trading strategies.
* **Algorithmic Triggers:** Provides clean daily data points to calculate simple moving averages (SMA) and exponential moving averages (EMA).

## 3. Data Schema & Columns (Silver Layer Target)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `ticker` | VARCHAR(10) | The unique stock symbol identifier (e.g., AAPL, MSFT). |
| `trading_date` | DATE | The calendar date of the trading session (YYYY-MM-DD). |
| `open_price` | DECIMAL(18, 4) | The opening price of the stock for the session. |
| `high_price` | DECIMAL(18, 4) | The maximum price reached during the session. |
| `low_price` | DECIMAL(18, 4) | The minimum price reached during the session. |
| `close_price` | DECIMAL(18, 4) | The standard closing price of the stock. |
| `adjusted_close`| DECIMAL(18, 4) | The closing price adjusted for corporate actions (splits/dividends). |
| `volume` | BIGINT | The total number of shares traded during the session. |
| `dividend_amount`| DECIMAL(18, 4) | Cash dividend amount paid per share on this date, if applicable. |
