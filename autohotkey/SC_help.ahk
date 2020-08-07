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
;single hotkey editing: !_::_ >>> "pressing ALT+_ inputs character _"

;"autocorrect/replace: ::string::replacement
^j::Send, My First Script
Return

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

!n::ñ
Return

^+a::ã
Return

^+c::ç
Return

^+e::ê
Return

^+o::õ
Return

#a::â
Return

#o::ô
Return

#+e::ê
Return

; test section
#e::ô
Return
; ß
;Return





!/::¿
!1::¡
^+u::ü

	;^+1::¡
	;!q::¡
	;!p::ü
	;!y::¿

!`::à

!0::°


;done