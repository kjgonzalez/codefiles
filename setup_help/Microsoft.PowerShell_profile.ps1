# Created: 190507

# Pre-Installation (assuming Git is installed)
# 1. open powershell as admin
# 2. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned ("A", yes to all)
# 3. close admin powershell
# 4. open powershell at ~/
# 5. run "ssh-keygen"
# 6. copy *.pub data and put into git
# 7. git clone (this repo)

# Installation & Setup: 
# 1. copy this script to the local profile folder, e.g. ~\Documents\WindowsPowerShell\ (per Win11 instructions, look at $PROFILE variable)
# 2. modify / disable all relevant aliases
# 3. activate python env, install modules. run: ipython numpy matplotlib pandas openpyxl
# 4. run: ipython profile create (latest instructions: https://ipython.readthedocs.io/en/stable/config/intro.html#setting-configurable-options)
# 5. edit ipython profile, use line: c.InteractiveShell.separate_in = ''
# 6. 


# Objective: a windows-version ".bashrc" file that can help preload helpful commands.
# Save this file at ~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
# another way to check path : echo $PROFILE.CurrentUserCurrentHost

# function ipython {ipython.exe --nosep} # not necessary
# first time setup of ipython: 
# 1. (go into relevant venv as needed)
# 2. >> ipython profile create
# 3. open relevant file, e.g. "~\.ipython\profile_default\ipython_config.py"
# 4. change following fields: 
#   a. c.TerminalInteractiveShell.highlighting_style = "one-dark" # good color
#   b. c.InteractiveShell.separate_in = '' # same as --nosep

echo "KJG functions/tips"
echo "  activate:   activate vemain "
echo "  foxit:      open PDF file in Foxit"
echo "  ipython:    run interactive python (only after 'activate')"
echo "  npp:        open file in notepad++"
echo "  sumatra:    open PDF file in Sumatra"
echo "  tip:        diff FILEA FILEB  (compare two files in vscode)"


Set-Alias -Name activate -Value "C:\Users\kjg\vemain\Scripts\Activate.ps1"
Set-Alias -Name foxit -Value "C:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitReader.exe"
Set-Alias -Name npp -Value "C:\Program Files\Notepad++\notepad++.exe"
Set-Alias -Name sumatra -Value "C:\Program Files\SumatraPDF\SumatraPDF.exe"




# old code, requires MinGW or similar installed on system
#function cpprun{
#    echo "SYSTEM: building..."
#    g++ -std=c++11 $args
#    if($?){
#        echo "SYSTEM: Success, running..."
#        echo ""
#        .\a.exe
#    }
#}

# todo: re-add "fgrep"




