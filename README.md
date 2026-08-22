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
