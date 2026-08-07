import sys
import subprocess
import tempfile
import requests

# ==========================================================
# INSTALL REQUIREMENTS
# ==========================================================

REQUIREMENTS_URL = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox/"
    "refs/heads/main/requirements.txt"
)

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
        "-r",
        temp_requirements
    ])

except Exception as e:

    print(f"Failed to install requirements:\n{e}")
    sys.exit(1)

# ==========================================================
# USER INSTRUCTIONS
# ==========================================================

# 1. Download all Upstox Historical Data (.xlsx) files.
#
# 2. Keep all files in one folder.
#
# 3. Modify only the folder_path below.
#
# 4. Run:
#
#       python run.py

# ==========================================================
# DOWNLOAD MAIN.PY
# ==========================================================

MAIN_URL = (
    "https://raw.githubusercontent.com/"
    "adityasatam/upstox/"
    "refs/heads/main/main.py"
)

try:

    response = requests.get(
        MAIN_URL,
        timeout=30
    )

    response.raise_for_status()

except Exception as e:

    print(f"Failed to download main.py:\n{e}")
    sys.exit(1)

# ==========================================================
# EXECUTE MAIN.PY
# ==========================================================

namespace = {}

exec(response.text, namespace)

# ==========================================================
# RUN PROGRAM
# ==========================================================

namespace["main"](

    folder_path=r"C:\Users\sasuk\upstox\upstox_files"

)
