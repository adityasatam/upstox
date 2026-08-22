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
# ----------------------------------------------------------
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
# 22-08-2026 Fixed date parsing warnings
##############################################################


import os
import pandas as pd


# ==========================================================
# DISPLAY SETTINGS
# ==========================================================

pd.set_option(
    "display.max_rows",
    None
)

pd.set_option(
    "display.max_columns",
    None
)

pd.set_option(
    "display.width",
    None
)

pd.set_option(
    "display.max_colwidth",
    None
)

pd.set_option(
    "display.expand_frame_repr",
    False
)


# ==========================================================
# READ BUY DATE FILE
# ==========================================================

def read_buy_dates(
    folder_path,
    buy_date_file
):

    file_path = os.path.join(
        folder_path,
        buy_date_file
    )

    if not os.path.exists(file_path):

        raise FileNotFoundError(
            f"Cannot find {buy_date_file}"
        )

    buy_dates = {}

    with open(
        file_path,
        "r"
    ) as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            parts = line.split("|")

            if len(parts) != 2:
                continue

            stock = parts[0].strip()
            date_string = parts[1].strip()

            buy_date = pd.to_datetime(
                date_string,
                format="%d-%m-%Y",
                errors="coerce"
            )

            if pd.isna(buy_date):

                print(
                    f"Invalid buy date for "
                    f"{stock}: {date_string}"
                )

                continue

            buy_dates[stock] = buy_date

    return buy_dates


# ==========================================================
# GET STOCK NAME
# ==========================================================

def get_stock_name(
    file_name
):

    return file_name.split("-")[0].strip()


# ==========================================================
# READ STOCK FILE
# ==========================================================

def read_stock_file(
    file_path
):

    df = pd.read_excel(
        file_path,
        engine="openpyxl"
    )

    return df


# ==========================================================
# CLEAN DATAFRAME
# ==========================================================

def clean_dataframe(
    df
):

    # ------------------------------------------------------
    # Validate DataFrame
    # ------------------------------------------------------

    if df is None or df.empty:

        return pd.DataFrame()

    # ------------------------------------------------------
    # Date Column
    # ------------------------------------------------------

    date_column = df.columns[0]

    # Upstox files can contain Excel datetime values,
    # DD-MM-YYYY strings, DD/MM/YYYY strings, etc.
    #
    # format="mixed" prevents Pandas from trying to infer
    # one format for the complete column and avoids the
    # "Could not infer format" warning.

    df[date_column] = pd.to_datetime(
        df[date_column],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )

    # ------------------------------------------------------
    # OHLC Columns
    # ------------------------------------------------------

    ohlc_columns = df.columns[1:5]

    for column in ohlc_columns:

        df[column] = (
            df[column]
            .astype(str)
            .str.replace(
                ",",
                "",
                regex=False
            )
            .str.strip()
        )

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # ------------------------------------------------------
    # Remove Rows With Invalid Dates
    # ------------------------------------------------------

    df = df[
        df[date_column].notna()
    ].copy()

    # ------------------------------------------------------
    # Remove Rows Without OHLC Data
    # ------------------------------------------------------

    if len(ohlc_columns) >= 4:

        df = df[
            df[ohlc_columns].notna().any(axis=1)
        ].copy()

    return df


# ==========================================================
# GET OVERALL MAXIMUM HIGH
# ==========================================================

def get_overall_max(
    df
):

    high_column = df.columns[2]

    if df.empty:

        return None

    max_high = df[high_column].max()

    if pd.isna(max_high):

        return None

    return max_high


# ==========================================================
# GET MAXIMUM HIGH AFTER FIRST BUY DATE
# ==========================================================

def get_max_since_buy(
    df,
    buy_date
):

    date_column = df.columns[0]
    high_column = df.columns[2]

    filtered_df = df[
        df[date_column] >= buy_date
    ]

    if filtered_df.empty:

        return None

    max_high = filtered_df[high_column].max()

    if pd.isna(max_high):

        return None

    return max_high


