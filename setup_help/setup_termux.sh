#!/bin/bash
# NOTE: NOT YET TESTED AS OF 191217
pkg update
pkg upgrade
pkg install git \
openssh \
vim \
python

ssh-keygen

curl --L0 https://its-pointless.github.io/setup-pointless-repo.sh
bash setup-pointless-repo.sh
pkg install numpy

python -m pip install ipython --user

cd ~/codefiles
git config --global pull.rebase true
git config --global push.default simple
