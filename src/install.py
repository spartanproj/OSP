import subprocess
from utils import Colours
from urllib.request import urlretrieve
import tempfile
import subprocess
import tempfile
from pathlib import Path
import shutil


def install_package(script, name) -> int:
    print(
        f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing {Colours.GREEN}{name}{Colours.RESET}")
    temp_folder = Path(tempfile.gettempdir())
    shFile = urlretrieve(script, "install.sh")
    shutil.copy("install.sh", temp_folder)
    newPath = temp_folder.joinpath("install.sh")

    # Hand it over to install.sh
    subprocess.run(["chmod", "+x", newPath.absolute()])
    subprocess.run(["bash", newPath.absolute()])
    return 0


if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py.")
    print("To install spk, run install.sh")
