import sys
import ospHelp
from utils import Colours
import os
import search
import install
import update

args = sys.argv[1:] # find all arguments

update.updateosp()

try:
    if os.name == 'nt' or args[0] == "42":
        print(Colours.BOLD + Colours.RED + "ERROR: You are using Windows. OSP is not meant for Windows and will not work on Windows. Use " +Colours.GREEN+"mingw64" + Colours.RESET + Colours.BOLD + Colours.RED+" instead."+Colours.RESET)
except IndexError:
    ospHelp.ospHelp()
try:
    if args[0] in ["-h", "--help", ""]: # see if help is specified
        ospHelp.ospHelp() # call for help!
except IndexError: # if no args are specified
    ospHelp.ospHelp()

if args[0] == "install":
    package_info = search.search_for_packages(args)
    install.install_package(package_info["script"], args[1])