# upstox_sell_alert

Analyzes multiple **Upstox Historical OHLC `.xlsx` files** and identifies the maximum High price since the first buy date.

# 🚀 Problem This Solves

When tracking multiple stocks, manually checking historical prices from individual Upstox files can be time-consuming.

This utility automatically analyzes all stock files and compares the **maximum High since the first purchase** with the **overall historical maximum High**.

# ⚙️ How It Works

Reads all Upstox Historical OHLC `.xlsx` files from the configured folder.

The stock name is automatically extracted from each filename.

The first purchase date for each stock is read from `first_buy_date.txt`.

For each stock, the program:

- Finds the maximum High price since the first buy date.
- Finds the overall historical maximum High price.
- Calculates the difference between the two values.
- Combines all stocks into a single consolidated report.

# 📥 Input

## Upstox Historical OHLC Files

Place all downloaded Upstox `.xlsx` files in the configured folder.

Example:

```text
upstox_files/
│
├── ADANIENSOL-OHLC-1W-Data.xlsx
├── ADANIENT-OHLC-1W-Data.xlsx
├── ADANIGREEN-OHLC-1W-Data.xlsx
├── RELIANCE-OHLC-1W-Data.xlsx
└── TCS-OHLC-1W-Data.xlsx

The stock name is automatically extracted from the filename.

For example:

ADANIENSOL-OHLC-1W-Data.xlsx

becomes:

ADANIENSOL
First Buy Date

Create first_buy_date.txt inside the same folder.

Format:

STOCK|DD-MM-YYYY

Example:

ADANIENSOL|12-09-2024
ADANIENT|11-07-2024
ADANIGREEN|10-09-2025
RELIANCE|20-01-2022
TCS|15-03-2020

Only stocks having a corresponding first buy date are included in the report.

🐦 Main
main(
    folder_path=r"C:\Users\YourName\upstox\upstox_files",
    buy_date_file="first_buy_date.txt"
)
Parameters
1. folder_path

Type: str

Folder containing the Upstox .xlsx files and first_buy_date.txt.

Example:

folder_path=r"C:\Users\YourName\upstox\upstox_files"
2. buy_date_file

Type: str

File containing the first purchase date for each stock.

Default:

buy_date_file="first_buy_date.txt"
📤 Output
Maximum High Report

The current report displays:

Stock
First Buy Date
Max Since First Bought
Overall Max
Difference

Example:

========================= MAXIMUM HIGH REPORT =========================

     Stock First Buy Date  Max Since First Bought  Overall Max  Difference
ADANIENSOL     12-09-2024                 1789.00      4236.80     2447.80
  ADANIENT     11-07-2024                 3258.00      4190.00      932.00
ADANIGREEN     10-09-2025                 1631.50      3050.00     1418.50
ADANIPORTS     05-08-2024                 1891.10      1891.10        0.00

Difference is calculated as:

Overall Max - Max Since First Bought
📌 Important Notes
Only .xlsx files are processed.
Stock names are extracted automatically from filenames.
Stocks without a first buy date are skipped.
Buy dates must use the DD-MM-YYYY format.
Invalid buy dates are reported and skipped.
OHLC values are converted to numeric values before calculations.
Historical dates support different date formats without generating Pandas date-format warnings.
Missing or invalid data for one stock does not stop processing of other stocks.
The report is sorted alphabetically by stock.
openpyxl is used to read Upstox .xlsx files.
run.py automatically installs required packages and downloads the latest main.py from GitHub.
Future reports are planned for Minimum Price, CAGR, Drawdown and Volatility.
