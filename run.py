import sys
import subprocess
import tempfile
import requests

# ==========================================================
# INSTALL REQUIREMENTS
# ==========================================================

requirements_url = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox_stock_summary/"
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

    print(f"Failed to install requirements: {e}")

    sys.exit(1)

# ==========================================================
# USAGE
# ==========================================================

# 1) Download all Upstox historical .xlsx files.
#
# 2) Keep all .xlsx files inside one folder.
#
# 3) Copy this run.py into any folder.
#
# 4) Modify only the folder_path parameter below.
#
# 5) Run:
#
#    python run.py

# ==========================================================
# DOWNLOAD & EXECUTE MAIN
# ==========================================================

main_url = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox/"
    "refs/heads/main/main.py"
)

response = requests.get(main_url)

if response.status_code == 200:

    exec(response.text)

    main(

        folder_path=r"C:\Users\sasuk\upstox\upstox_files"

    )

else:

    print("Failed to download main.py from GitHub.")
