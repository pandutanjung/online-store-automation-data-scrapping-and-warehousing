
# 🛍️ Online Store Automation: Data Scraping & Warehousing

This project showcases a complete end-to-end ETL pipeline for scraping product data from an online fashion store, transforming the data for analysis, and storing it in multiple destinations. Built with Python, the solution is designed to support data-driven operations and business intelligence through automation.

## 📌 Features

- **Web Scraping**: Extract product information such as name, price, rating, size, color, and gender using BeautifulSoup.
- **Data Cleaning & Transformation**: Clean and format raw data using Pandas.
- **Data Loading**:
  - Save the final dataset to a CSV file.
  - Export to Google Sheets using Sheets API.
  - Insert into a PostgreSQL database for further processing.
- **Unit Testing**: Modular tests included for extract, transform, and load phases using `unittest` and `mock`.

## 🗂️ Project Structure

```
.
├── main.py                  # Main controller for the ETL pipeline
├── utils/
│   ├── extract.py           # Scraping logic
│   ├── transform.py         # Data cleaning and formatting
│   └── load.py              # Load data to CSV, Google Sheets, PostgreSQL
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── products.csv             # Output file for scraped data
├── requirements.txt         # List of required Python packages
├── submission.txt           # Final notes or report
└── google-sheets-api.json   # Google Sheets API credentials (excluded from repo)
```

## 🚀 How to Run

1. Clone this repository:
```bash
git clone https://github.com/pandutanjung/online-store-automation-data-scrapping-and-warehousing.git
cd online-store-automation-data-scrapping-and-warehousing
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main pipeline:
```bash
python main.py
```

> ⚠️ Make sure you have configured your Google Sheets API key if you want to use the export-to-sheets feature.

## 🧪 Run Tests

To ensure each ETL phase works correctly:

```bash
python -m unittest discover tests
```

Or run with test coverage:
```bash
coverage run -m unittest discover tests
coverage report -m
```
