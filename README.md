# Upstox Sell Alert

Reads multiple **Upstox Historical OHLC `.xlsx` files** and generates a consolidated stock-wise price summary.

# 🚀 Problem This Solves

Analyzing historical OHLC data for multiple stocks manually can be time-consuming, especially when each stock is downloaded as a separate Upstox file.

This code automatically reads all Upstox files from a folder, identifies the stock from the filename, and generates a consolidated summary.

# ⚙️ How It Works

Reads all `.xlsx` files from the configured folder.

The stock name is automatically extracted from each filename.

For every stock, the program calculates the maximum:

- Open Price
- High Price
- Low Price
- Close Price

All stocks are then combined into a single consolidated report.

# 📥 Input

## Upstox Historical OHLC Files

Place the downloaded Upstox `.xlsx` files in a folder and provide the folder path in `run.py`.

Example:

```python
folder_path = r"C:\Users\YourName\Downloads\Upstox"
