#! /bin/bash

#!/bin/bash
echo "-------------------------WARNING-------------------------"
echo "This will write scripts to:"
echo "~/.config/autokey/data/scripts/right-shift-vi-like/"
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

autokeyDir=~/.config/autokey/data/scripts/right-shift-vi-like/

if [ ! -d $autokeyDir ]; then
  mkdir -p $autokeyDir
fi

cp src/* $autokeyDir

echo "..all done, review in 'autokey -> Show main window'"
