Upstox Stock Summary

Reads multiple Upstox Historical OHLC .xlsx files and generates a consolidated stock-wise price summary.

🚀 Problem This Solves

Analyzing historical OHLC data for multiple stocks manually can be time-consuming, especially when each stock is downloaded as a separate Upstox file.

This code automatically reads all Upstox files from a folder, identifies the stock from the filename, and generates a consolidated summary.

⚙️ How It Works

Reads all .xlsx files from the configured folder.

The stock name is automatically extracted from each filename.

For every stock, the program calculates the maximum:

Open Price
High Price
Low Price
Close Price

All stocks are then combined into a single consolidated report.

📥 Input
Upstox Historical OHLC Files

Place the downloaded Upstox .xlsx files in a folder and provide the folder path in run.py.

Example:

folder_path = r"C:\Users\YourName\Downloads\Upstox"

Example files:

ADANIENSOL-OHLC-1W-Data-12Feb2018(5.30AM)-3Aug2026(5.30AM).xlsx

RELIANCE-OHLC-1W-Data-01Jan2018-03Aug2026.xlsx

SBIN-OHLC-1W-Data-01Jan2018-03Aug2026.xlsx

The stock names are automatically extracted as:

ADANIENSOL
RELIANCE
SBIN
🐦 Main
main(
    folder_path=folder_path
)
Parameters
1. folder_path

Type: str

Folder containing the Upstox Historical OHLC .xlsx files.

Example:

folder_path = r"C:\Users\YourName\Downloads\Upstox"

All .xlsx files in this folder are processed automatically.

📤 Output

The program generates a consolidated Maximum OHLC Summary.

Example:

=============== MAXIMUM OHLC SUMMARY ===============

        Stock   Max_Open  Max_High  Max_Low  Max_Close

 ADANIENSOL     1385.50   1450.00   1340.20    1438.40
 RELIANCE       3520.30   3589.40   3478.10    3565.80
 SBIN             988.40   1006.80    945.00     999.30

For each stock, the report contains:

Maximum Open Price
Maximum High Price
Maximum Low Price
Maximum Close Price
📌 Important Notes
Only .xlsx files are processed.
All .xlsx files in the configured folder are analyzed.
Stock names are automatically extracted from the filenames.
Multiple stocks can be analyzed in a single execution.
run.py automatically downloads and installs the required packages.
run.py always downloads and executes the latest main.py directly from GitHub.
Internet access is required to download the latest code and dependencies.
Python 3.10 or later is recommended.
