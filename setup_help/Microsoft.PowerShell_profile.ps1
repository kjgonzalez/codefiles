# Created: 190507
# Objective: a windows-version ".bashrc" file that can help preload helpful commands.
# Save this file at ~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1

# function ipython {ipython.exe --nosep} # not necessary
# first time setup of ipython: 
# 1. (go into relevant venv as needed)
# 2. >> ipython profile create
# 3. open relevant file, e.g. "~\.ipython\profile_default\ipython_config.py"
# 4. change following fields: 
#   a. c.TerminalInteractiveShell.highlighting_style = "one-dark" # good color
#   b. c.InteractiveShell.separate_in = '' # same as --nosep

Set-Alias -Name sumatra -Value "C:\Program Files\SumatraPDF\SumatraPDF.exe"
Set-Alias -Name npp -Value "C:\Program Files (x86)\Notepad++\notepad++.exe"
Set-Alias -Name foxit -Value "D:\Programs2\FoxitReader\FoxitReader.exe"
Set-Alias -Name activate -Value "C:\Users\kjg\vemain\Scripts\Activate.ps1"

function cpprun{
    echo "SYSTEM: building..."
    g++ -std=c++11 $args
    if($?){
        echo "SYSTEM: Success, running..."
        echo ""
        .\a.exe
    }
}
