; Special Characters program
; Written by: Kristian Gonzalez

; KJGNOTE: this is for being able to write special characters in spanish and portuguese with relative ease, at least greater than without this script.

;included list of characters: 
;>>> á é í ñ ó ú ã ç õ

;KJGNOTE: 
;CTRL	^
;ALT	!
;SHIFT	+
;WIN	#
; KJG180302: as of now, latest autohotkey verison (1.1.28.00)
; 	requires users to write "Send, " before letters, as well 
; 	finishing the command with "Return"
;
#Persistent
Menu, Tray, Icon, esppor.ico

!a::Send, á
Return
!e::Send, é
Return
!i::Send, í
Return
!o::Send, ó
Return
!u::Send, ú
Return
!n::Send, ñ
Return

^+a::Send, ã
Return
^+c::Send, ç
Return
^+e::Send, ê
Return
^+o::Send, õ
Return

#a::Send, â
Return
#o::Send, ô
Return
#+e::Send, ê
Return

; test section
#e::Send, ô
Return
; ß





!/::Send, ¿
Return
!1::Send, ¡
Return
^+u::Send, ü
Return

	;^+1::Send, ¡
	;!q::Send, ¡
	;!p::Send, ü
	;!y::Send, ¿

!`::Send, à
Return

!0::Send, °
Return


;eof