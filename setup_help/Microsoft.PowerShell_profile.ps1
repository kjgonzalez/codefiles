# Objective: A windows-specific ".bashrc" file that can help preload helpful commands.
# Save this file at ~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
# another way to check path : echo $PROFILE.CurrentUserCurrentHost
#
# First time setup of ipython: 
# 1. (go into relevant venv as needed)
# 2. >> ipython profile create
# 3. open relevant file, e.g. "~\.ipython\profile_default\ipython_config.py"
# 4. change following fields: 
#   a. c.TerminalInteractiveShell.highlighting_style = "one-dark" # good color
#   b. c.InteractiveShell.separate_in = '' # same as --nosep
#
# First time setup of g++ & other tools via MinGW
# src: https://code.visualstudio.com/docs/cpp/config-mingw
# 1. install msys2 https://www.msys2.org/
# 2. install somewhere convenient (e.g. C:/programs/msys64)
# 3. run msys shell, or run "MSYS2 MSYS" shell
# 4. run command: pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
#   a. ENTER to install all
#   b. 'Y' to install 
# 5. add bin folder of install (e.g. C:\programs\msys64\ucrt64\bin) to "Path" environment variable

echo "KJG commands"
echo "  activate:   activate 'main' venv"
echo "  cpprun XX:  build and run (if built) basic cpp script"
echo "  foxit XX:   open pdf file in Foxit"
echo "  npp XX:     open text file in Notepad++"
echo "  ipython:    run iPython --nosep (need active venv)"
echo "  sumatra XX: open pdf file in Sumatra"

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
