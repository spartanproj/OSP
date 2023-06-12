from utils import Colours
import subprocess

def install_package(script, name):
    print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing {Colours.GREEN}{name}{Colours.RESET}")
    subprocess.run(["curl", script], check=True)

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py")