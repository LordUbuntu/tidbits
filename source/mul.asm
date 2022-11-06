; Jacobus Burger (2022)
; Info:
;   multiply two numbers together in ASM without using mul opcode

; define two numbers to start with
section .rodata
        a db 2
        b db 6

; set program start point
section .text
        global _start

_start:
        mov ecx, a  ; set counter to multiplier
        mov eax, 0  ; set accumulator to multiplicand
multiply:
        add eax, b
        dec ecx
        jnz multiply
        ret
