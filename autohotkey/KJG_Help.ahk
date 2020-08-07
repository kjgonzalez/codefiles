; Author: Kris Gonzalez
; Objective: runtime help script, augment / modify some behavior on computer

; For ASUS FX305 (Hades), show on icon when numlock on/off (star, illegal icon)
if (GetKeyState("NumLock", "T"))  ; get the toggle-state of NumLock
	#Persistent
	Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 44 ; change icon (on)
else
	#Persistent
	Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 110 ; change icon (off)

;keep a window on top
#SPACE:: Winset,Alwaysontop, ,A

; tilde / zero modification
;`::Send {0}

; F1 denial and hotkey
;F1::Esc
;^`::Send {F1}

NumpadMult::Send {Volume_Up}
NumpadDiv::Send {Volume_Down}



~Numlock::  ; detect NumLock without blocking it (~)
    if (GetKeyState("NumLock", "T"))  ; get the toggle-state of NumLock
        #Persistent
		Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 44 ; change icon (on)
    else
		#Persistent
		Menu, Tray, Icon, %A_WinDir%\System32\shell32.dll, 110 ; change icon (off)
    return


; <> -------------- ENDNOTES ---------------- <>
; PLEASE begin this script with work computer (Win7 computer)

;CTRL	^
;ALT	!
;SHIFT	+
;WIN	#
;single hotkey editing: !_::_ >>> "pressing ALT+_ inputs character _"
;"autocorrect/replace: ::string::replacement

; eof
