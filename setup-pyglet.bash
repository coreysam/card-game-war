#! /bin/bash
[[ "${BASH_SOURCE[0]}" != "${0}" ]] || (echo To run this script, type '"'source "$0"'"' in the terminal where you"'"ll be working. && exit 1) || return

function yes_no {
    read -n 1 -p "$1" REPLY
    echo
}

VERSION=$(python --version 2>&1 | sed 's/.* \([0-9]\.[0-9]\).*/\1/')
INSTALLED="$HOME/pyglet-installation"
PACKAGES="$INSTALLED/lib/python$VERSION/site-packages"

echo Updating PYTHONPATH.
export PYTHONPATH="$PACKAGES:$PYTHONPATH"

echo Updating PATH.
export PATH="$INSTALLED/bin:$PATH"

echo Installing.
REPLY='n'
if [ -e "$INSTALLED" ]
then
    yes_no "pyglet seems to already be installed.  Skip the installation step (Y/n)? "
fi

if [[ $REPLY =~ ^[Nn]$ ]]
then
    rm -rf "$INSTALLED"
    mkdir -p "$PACKAGES" || return
    easy_install --prefix="$INSTALLED" 'pyglet'
fi
