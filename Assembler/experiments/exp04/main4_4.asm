DATA SEGMENT
    DATAA DB 12H
    DATAB DB 23H
    DATAC DB 34H
    TABL DB 45H
    RESULT DW ?
DATA ENDS

CODE SEGMENT
    ASSUME DS:DATA, CS:CODE

START:
    MOV AX, DATA
    MOV DS, AX

    ; Load X into AX
    MOV AL, TABL

    ; Calculate X^2
    MUL AL
    MOV BX, AX

    ; Multiply by A
    MOV AL, DATAA
    MUL BX
    MOV CX, AX

    ; Calculate B*X
    MOV AL, DATAB
    MUL TABL
    ADD AX, CX

    ; Add C
    ADD AL, DATAC
    ADC AH, 0

    ; Store the result in RESULT
    MOV RESULT, AX

    MOV AH, 4CH
    INT 21H
CODE ENDS
END START