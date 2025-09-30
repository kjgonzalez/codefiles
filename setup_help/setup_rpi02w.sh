# RPI Zero 2 W starter script
# versions as of 250913
# git 2.39.5
# cmake 3.25.1
# screen 4.09
# vim 9.0
sudo apt-get update
# sudo apt-get upgrade -y # perhaps not recommended?

sudo apt install git cmake screen vim -y
# todo: samba server
# sudo apt install samba samba-common-bin
cd ~/
python -m venv vemain
. vemain/bin/activate
python -m pip install numpy pandas ipython pyserial

# add ~/.bashrc info
# todo: add some logic to decide whether to add
# # KJG Section =================================
# 
# echo "KJG functions/tips"
# echo "  activate:   activate vemain"
# echo "  sn:         new screen socket"
# echo "  sr:         reattach to socket"
# echo "  sl:         list sockets"
# echo "  CTRL+A,D:   detach from socket"
# echo "  tip: kill socket by entering & 'exit'"
# 
# alias activate=". ~/vemain/bin/activate"
# alias sn="screen -S $arg1"  # new socket
# alias sr="screen -r $arg1"  # reattach to socket
# alias sl="screen -ls"       # list active sockets
# # manual detach: enter session & press CTRL+A,D
# # manual kill: enter session & type "exit". (delete is sr <ScrName>, exit)

# add ~/.vimrc info
echo "setup ~/.vimrc..."
echo "\" vim runtime configuration (via script)" >> ~/.vimrc
echo "" >> ~/.vimrc
echo ":set expandtab" >> ~/.vimrc
echo ":set shiftwidth=4" >> ~/.vimrc
echo ":set tabstop=4" >> ~/.vimrc
echo ":set autoindent" >> ~/.vimrc
echo "\" eof" >> ~/.vimrc
echo "" >> ~/.vimrc

# config git
# note: correctly configured pi will be called pi<LETTER>, e.g. pia
echo "configuring git..."z
git config --global user.email k@j
git config --global user.name $USER
git config --global pull.rebase true
git config --global push.default simple

