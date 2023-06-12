# I need help!
import sys

def SpkHelp(arg=""):
    if arg == "":
        print("""
Usage: osp [options] [path-to-os] [name]

Package manipulation:
  osp search TEXT    Searches for a package
  osp info PACKAGE    Tells you some info about a package
  osp install PACKAGE    Install a package
  osp update    Update osp
  osp upgrade [PACKAGE]    Upgrade a package

Debugging:
  osp install PACKAGE --debug    Install a package with all the logs

Help:
  osp -h|--help    Displays this help menu
  https://github.com/spartan-nerdos/osp
              """)
        sys.exit()

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py")