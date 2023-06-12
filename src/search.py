import urllib, json
from utils import Colours

def search_for_packages(args):
    try:
        package = args[1]
    except IndexError:
        print(Colours.BOLD + Colours.RED + "ERROR: No arguments specified for install. Quitting." + Colours.RESET)
    with urllib.request.urlopen("https://raw.githubusercontent.com/spartan-os/osp-packages/main/packages.json") as url:
        index = json.load(url)
    print(index)
    category = package.split("/",1)[0]
    name = package.split("/",1)[1]
    try:
        return index["packages"][category][name]
    except KeyError:
        print(Colours.BOLD + Colours.RED + "ERROR: Package not found or you do not have an internet connection." + Colours.RESET)

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py")