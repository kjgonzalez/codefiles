# codefiles

Objective: unify all code in all locations, and enable simple way to have all code in one place, with revision control. have chosen to avoid dropbox out of deference to ubuntu and git functionality. windows will be outfitted with git to match. finally, code may be moved or copied
## Overall Layout of this Repository
1. catkin_ws for ROS packages / ROS-related work
2. *_sandbox folders for testing assorted programming ideas
3. scripts folder for running useful, live code
 
### establish kjg repo on new computer
(for all steps, refer to bash_help.txt)
1. generate ssh key & upload
2. clone repo
3. set rebase: git config --global pull.rebase true


KJGNOTE: moving repo / user a to a new location:
if get this message: "remote: This repository moved. Please use the new location", then simply do this:
git remote set-url origin [updated link url https://........git]

src: https://stackoverflow.com/questions/30443333/error-with-renamed-repo-in-github-remote-this-repository-moved-please-use-th

abc



eof
