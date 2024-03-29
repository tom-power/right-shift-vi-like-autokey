#! /bin/bash

#!/bin/bash
echo "-------------------------WARNING-------------------------"
echo "This will write settings to:"
echo "~/.config/autokey/data/scripts/vi/"
echo "anything there currently will be overwritten."
echo "-------------------------WARNING-------------------------"
read \
-n 1 \
-p "continue? (y/n): `echo $'\n> '`"
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "ok bye" && exit
fi

echo "copying.."

configDir=~/.config/autokey/data/scripts/vi/

if [ ! -d $configDir ]; then
  mkdir -p $configDir
fi

cp ./src/* $configDir

if  [ "$1" == "--with-extras" ]; then
  echo "copying extras.."
  cp ./src/extras/* $configDir
fi

echo "..all done, check they've been installed in the autokey main window"
