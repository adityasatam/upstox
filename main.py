##############################################################
# INPUT:
# Folder containing Upstox Historical OHLC (.xlsx) files
# first_buy_date.txt
#
# OUTPUT:
# Report 1
# Maximum High Since First Buy
# Overall Maximum High
# Difference
#
# Future Reports
# ------------------------------
# Report 2 : Minimum Price
# Report 3 : CAGR
# Report 4 : Drawdown
# Report 5 : Volatility
#
# Author : Aditya Satam
#
# Version History
# ----------------------------------------------------------
# 08-08-2026 Initial Version
# 08-08-2026 Added First Buy Date Report
##############################################################

import os
import pandas as pd

# ==========================================================
# DISPLAY SETTINGS
# ==========================================================

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# ==========================================================
# READ BUY DATE FILE
# ==========================================================

def read_buy_dates(folder_path, buy_date_file):

    file_path = os.path.join(
        folder_path,
        buy_date_file
    )

    if not os.path.exists(file_path):

        raise FileNotFoundError(

            f"Cannot find {buy_date_file}"

        )

    buy_dates = {}

    with open(file_path, "r") as f:

        for line in f:

            line = line.strip()

            if not line:

                continue

            parts = line.split("|")

            if len(parts) != 2:

                continue

            stock = parts[0].strip()

            buy_date = pd.to_datetime(

                parts[1].strip(),

                format="%d-%m-%Y"

            )

            buy_dates[stock] = buy_date

    return buy_dates


# ==========================================================
# GET STOCK NAME
# ==========================================================

def get_stock_name(file_name):

    return file_name.split("-")[0]


# ==========================================================
# READ STOCK FILE
# ==========================================================

def read_stock_file(file_path):

    df = pd.read_excel(

        file_path,

        engine="openpyxl"

    )

    return df


# ==========================================================
# CLEAN DATAFRAME
# ==========================================================

def clean_dataframe(df):

    # First column is Date

    date_column = df.columns[0]

    df[date_column] = pd.to_datetime(

        df[date_column],

        dayfirst=True,

        errors="coerce"

    )

    # OHLC Columns

    ohlc_columns = df.columns[1:5]

    for column in ohlc_columns:

        df[column] = (

            df[column]

            .astype(str)

            .str.replace(",", "", regex=False)

            .str.strip()

        )

        df[column] = pd.to_numeric(

            df[column],

            errors="coerce"

        )

    return df


# ==========================================================
# GET MAXIMUM HIGH
# ==========================================================

def get_overall_max(df):

    high_column = df.columns[2]

    return df[high_column].max()


# ==========================================================
# GET MAXIMUM HIGH AFTER BUY DATE
# ==========================================================

def get_max_since_buy(df, buy_date):

    date_column = df.columns[0]

    high_column = df.columns[2]

    filtered_df = df[

        df[date_column] >= buy_date

    ]

    if filtered_df.empty:

        return None

    return filtered_df[high_column].max()


# ==========================================================
# DIFFERENCE
# ==========================================================

def calculate_difference(

    overall_max,

    max_since_buy

):

    if pd.isna(max_since_buy):

        return None

    return round(

        overall_max - max_since_buy,

        2

    )

# ==========================================================
# REPORT
# ==========================================================

def report_max_since_buy(

    folder_path,

    buy_date_file

):

    buy_dates = read_buy_dates(

        folder_path,

        buy_date_file

    )

    report = []

    for file in os.listdir(folder_path):

        if not file.lower().endswith(".xlsx"):

            continue

        stock = get_stock_name(file)

        if stock not in buy_dates:

            continue

        try:

            file_path = os.path.join(

                folder_path,

                file

            )

            df = read_stock_file(

                file_path

            )

            df = clean_dataframe(df)

            buy_date = buy_dates[stock]

            overall_max = get_overall_max(df)

            max_since_buy = get_max_since_buy(

                df,

                buy_date

            )

            difference = calculate_difference(

                overall_max,

                max_since_buy

            )

            report.append({

                "Stock": stock,

                "First Buy Date": buy_date.strftime(

                    "%d-%m-%Y"

                ),

                "Max Since First Bought":

                    None

                    if pd.isna(max_since_buy)

                    else round(

                        max_since_buy,

                        2

                    ),

                "Overall Max":

                    round(

                        overall_max,

                        2

                    ),

                "Difference":

                    difference

            })

        except Exception as e:

            print(

                f"Error processing {stock}"

            )

            print(e)

    report_df = pd.DataFrame(report)

    if report_df.empty:

        return report_df

    report_df = (

        report_df

        .sort_values(

            by="Stock"

        )

        .reset_index(

            drop=True

        )

    )

    return report_df


# ==========================================================
# PRINT REPORT
# ==========================================================

def print_report(

    df,

    report_name

):

    if df.empty:

        print()

        print(

            "No records found."

        )

        return

    print()

    print(

        "=" * 25,

        report_name,

        "=" * 25

    )

    print()

    print(

        df.to_string(

            index=False

        )

    )


# ==========================================================
# FUTURE REPORT PLACEHOLDER
# ==========================================================

def report_min_price(

    folder_path,

    buy_date_file

):

    """
    Future Report

    Minimum price after buying.
    """

    pass


def report_cagr(

    folder_path,

    buy_date_file

):

    """
    Future Report

    CAGR calculation.
    """

    pass


def report_drawdown(

    folder_path,

    buy_date_file

):

    """
    Future Report

    Maximum drawdown.
    """

    pass

# ==========================================================
# MAIN
# ==========================================================

def main(

    folder_path,

    buy_date_file="first_buy_date.txt"

):

    # ------------------------------------------------------
    # Report 1
    # Maximum High Since First Buy
    # ------------------------------------------------------

    report_1 = report_max_since_buy(

        folder_path,

        buy_date_file

    )

    print_report(

        report_1,

        "MAXIMUM HIGH REPORT"

    )

    # ------------------------------------------------------
    # Future Reports
    # Uncomment whenever implemented
    # ------------------------------------------------------

    #
    # report_2 = report_min_price(
    #     folder_path,
    #     buy_date_file
    # )
    #
    # print_report(
    #     report_2,
    #     "MINIMUM PRICE REPORT"
    # )
    #

    #
    # report_3 = report_cagr(
    #     folder_path,
    #     buy_date_file
    # )
    #
    # print_report(
    #     report_3,
    #     "CAGR REPORT"
    # )
    #

    #
    # report_4 = report_drawdown(
    #     folder_path,
    #     buy_date_file
    # )
    #
    # print_report(
    #     report_4,
    #     "DRAWDOWN REPORT"
    # )


# ==========================================================
# END OF FILE
# ==========================================================
