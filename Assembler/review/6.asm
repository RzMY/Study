comment /*
编写汇编程序，实现如下功能：从键盘接收一个字符，
如果输入字符为Y,则显示字符6,
如果输入字符为N,则显示字符8。
comment */

DATA SEGMENT
    CHAR DB ?
    MESS1 DB '6$'
    MESS2 DB '8$'
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    MOV AH,01H
    INT 21H
    MOV CHAR,AL
    CMP CHAR,'Y'
    JNE N
    MOV DX,OFFSET MESS1
    JMP EXIT
N:
    MOV DX,OFFSET MESS2
EXIT:
    MOV AH,09H
    INT 21H
    MOV AH,4CH
    INT 21H
CODE ENDS
END START