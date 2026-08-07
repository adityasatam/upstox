##############################################################
# INPUT:
# Folder containing Upstox historical OHLC files
#
# OUTPUT:
# 1. Maximum Open Price
# 2. Maximum High Price
# 3. Maximum Low Price
# 4. Maximum Close Price
#
# Future Reports:
# - Minimum Prices
# - Average Prices
# - CAGR
# - Drawdown
# - Volatility
#
# Author : Aditya Satam
##############################################################

import os
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


# ==========================================================
# Read one stock file
# ==========================================================

def read_stock_file(file_path):

    df = pd.read_excel(
        file_path,
        usecols="B:E",
        dtype=str,
        engine="openpyxl"
    )

    df.columns = [
        "Open",
        "High",
        "Low",
        "Close"
    ]

    return df


# ==========================================================
# Clean numeric columns
# ==========================================================

def clean_numeric_columns(df):

    for col in df.columns:

        df[col] = (
            df[col]
            .fillna("")
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.strip()
        )

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


# ==========================================================
# Extract stock name
# ==========================================================

def get_stock_name(file_name):

    return file_name.split("-")[0]


# ==========================================================
# Maximum OHLC Report
# ==========================================================

def summary_max_price(folder_path):

    result = []

    for file in os.listdir(folder_path):

        if not file.endswith(".xlsx"):
            continue

        try:

            stock = get_stock_name(file)

            df = read_stock_file(
                os.path.join(folder_path, file)
            )

            df = clean_numeric_columns(df)

            result.append({

                "Stock": stock,

                "Max_Open": df["Open"].max(),

                "Max_High": df["High"].max(),

                "Max_Low": df["Low"].max(),

                "Max_Close": df["Close"].max()

            })

        except Exception as e:

            print(f"Error : {file}")

            print(e)

    return (
        pd.DataFrame(result)
        .sort_values("Stock")
        .reset_index(drop=True)
    )


# ==========================================================
# Print Report
# ==========================================================

def print_report(df, title):

    print()

    print("=" * 15, title, "=" * 15)

    print()

    print(df.to_string(index=False))


# ==========================================================
# Main
# ==========================================================

def main(folder_path):

    max_df = summary_max_price(folder_path)

    print_report(
        max_df,
        "MAXIMUM OHLC SUMMARY"
    )


# ==========================================================
# Driver
# ==========================================================

if __name__ == "__main__":

    main(
        r"C:\Users\sasuk\upstox\upstox_files"
    )
