comment /*
假设数据段定义如下,DATAX和DATAY均为带符号数,
从键盘上接收加（＋）、减（－）、乘（*）符号,
然后对DATAX和DATAY完成相应运算,结果存入RLT单元。
DATAS SEGMENT
DATAX  DW  10
DATAY  DB   2
RLT  DW   ?
DATAS ENDS
comment */

DATA SEGMENT
    DATAX DW 10
    DATAY DB 2
    RLT DW ?
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    MOV DX,DATAX
    MOV AH,01
    INT 21H
    MOV AH,'+'
    CMP AL,AH
    JE AD
    MOV AH,'-'
    CMP AL,AH
    JE SU
    JMP MU
AD:
    ADD DL,DATAY
    ADC DH,0
    MOV RLT,DX
    JMP EXIT
SU:
    SUB DL,DATAY
    SBB DH,0
    MOV RLT,DX
    JMP EXIT
MU:
    MOV AX,0
    MOV AL,DATAY
    MUL DATAX
    MOV RLT,AX
EXIT:
    MOV AH,4CH
    INT 21H
CODE ENDS
END START