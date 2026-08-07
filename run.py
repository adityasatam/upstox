##############################################################
# INSTALL REQUIRED PACKAGES
##############################################################

import sys
import subprocess
import tempfile
import requests

requirements_url = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox/"
    "refs/heads/main/requirements.txt"
)

try:

    response = requests.get(
        requirements_url,
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
        "-r",
        temp_requirements
    ])

except Exception as e:

    print(f"Failed to install requirements : {e}")

    sys.exit(1)


##############################################################
# HOW TO USE
##############################################################

# 1. Download all historical Upstox (.xlsx) files.
#
# 2. Keep all files inside ONE folder.
#
# 3. Create first_buy_date.txt inside the same folder.
#
#    Example:
#
#    ADANIENT|11-07-2024
#    RELIANCE|20-01-2022
#    TCS|15-03-2020
#
# 4. Copy this run.py anywhere.
#
# 5. Change ONLY the folder_path below.
#
# 6. Run:
#
#       python run.py
#
##############################################################


##############################################################
# DOWNLOAD & EXECUTE main.py FROM GITHUB
##############################################################

main_url = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox/"
    "refs/heads/main/main.py"
)

response = requests.get(main_url)

if response.status_code == 200:

    exec(response.text)

    main(

        folder_path=r"C:\Users\sasuk\upstox\upstox_files",

        buy_date_file="first_buy_date.txt"

    )

else:

    print("Failed to download main.py from GitHub.")
