# upstox_sell_alert

Analyzes multiple **Upstox Historical OHLC `.xlsx` files** and identifies the **maximum High price since the first buy date**, along with the overall historical maximum.

# 🚀 Problem This Solves

When holding multiple stocks, manually checking whether a stock has reached its historical high after the first purchase can be time-consuming.

This utility automatically compares each stock's:

- Maximum High since the first buy date
- Overall historical Maximum High
- Difference between the two

and generates a consolidated report.

# ⚙️ How It Works

Reads all Upstox Historical OHLC `.xlsx` files from a configured folder.

The stock name is automatically extracted from the filename.

The first purchase date for each stock is read from `first_buy_date.txt`.

For every stock, the program calculates:

- **Maximum High Since First Buy** — Highest High price recorded on or after the first buy date.
- **Overall Maximum High** — Highest High price available in the complete historical data.
- **Difference** — Difference between the overall historical maximum and the maximum reached since the first purchase.

# 📥 Input

## Upstox Historical OHLC Files

Place all downloaded Upstox `.xlsx` files in one folder.

Example:

```text
upstox_files/
│
├── ADANIENSOL-OHLC-1W-Data.xlsx
├── ADANIENT-OHLC-1W-Data.xlsx
├── ADANIGREEN-OHLC-1W-Data.xlsx
├── RELIANCE-OHLC-1W-Data.xlsx
└── TCS-OHLC-1W-Data.xlsx
