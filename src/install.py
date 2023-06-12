import subprocess
from utils import Colours


def install_package(script, name) -> int:
    print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing {Colours.GREEN}{name}{Colours.RESET}")
    subprocess.run(["curl", script], check=True)
    
    return 0

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py.")
    print("To install spk, run install.sh")