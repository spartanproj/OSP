#!/usr/bin/env bash

if [[ -t 1 ]]
then
    tty_escape() { printf "\033[%sm" "$1"; }
else
    tty_escape() { :; }
fi
tty_mkbold() { tty_escape "1;$1"; }
tty_blue="$(tty_mkbold 34)";
tty_red="$(tty_mkbold 31)";
tty_bold="$(tty_mkbold 39)";
tty_reset="$(tty_escape 0)";

# define functions
ring_bell() {
    # Use the shell's audible bell.
    if [[ -t 1 ]]
    then
        printf "\a"
    fi
}

getc() {
    local save_state
    save_state="$(/bin/stty -g)"
    /bin/stty raw -echo
    IFS='' read -r -n 1 -d '' "$@"
    /bin/stty "${save_state}"
}

# See if wget is installed
wget_installed=0
which wget && wget_installed=1
if (( wget_installed == 0 ))
then
    # worse way for detecting internet
    detection_out=$(ping google.com -c 2 | grep time)
    if [[ "$detection_out" == "" ]]
    then
        echo "${tty_red}${tty_bold}You do not have an internet connection. An internet connection is required for this script to run.${tty_reset}"
        echo "${tty_bold}Press any key to exit.${tty_reset}"
        getc c
        exit 1
    fi
elif (( wget_installed == 1 ))
then
    # better way to determine internet
    detection_out=$(wget -q http://detectportal.firefox.com/success.txt --timeout=10 -O - 2> /dev/null)
    if ! [[ "$detection_out" == "success" ]]
    then
        echo "${tty_red}${tty_bold}You do not have an internet connection. An internet connection is required for this script to run.${tty_reset}"
        echo "${tty_bold}Press any key to exit.${tty_reset}"
        getc c
        exit 1
    fi
fi

if ! [[ $1 == "--suppress-confirmation" ]]
then
    echo "${tty_bold}${tty_blue}==>${tty_reset}${tty_bold} This script will install:"
    echo "- nuitka to build the Python into a standalone executable"
    echo "- The downloaded script is located in your temp directory, it should be at $TEMPDIR."
    echo "- Will install the spk binary into /usr/bin (/usr/local/bin on macOS)"
    echo "${tty_bold}Python 2 is NOT SUPPORTED. Use Python 3 (ideally the latest version).${tty_reset}";
    echo
    echo "To continue, press ${tty_bold}RETURN/ENTER${tty_reset}. Press any other key to abort.";

    c="i want to get cancelled!!!!!";
    getc c;
    # we test for \r and \n because some stuff does \r instead
    if ! [[ "${c}" == $'\r' || "${c}" == $'\n' ]]
    then
        exit 1
    fi
fi

PIP_INSTALLED="no"
which pip > /dev/null && PIP_INSTALLED="pip"
which pip3 > /dev/null && PIP_INSTALLED="pip3"
if [[ "$PIP_INSTALLED" == "no" ]]
then
    echo "${tty_bold}${tty_red}ERROR: This script can't find pip in pip or pip3. If it is installed, alias your pip to pip or pip3.${tty_reset}";
    echo "${tty_bold}Python 2 is NOT SUPPORTED. Use Python 3 (ideally the latest version).${tty_reset}";
    exit 1
fi

PY_INSTALLED="no"
which python > /dev/null && PY_INSTALLED="python"
which python3 > /dev/null && PY_INSTALLED="python3"
if [[ "$PY_INSTALLED" == "no" ]]
then
    echo "${tty_bold}${tty_red}ERROR: This script can't find python in python or python3. If it is installed, alias your python to python or python3.${tty_reset}";
    echo "${tty_bold}Python 2 is NOT SUPPORTED. Use Python 3 (ideally the latest version).${tty_reset}";
    exit 1
fi

echo "${tty_bold}${tty_blue}==>${tty_reset}${tty_bold} Installing dependency nuitka${tty_reset}"
$PIP_INSTALLED install nuitka

echo "${tty_bold}${tty_blue}==>${tty_reset}${tty_bold} Cloning git repository${tty_reset}"
cd "$TMPDIR" || exit
rm -rf Spk > /dev/null
git clone https://github.com/spartanproj/Spk
cd Spk || exit
echo "${tty_bold}${tty_blue}==>${tty_reset}${tty_bold} Building file${tty_reset}"
$PY_INSTALLED -m nuitka --onefile src/main.py
mv main.bin spk
chmod +x main
echo "${tty_bold}${tty_blue}==>${tty_reset}${tty_bold} Moving the executable into your binaries folder${tty_reset}"

case $(uname) in
    Linux )
        mv spk /usr/bin/spk
        ;;
    Darwin )
        mv spk /usr/local/bin/spk
        ;;
  * )
        # Handle AmigaOS, CPM, and modified cable modems.
        mv spk /usr/bin/spk
        ;;
esac
echo "${tty_bold}${tty_blue}==>${tty_reset}${tty_bold} Cleaning up${tty_reset}"
rm -rf "$TEMPDIR/Spk"
echo "Delete git repository"
echo "${tty_bold}Done!${tty_reset}"