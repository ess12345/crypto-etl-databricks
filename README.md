🪙 Crypto Market ETL Pipeline (Databricks + Delta Live Tables)

This project collects live cryptocurrency market data from the CoinGecko API, stores it in Databricks, and processes it through a structured data pipeline using Delta Live Tables (DLT) and PySpark.

The goal is to build a clear Medallion-style pipeline with three layers:

Bronze: Raw ingested data

Silver: Cleaned and structured data

Gold: Analytics-ready table


🔄 How the Pipeline Works
1️⃣ API Extraction (Python script)

A Python function (fetch_crypto_data.py) calls the CoinGecko API.

It retrieves crypto market data and returns it as JSON.

The notebook runs this function and writes the data into a Unity Catalog Volume as raw JSON files.

2️⃣ Bronze Layer (DLT)

Reads the raw JSON data using Autoloader.

Adds a timestamp column.

Stores the output as a Bronze DLT table.

✨ Purpose: Capture the raw source data with minimal changes.

3️⃣ Silver Layer (DLT)

Reads the Bronze table.

Renames columns for clarity.

Enforces data types.

Applies basic validation rules (dropping bad or missing data).

✨ Purpose: Create a clean, usable version of the data.

4️⃣ Gold Layer (DLT)

Reads the Silver table.

Uses window functions and calculations to create analytics-ready datasets.

Example outputs include:

Latest crypto leaderboard

Time-based trend metrics

✨ Purpose: Prepare data for reporting, dashboards, or analysis.

⚙️ Requirements

Current dependencies:

requests


Install with:

pip install -r requirements.txt

🧱 Medallion Architecture Summary
Layer	Description
Bronze	Raw API data stored as-is
Silver	Cleaned and standardized
Gold	Aggregated and analytical
📌 Current Status

✔ API data ingestion working
✔ Raw JSON stored in Databricks
✔ Bronze, Silver, Gold DLT tables created
✔ Basic transformations and trends implemented

🚀 Next Steps (Future Enhancements)

Schedule the pipeline to run automatically

Add monitoring or alerts

Build dashboards in Power BI / Databricks SQL