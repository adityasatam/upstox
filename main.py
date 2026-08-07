##############################################################
# INPUT
# Historical Upstox OHLC (.xlsx)
#
# OUTPUT
# Report 1 : Overall Maximum High
# Report 2 : Maximum High Since First Buy
# Report 3 : Difference
#
# Author : Aditya Satam
#
# Version History
# ------------------------------------------------------------
# 08-08-2026  Initial Version
# 08-08-2026  Added First Buy Date Report
# 08-08-2026  Added Difference Column
##############################################################

import os
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", None)
