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
    
    with urlopen("https://raw.githubusercontent.com/spartanproj/spk-packages/main/packages.json") as url:
        index = json.load(url)
    latestVersion = index["spk"]["latest-version"]
    if currentVersion != latestVersion:
        getUpdate(latestVersion, index)



def getUpdate(latestVersion, index):
    print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing update to spk: {Colours.GREEN}v{latestVersion}{Colours.RESET}")
    temp_folder = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
    shFile = urlretrieve(index["spk"]["link-to-script"], "spk_update.sh")
    shutil.copy("spk_update.sh", temp_folder)
    newPath = temp_folder.joinpath("spk_update.sh")
    
    # Hand it over to install.sh
    subprocess.run(["chmod", "+x", newPath.absolute()])
    subprocess.run([newPath.absolute(), "--suppress-confirmation"])