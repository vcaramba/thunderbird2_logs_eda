import subprocess
import sys
import logging

def install():
    packages_to_install = [
        "jupyter",
        "dask[complete]",
        "pandas",
        "pandasql"
    ]

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    for package in packages_to_install:
        try:
            import pip
        except ImportError:
            print("installing pip")
            cmd = "sudo easy_install pip"
            subprocess.call([sys.executable, cmd])

        subprocess.call([sys.executable, "-m", "pip", "install", package])
