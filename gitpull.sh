#!/bin/bash

cd ~/Team-Peyton/
/usr/bin/git pull origin master > git_output

python3 media.py &
# @reboot ~/gitpull.sh
