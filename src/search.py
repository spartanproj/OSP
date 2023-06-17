import json
from urllib.request import urlopen
from utils import Colours
import sys


def search_for_packages(args):
    try:
        package = args[1]
    except IndexError:
        print(Colours.BOLD + Colours.RED + "ERROR: No arguments specified for search. Quitting." + Colours.RESET)
    with urlopen("https://raw.githubusercontent.com/spartan-os/osp-packages/main/packages.json") as url:
        index = json.load(url)
    category = package.split("/", 1)[0]
    try:
        name = package.split("/", 1)[1]
    except IndexError:
        print(
            Colours.BOLD + Colours.RED + "ERROR: All packages have four categories: extras, experiments, community and themes. Example: osp install extras/marvin-adventures" + Colours.RESET)
        sys.exit()
    try:
        return index["packages"][category][name]
    except KeyError:
        print(
            Colours.BOLD + Colours.RED + "ERROR: Package not found or you do not have an internet connection." + Colours.RESET)
        sys.exit()


if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py")
