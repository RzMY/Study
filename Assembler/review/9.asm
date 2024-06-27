comment /*
假设数据段定义如下：
DATA  SEGMENT
    ARRAY  DW  1,2,-3,-4,0,0,5,6,-7,-8,-9,10
    COUNT  EQU  $-ARRAY
DATA  ENDS
要求编写程序,测试其中正数、0及负数的个数。
正数的个数放在DI中,0的个数放在SI中,负数的个数放在AX中。 
comment */

DATA SEGMENT
    ARRAY  DW  1,2,-3,-4,0,0,5,6,-7,-8,-9,10
    COUNT  EQU  $-ARRAY
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    MOV AX,0
    MOV BX,0
    MOV CX,12
S:
    MOV DX,ARRAY[BX]
    CMP DX,0
    JE ZERO
    JG POSITIVE
    INC AX
    JMP EXIT
POSITIVE:
    INC DI
    JMP EXIT
ZERO:
    INC SI
EXIT:
    ADD BX,2
    LOOP S

    MOV AH,4CH
    INT 21H
CODE ENDS
END START