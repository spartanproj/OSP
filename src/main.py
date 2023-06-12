import sys
import SpkHelp
from utils import Colours
import os
import search
import install
import update

args = sys.argv[1:] # find all arguments

update.updateSpk("0.0.1")

try:
    if os.name == 'nt' or args[0] == "42":
        print(Colours.BOLD + Colours.RED + "ERROR: You are using Windows. OSP is not meant for Windows and will not work on Windows. Use " +Colours.GREEN+"mingw64" + Colours.RESET + Colours.BOLD + Colours.RED+" instead."+Colours.RESET)
except IndexError:
    SpkHelp.SpkHelp()
try:
    if args[0] in ["-h", "--help", ""]: # see if help is specified
        SpkHelp.SpkHelp() # call for help!
except IndexError: # if no args are specified
    SpkHelp.SpkHelp()

if args[0] == "install":
    package_info = search.search_for_packages(args)
    install.install_package(package_info["script"], args[1])