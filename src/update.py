from urllib.request import urlopen, urlretrieve
import json
from utils import Colours
import subprocess
import tempfile
import platform
from pathlib import Path
import shutil


def updateosp():
    # UPDATE: latest version
    currentVersion = "0.0.1"

    with urlopen("https://raw.githubusercontent.com/spartanproj/osp-packages/main/packages.json") as url:
        index = json.load(url)
    latestVersion = index["osp"]["latest-version"]
    if currentVersion != latestVersion:
        getUpdate(latestVersion, index)
        return [0, currentVersion]
    else:
        return [1, currentVersion]


def getUpdate(latestVersion, index):
    print(
        f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing update to osp: {Colours.GREEN}v{latestVersion}{Colours.RESET}")
    temp_folder = Path(tempfile.gettempdir())
    shFile = urlretrieve(index["osp"]["link-to-script"], "osp_update.sh")
    shutil.copy("osp_update.sh", temp_folder)
    newPath = temp_folder.joinpath("osp_update.sh")

    # Hand it over to install.sh
    subprocess.run(["chmod", "+x", newPath.absolute()])
    subprocess.run([newPath.absolute(), "--suppress-confirmation"])
