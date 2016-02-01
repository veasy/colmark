#!/usr/bin/env bash

if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform
    echo "install autopy on MacOSX..."
    # specialized install of autopy
    # brew install libpng
    # CFLAGS="-Wno-return-type" pip install git+https://github.com/potpath/autopy.git

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under Linux platform
    sudo apt-get install libxtst-dev
    # apt-get install libpng-dev zlib1g-dev

elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    # Do something under Windows NT platform
    echo "nothing to install here..."
fi

sudo pip install -r requirements.txt