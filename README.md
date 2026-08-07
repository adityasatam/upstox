# Upstox Stock Summary

Python utility to analyze multiple **Upstox Historical OHLC (.xlsx)** files and generate stock-wise price summaries.

---

## Features

- Reads all `.xlsx` files from a folder.
- Automatically extracts the **stock name** from the filename.
- Calculates:
  - Maximum Open Price
  - Maximum High Price
  - Maximum Low Price
  - Maximum Close Price
- Displays a consolidated report.
- Automatically installs required Python packages.
- Always executes the latest `main.py` directly from GitHub.

---

## Folder Structure

```
upstox_stock_summary/
│
├── main.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Input

Place all Upstox Historical Data files in one folder.

Example:

```
ADANIENSOL-OHLC-1W-Data-12Feb2018(5.30AM)-3Aug2026(5.30AM).xlsx

RELIANCE-OHLC-1W-Data-01Jan2018-03Aug2026.xlsx

SBIN-OHLC-1W-Data-01Jan2018-03Aug2026.xlsx
```

The stock name is automatically extracted as:

```
ADANIENSOL
RELIANCE
SBIN
```

---

## Output

Example

```
=============== MAXIMUM OHLC SUMMARY ===============

        Stock   Max_Open  Max_High  Max_Low  Max_Close

 ADANIENSOL     1385.50   1450.00   1340.20    1438.40
 RELIANCE       3520.30   3589.40   3478.10    3565.80
 SBIN            988.40   1006.80    945.00     999.30
```

---

## Installation

Python 3.10 or later is recommended.

No manual package installation is required.

`run.py` automatically downloads and installs all required dependencies.

---

## How to Run

Open `run.py`.

Modify only:

```python
main(
    folder_path=r"C:\Users\YourName\Downloads\Upstox"
)
```

Then execute:

```
python run.py
```

---

## Reports

Current Reports

- Maximum OHLC Summary

Future Reports

- Minimum OHLC Summary
- Average OHLC Summary
- 52 Week High
- 52 Week Low
- CAGR
- Volatility
- Drawdown
- Returns
- ATH Analysis

---

## Requirements

Automatically installed.

```
pandas
openpyxl
```

---

## Author

Aditya Satam

---

## License

MIT License
