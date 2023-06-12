# I need help!
import sys

def SpkHelp(arg=""):
    if arg == "":
        print("""
Usage: spk [options] [path-to-os] [name]

Arguments:
  spk -s|--shipment install|search|info|upgrade    Manipulate a shipment (group of packages)

Package manipulation:
  spk search TEXT    Searches for a package
  spk info PACKAGE    Tells you some info about a package
  spk install PACKAGE    Install a package
  spk update    Update spk
  spk upgrade [PACKAGE]    Upgrade a package

Debugging:
  spk install PACKAGE --debug    Install a package with all the logs

Help:
  spk -h|--help    Displays this help menu
  https://github.com/spartan-nerdos/spk
              """)
        sys.exit()

if __name__ == "__main__":
    print("This file is not meant to be ran! Run main.py")