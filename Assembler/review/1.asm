comment /*
求表达式Y=A*X+B-C的值,已知A、B、C分别为存放在DA_1、DA_2、DA_3字节单元的无符号数,
它们的值分别是:8、9、10,X存放在INPUT字节单元,把结果Y放入JSJ_10字单元。
comment */

DATA SEGMENT
    DA_1 DB 255
    DA_2 DB 9
    DA_3 DB 255
    INPUT DB 255
    JSJ_10 DW ?
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX

    MOV AL, DA_1
    MOV BL, INPUT
    MUL BL
    ADD AL, DA_2
    ADC AH, 0
    SUB AL, DA_3
    SBB AH, 0
    MOV JSJ_10, AX

    MOV AH , 4CH
    INT 21H
CODE ENDS
END START