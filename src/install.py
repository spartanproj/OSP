import subprocess
from utils import Colours
from urllib.request import urlretrieve
import tempfile
import subprocess
import tempfile
from pathlib import Path
import shutil
import os


def install_package_deprecated(script, name) -> int:
    print(f"{Colours.RED}{Colours.BOLD}You should not use this as it is deprecated. Most packages do not support installing this way.{Colours.RESET}")
    print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing {Colours.GREEN}{name}{Colours.RESET}")
    temp_folder = Path(tempfile.gettempdir())
    shFile = urlretrieve(script, "install.sh")
    shutil.copy("install.sh", temp_folder)
    newPath = temp_folder.joinpath("install.sh")

    # Hand it over to install.sh
    subprocess.run(["chmod", "+x", newPath.absolute()])
    subprocess.run(["bash", newPath.absolute()])
    return 0

def install_package(json, name, path) -> int:
    print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing {Colours.GREEN}{name}{Colours.RESET}")
    exe_name = list(json['exe']['name'])
    exe_letters = len(exe_name)
    files = json['exe']['files']
    temp_folder = Path(tempfile.gettempdir())
    os.chdir(temp_folder.absolute())
    for i,j in files.items():
        print(j)
        fileName = i.split("/")[-1] # Find last value in list, therefore file name
        urlretrieve(j, fileName)
        p = f"{path}/kernel/packages"
        subprocess.run(['mkdir', p])
        shutil.copy(fileName, f"{path}/kernel/packages/")

    # Now inject commands into the kernel
    with open(f"{path}/kernel/kernel.c", "a+") as k:
        k.seek(0)
        for i,j in files.items():
            l = j.replace("kernel/", "")
            k.write("#include {l} // Extension: {exe_name}")
        modifyKernel(k, exe_letters, exe_name, json)

# Random VSC extension did this
def modifyKernel(k, exe_letters, exe_name, json):
    lines = k.readlines()
    print(lines)
    i = lines.index("""if (typed[0]=="e" && typed[1]=="c" && typed[2]=="ENTER"){""") # find random command in kernel
    command = 'else if ('
    for j in range(exe_letters):
        command += f"typed[{j}]=='{exe_name[j]}'"
        if j != exe_letters-1:
            command += " && "
    command += ") { "
    command += json['exe']['name']
    command += "() }"
    print(command)
    lines.insert(i, command)

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py.")
    print("To install spk, run install.sh")
