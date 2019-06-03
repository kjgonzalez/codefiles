'''
date: 190603
objective: auto-sync git stuff when possible, to ensure better connectivity when working remotely.

general steps:
0. check if unsaved work locally
1. git pull
1a. if error, pause and exit... ?
2. git status
3. git auto-commit
4. try to git push
5. if branch problems, then state error and exit

'working tree clean' == no unsaved local work

'Untracked files' == unsaved new local work
'Changes not staged for commit' == unsaved modified local work

https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files

to hard-overwrite local changes:
    git fetch --all
    git reset --hard origin/master

'''

import sys, os
import ipdb

def git_status():
    return os.popen('git status').read()

def git_add():
    return os.popen('git add -A').read()
def git_commit():
    return os.popen("git commit -a -m 'auto-commit'").read()

def git_pull():
    # here, need to notify if have a merge conflict
    return os.popen("git pull").read()

def git_push():
    # what if get a merge conflict while pushing?
    return os.popen('git push').read()

def is_clean():
    if('nothing to commit, working tree clean' in git_status()):
        return True
    else:
        return False

print('starting test')
if(not is_clean()):
    print('need to commit local')
    print(git_status())
    print('committing')
    git_add()
    git_commit()
print('pulling first')
git_pull()
print('pushing')
git_push()
