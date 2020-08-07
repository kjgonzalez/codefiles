
; For ASUS FX305 (Hades), show 
if (GetKeyState("NumLock", "T"))  ; get the toggle-state of NumLock
	#Persistent
	Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 44 ; change icon (on)
else
	#Persistent
	Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 110 ; change icon (off)

~Numlock::  ; detect NumLock without blocking it (~)
    if (GetKeyState("NumLock", "T"))  ; get the toggle-state of NumLock
        #Persistent
		Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 44 ; change icon (on)
    else
		#Persistent
		Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 110 ; change icon (off)
    return
