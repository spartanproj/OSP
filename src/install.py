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
        print(p)
        subprocess.run(['mkdir', p])
        shutil.copy(fileName, f"{path}/kernel/packages/")
        

    # Now inject commands into the kernel
    
    with open(f"{path}/kernel/kernel.c", "r+") as f:
        content = f.readlines()
        f.seek(0, 0)
        for i,j in files.items():
            l = i.replace("kernel/", "")
            try:
                p = content.index(f'#include "{l}" // Extension: {json["exe"]["name"]}\n')
            except ValueError:
                content.insert(0, f'#include "{l}" // Extension: {json["exe"]["name"]}\n')
            f.seek(0)                 # file pointer locates at the beginning to write the whole file again
            f.writelines(content)
        modifyKernel(path, exe_letters, exe_name, json)
        

# Random VSC extension did this
def modifyKernel(path, exe_letters, exe_name, json):
    with open(f"{path}/kernel/util/cmd.h","r+") as k:
        lines = k.readlines()
    open(f"{path}/kernel/util/cmd.h", 'w').close()
    with open(f"{path}/kernel/util/cmd.h","r+") as k:
        i = lines.index("""\t\t if (typed[0]=="e" && typed[1]=="c" && typed[2]=="ENTER"){ \n""") # find random command in kernel
        command = '\t\telse if ('
        for j in range(exe_letters):
            command += f'typed[{j}]=="{exe_name[j]}"'
            if j != exe_letters-1:
                command += " && "
            else:
                o = j+1
        command += f' && typed[{o}] == "ENTER") '
        command += "{\n\t\t\t"
        command += json['exe']['name']
        command += "();\n\t\t\ttoclear=true;\n\t\t}\n\t\t"
        lines.insert(i, command)
        k.writelines(lines)
        print(f"{Colours.BOLD}")

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py.")
    print("To install spk, run install.sh")
