; Created by Jacobus Burger (2019)
;
; Info:
;		One of my first programs. The very first was action-script (man I'm old).
;		Just a bog-standard hello world program written in assembly.
section .data
	msg db "你好, 世界!", 10, "Bonjour, le monde!", 10, "Hello, World!", 10, 0
	len equ $ - msg

section .text
	global _start

_start:
	mov edx, len
	mov ecx, msg
	mov ebx, 1
	mov eax, 4
	int 80h
	mov eax, 1
	int 80h
    ret
