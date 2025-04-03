DATA SEGMENT
    X SBYTE 10H
    Y SBYTE 10H
    Z SBYTE 5H
    SUM DW ?
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA

START:
    MOV AX, DATA
    MOV DS, AX

    MOV AH, 0H
    MOV AL, X
    MOV BL, Y
    ADD AL, BL

    ; 比较X + Y 和 200
    CMP AL, 200
    JB  NOT_OVER_200

    ; 如果X + Y > 200，计算X - Z
    MOV AL, X
    MOV BL, Z
    SUB AL, BL
    MOV SUM, AX
    JMP ENDC

NOT_OVER_200:
    ; 如果X + Y <= 200，计算X + Z
    MOV AL, X
    MOV BL, Z
    ADD AL, BL
    MOV SUM, AX

ENDC:
    MOV AH, 4CH
    INT 21H

CODE ENDS
END START