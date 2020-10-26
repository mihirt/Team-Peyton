#!/bin/bash

cd ~/Team-Peyton/
/usr/bin/git pull origin master

python3 media.py &
# @reboot ~/gitpull.sh
