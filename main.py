import sys
import help
from utils import Colours
import utils
import urllib.request
import json
import subprocess
import os

args = sys.argv[1:] # find all arguments

if os.name == 'nt':
    print(Colours.BOLD + Colours.RED + "ERROR: You are using Windows. OSP is not meant for Windows and will not work on Windows. Use " +Colours.GREEN+"mingw64" + Colours.RESET + Colours.BOLD + Colours.RED+" instead."+Colours.RESET)

try:
    if args[0] in ["-h", "--help", ""]: # see if help is specified
        help.help() # call for help!
except IndexError: # if no args are specified
    help.help()

if args[0] == "install":
    #try:
        package = args[1]
        with urllib.request.urlopen("https://raw.githubusercontent.com/spartan-os/osp-packages/main/packages.json") as url:
            index = json.load(url)
        print(index)
        category = package.split("/",1)[0]
        name = package.split("/",1)[1]
        print(category)
        print(name)
        try:
            package_info = index["packages"][category][name]
            print(f"{Colours.BOLD}{Colours.BLUE}==>{Colours.RESET}{Colours.BOLD} Installing {Colours.GREEN}{name}{Colours.RESET}")
            rc = subprocess.run(["curl", package_info['script']])
        except KeyError:
            print(f"{Colours.BOLD}{Colours.RED}ERROR: package does not exist or you do not have a proper internet connection.{Colours.RESET}")
        #except Exception as e:
            #print(
                #f"{Colours.BOLD}{Colours.RED}ERROR: Something unexpected happened: Error: {type(e).__name__}{Colours.RESET}"
            #)
    #except Exception:
        #print(Colours.BOLD + Colours.RED + "ERROR: No arguments specified for install. Quitting." + Colours.RESET)