DATAS SEGMENT
    VAR1 DB 12H
    VAR2 DB 34H
    VAR3 DB 56H
    VAR4 DB 78H
    VAR5 DB 2AH
    VAR6 DB 4CH
    VAR7 DB B7H
    VAR8 DB 65H
    VAR9 DB 88H
DATAS ENDS

STACKS SEGMENT
    DW 128 DUP(?)
STACKS ENDS

CODES SEGMENT
    ASSUME DS:DATAS, SS:STACKS
    MOV AX, DATAS
    MOV DS, AX
    MOV AX, STACKS
    MOV SS, AX
    MOV SP, 128
    MOV BX, 0100H
    MOV SI, 0002H
    MOV BP, 0200H
    MOV AX, 1200H
    MOV AX, BX
    MOV AX, [BX]
    MOV AX, [BX+SI]
    MOV AX, [BP + SI + 04]
CODES ENDS
END