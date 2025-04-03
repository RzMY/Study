comment /*
编写汇编程序,实现如下功能:在首地址为ARRAY的存储区中依次存储5个字数据
23,36,2,10,7,求出该数组的内容之和（不考虑溢出），
并把结果存入字变量TOTAL中。
comment */

DATA SEGMENT
    ARRAY DW 23,36,2,10,7
    TOTAL DW ?
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    MOV CX,5
    MOV AX,0
    MOV SI,0
S:
    ADD AX,ARRAY[SI]
    ADD SI,2
    LOOP S
    MOV TOTAL,AX

    MOV AH,4CH
    INT 21H
CODE ENDS
END START