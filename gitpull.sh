#!/bin/bash

cd ~/Team-Peyton/
git pull origin master

python3 media.py &
# @reboot ~/gitpull.sh
