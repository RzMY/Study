DATA SEGMENT
    X DW 1234H
    Y DW 2345H
    Z DW 0
    W DW ?
DATA ENDS
ASSUME CS:CODE, DS:DATA
CODE SEGMENT
START:
    MOV AX,DATA
    MOV DS,AX

    MOV AX, X ; 将 X 的值加载到 AX
    OR AX, AX   ; 检查 AX 是否为零
    JE Clear    ; 如果 AX 为零，跳转到 Clear
    MOV BX, Y
    OR BX, BX
    JE Clear
    MOV CX, Z
    OR CX, CX
    JE Clear

    ADD AX, BX
    ADD AX, CX
    MOV W, AX
    JMP End_program    ; 结束程序

Clear: ; 清零
    MOV X, 0
    MOV Y, 0
    MOV Z, 0

End_program: ; 程序结束
    MOV AH, 4CH
    INT 21H

CODE ENDS
END START