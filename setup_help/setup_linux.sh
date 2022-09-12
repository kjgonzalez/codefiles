#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install \
terminator \
chromium-browser \
python3-pip \
git \
kate \
pinta \
vim\
compizconfig-settings-manager \
unity-tweak-tool \
kompare \
python3-tk \
screen

sudo pip3 install --upgrade pip # after 1st run, just pip
pip install -r python_requirements.txt --user
# google tasks-only page: https://tasks.google.com/embed/?origin=https%3A%2F%2Fcalendar.google.com
