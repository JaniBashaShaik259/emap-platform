# Data Source Documentation: News API

## 1. Clear Understanding of the Source
News API aggregates live and historical news articles from thousands of global business publications and financial blogs via a REST API protocol. It delivers structured metadata, titles, and body snippets for any targeted keyword or ticker query.

## 2. Business Purpose & Value Add
* **Market Sentiment Engine:** Provides the textual raw material required for Natural Language Processing (NLP) models to score daily market mood (Positive, Negative, Neutral).
* **Early Warning Tracking:** Detects sudden spikes in news volume or negative vocabulary relating to corporate scandals, supply chain breaks, or management changes.
* **Contextual Analysis:** Overlays news events directly onto stock charts to understand why a price spiked or crashed on a specific day.

## 3. Data Schema & Columns (Silver Layer Target)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `article_id` | VARCHAR(64) | Unique SHA-256 hash generated from the URL to serve as a primary key. |
| `target_keyword` | VARCHAR(50) | The stock ticker or keyword searched (e.g., "AAPL", "Inflation"). |
| `published_at` | TIMESTAMP | The exact date and UTC time the article went live. |
| `source_name` | VARCHAR(100)| The name of the publishing media outlet (e.g., Reuters, Bloomberg). |
| `author` | VARCHAR(150)| The journalist or writer credited, if available. |
| `title` | TEXT | The main headline of the news article. |
| `description` | TEXT | A brief introductory snippet or summary of the article body. |
| `article_url` | VARCHAR(512)| The direct web hyperlink to the original article source. |
