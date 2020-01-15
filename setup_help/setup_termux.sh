#!/bin/bash
# NOTE: NOT YET TESTED AS OF 191217
# KJG200115: tested, fixed

pkg update
pkg upgrade
pkg install git openssh vim python

ssh-keygen

curl -L0 https://its-pointless.github.io/setup-pointless-repo.sh >> setup-pointless-repo.sh
bash setup-pointless-repo.sh
pkg install numpy
# pkg install scipy # not sure if want to install this quite yet
python -m pip install ipython --user

echo "export PATH=$PATH:/data/data/com.termux/files/home/.local/bin" >> ~/.bashrc
echo "source ~/codefiles/setup_help/bashrc_repo" >> ~/.bashrc

cd ~/codefiles
git config --global pull.rebase true
git config --global push.default simple
# git config --global user.name
# git config --global user.email
