;Special Characters program, for German
;Written by: Kristian Gonzalez
;Objective: this is for being able to write special 
;   characters in german with relative ease, at least 
;   greater than without this script.
; NOTES:
;* KJGNOTE: this is a workaround to using a single script to
;    handle spanish, portuguese, AND german. in the future, 
;    may have a way to combine all together.
;* autohotkey: "autocorrect/replace: ::Send, string::Send, replacement
;* grouping everything by input method / combination, 
;    alphabetical order
; KJG180302: as of now, latest autohotkey verison (1.1.28.00)
; 	requires users to write "Send, " before letters, as well 
; 	finishing the command with "Return"
;
;* CTRL ^  //  ALT !  //  SHIFT +  //  WIN #
;// SCRIPT START ///////////////////////////////////////////
#Persistent
Menu, Tray, Icon, D:\Documents2\Dropbox\DesignStudies\Software\AutoHotKey\ger.ico

!a::Send, ä
Return
!o::Send, ö
Return
!u::Send, ü
Return
!s::Send, ß
Return
!0::Send, °
Return

;uppercase (since so few special chars in german, convenient)
!+a::Send, Ä
Return
!+o::Send, Ö
Return
!+u::Send, Ü
Return

;eof