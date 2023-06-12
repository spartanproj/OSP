from urllib.request import urlopen, urlretrieve
import json
from utils import Colours
import subprocess
import tempfile
import platform
from pathlib import Path
import shutil
import zipfile

def updateSpk(currentVersion):
    with urlopen("https://raw.githubusercontent.com/spartan-os/osp-packages/main/packages.json") as url:
        index = json.load(url)
    print(index)
    latestVersion = index["spk"]["latest-version"]
    if currentVersion != latestVersion:
        getUpdate(latestVersion, index)


# TODO Rename this here and in `updateSpk`
def getUpdate(latestVersion, index):
    print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing update to spk: {Colours.GREEN}v{latestVersion}{Colours.RESET}")
    temp_folder = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
    zipFile = urlretrieve(index["spk"]["link-to-code"], "spk_update.zip")
    shutil.move("spk_update.zip", temp_folder)
    newPath = temp_folder.joinpath("spk_update.zip")
    with zipfile.ZipFile(newPath, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)
    newPath = temp_folder.joinpath("Spk-main")
    