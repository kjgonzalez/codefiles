; Special Characters program
; Written by: Kristian Gonzalez

; KJGNOTE: this is for being able to write special characters in spanish and portuguese with relative ease, at least greater than without this script.

;included list of characters: 
;>>> � � � � � � � � �

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

!a::Send, �
Return
!e::Send, �
Return
!i::Send, �
Return
!o::Send, �
Return
!u::Send, �
Return
!n::Send, �
Return

^+a::Send, �
Return
^+c::Send, �
Return
^+e::Send, �
Return
^+o::Send, �
Return

#a::Send, �
Return
#o::Send, �
Return
#+e::Send, �
Return

; test section
#e::Send, �
Return
; �





!/::Send, �
Return
!1::Send, �
Return
^+u::Send, �
Return

	;^+1::Send, �
	;!q::Send, �
	;!p::Send, �
	;!y::Send, �

!`::Send, �
Return

!0::Send, �
Return


;eof