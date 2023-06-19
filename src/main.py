import sys
import ospHelp
from utils import Colours
import os
import search
import install
import update

args = sys.argv[1:]  # find all arguments

update.updateosp()

try:
    if os.name == 'nt' or args[0] == "42":
        print(
            Colours.BOLD + Colours.RED + "ERROR: You are using Windows. OSP is not meant for Windows and will not "
                                         "work on Windows. Use " + Colours.GREEN + "mingw64" + Colours.RESET +
            Colours.BOLD + Colours.RED + " instead." + Colours.RESET)
except IndexError:
    ospHelp.ospHelp()
try:
    if args[0] in ["-h", "--help", ""]:  # see if help is specified
        ospHelp.ospHelp()  # call for help!
except IndexError:  # if no args are specified
    ospHelp.ospHelp()

if args[0] == "install":
    package_info = search.search_for_packages(args)
    try:
        idkwhythisisthevariablename = args[2]
    except IndexError:
        print(
            Colours.BOLD + Colours.RED + "ERROR: Please make sure that you have specified the path to your BlueberryOS files." + Colours.RESET)
    install.install_package(package_info, args[1], args[2])
elif args[0] == "info":
    package_info = search.search_for_packages(args)
    print(f"{Colours.BOLD}{Colours.GREEN}==> {Colours.RESET}{Colours.BOLD}{args[1]}{Colours.RESET}")
    print(f"Version: v{package_info['version']}")
    print(f"Author: {package_info['author']}")
    print(f"Description: {package_info['description']}")
    print(f"Link: {package_info['link']}")
elif args[0] == "update":
    status = update.updateosp()
    if status[0] == 1:
        print(f"{Colours.BOLD}You are on the latest version of OSP: {status[1]}")
    else:
        print(f"{Colours.BOLD}You have updated! New version: {status[1]}")
