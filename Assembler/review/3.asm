comment /*
编写汇编程序,实现如下功能:在首地址为STRING1的存储区中以字节方式存储字符H,
在首地址为STRING2的存储区中以字节方式存储字符E,比较两个字符是否相等，
相等给字节变量TAG送数据0,不相等给字节变量TAG送数据1。
comment */

DATA SEGMENT
    STRING1 DB 'H'
    STRING2 DB 'H'
    TAG DB ?
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    MOV AL,STRING1
    MOV AH,STRING2
    CMP AL,AH
    JE EQUAL
    MOV TAG,1
EXIT:
    MOV AH,4CH
    INT 21H
EQUAL:
    MOV TAG,0
    JMP EXIT
CODE ENDS
END START