# ==========================================================
# CALCULATE DIFFERENCE
# ==========================================================

def calculate_difference(
    overall_max,
    max_since_buy
):

    if (
        overall_max is None
        or max_since_buy is None
    ):

        return None

    return round(
        overall_max - max_since_buy,
        2
    )


# ==========================================================
# REPORT 1
# MAXIMUM HIGH SINCE FIRST BUY
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

    # ------------------------------------------------------
    # Check Folder
    # ------------------------------------------------------

    if not os.path.exists(folder_path):

        raise FileNotFoundError(
            f"Folder not found: {folder_path}"
        )

    # ------------------------------------------------------
    # Process XLSX Files
    # ------------------------------------------------------

    for file in os.listdir(folder_path):

        if not file.lower().endswith(
            ".xlsx"
        ):
            continue

        # Ignore temporary Excel files
        # such as ~$filename.xlsx

        if file.startswith("~$"):
            continue

        stock = get_stock_name(
            file
        )

        # --------------------------------------------------
        # Process only stocks available in buy-date file
        # --------------------------------------------------

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

            df = clean_dataframe(
                df
            )

            if df.empty:

                print(
                    f"No valid data found for {stock}"
                )

                continue

            buy_date = buy_dates[stock]

            overall_max = get_overall_max(
                df
            )

            max_since_buy = get_max_since_buy(
                df,
                buy_date
            )

            difference = calculate_difference(
                overall_max,
                max_since_buy
            )

            report.append({

                "Stock":
                    stock,

                "First Buy Date":
                    buy_date.strftime(
                        "%d-%m-%Y"
                    ),

                "Max Since First Bought":
                    None
                    if max_since_buy is None
                    else round(
                        max_since_buy,
                        2
                    ),

                "Overall Max":
                    None
                    if overall_max is None
                    else round(
                        overall_max,
                        2
                    ),

                "Difference":
                    difference

            })

        except Exception as e:

            print()
            print(
                f"Error processing {stock}"
            )

            print(e)

    # ------------------------------------------------------
    # No Report Data
    # ------------------------------------------------------

    if not report:

        return pd.DataFrame()

    # ------------------------------------------------------
    # Create Report DataFrame
    # ------------------------------------------------------

    report_df = pd.DataFrame(
        report
    )

    # ------------------------------------------------------
    # Sort Report
    # ------------------------------------------------------

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

    if df is None or df.empty:

        print()
        print(
            f"{report_name}: No data found."
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
# FUTURE REPORT
# MINIMUM PRICE
# ==========================================================

def report_min_price(
    folder_path,
    buy_date_file
):

    """
    Future Report:
    Minimum price after first buy date.
    """

    pass


# ==========================================================
# FUTURE REPORT
# CAGR
# ==========================================================

def report_cagr(
    folder_path,
    buy_date_file
):

    """
    Future Report:
    CAGR calculation.
    """

    pass


# ==========================================================
# FUTURE REPORT
# DRAWDOWN
# ==========================================================

def report_drawdown(
    folder_path,
    buy_date_file
):

    """
    Future Report:
    Maximum drawdown.
    """

    pass


# ==========================================================
# FUTURE REPORT
# VOLATILITY
# ==========================================================

def report_volatility(
    folder_path,
    buy_date_file
):

    """
    Future Report:
    Stock price volatility.
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
    # report_4 = report_drawdown(
    #     folder_path,
    #     buy_date_file
    # )
    #
    # print_report(
    #     report_4,
    #     "DRAWDOWN REPORT"
    # )


    #
    # report_5 = report_volatility(
    #     folder_path,
    #     buy_date_file
    # )
    #
    # print_report(
    #     report_5,
    #     "VOLATILITY REPORT"
    # )


# ==========================================================
# END OF FILE
# ==========================================================
