import sys
import subprocess
import tempfile
import requests


# ======================================================
# USER CONFIGURATION
#
# Modify ONLY the below parameters.
# ======================================================

FOLDER_PATH = r"C:/Users/sasuk/my_projects/upstox_sell_alert/upstox_files/"

BUY_DATE_FILE = "first_buy_date.txt"


# ======================================================
# GITHUB CONFIGURATION
# ======================================================

GITHUB_RAW_BASE = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox_sell_alert/main/"
)

REQUIREMENTS_URL = GITHUB_RAW_BASE + "requirements.txt"

MAIN_URL = GITHUB_RAW_BASE + "main.py"


# ======================================================
# DOWNLOAD AND INSTALL REQUIRED PACKAGES
# ======================================================

try:

    response = requests.get(
        REQUIREMENTS_URL,
        timeout=30
    )

    response.raise_for_status()

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        delete=False
    ) as f:

        f.write(response.text)

        temp_requirements = f.name

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "--quiet",
        "--disable-pip-version-check",
        "-r",
        temp_requirements
    ])

except Exception as e:

    print("\nFailed to install requirements.")
    print(e)

    sys.exit(1)


# ======================================================
# DOWNLOAD LATEST main.py FROM GITHUB
# ======================================================

try:

    response = requests.get(
        MAIN_URL,
        timeout=30
    )

    response.raise_for_status()

    main_code = response.text

except Exception as e:

    print("\nUnable to download main.py.")
    print(e)

    sys.exit(1)


# ======================================================
# EXECUTE main.py
# ======================================================

try:

    exec(
        main_code,
        globals()
    )

except Exception as e:

    print("\nFailed to load main.py.")
    print(e)

    sys.exit(1)


# ======================================================
# RUN
# ======================================================

main(
    folder_path=FOLDER_PATH,
    buy_date_file=BUY_DATE_FILE
)
