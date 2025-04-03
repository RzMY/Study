comment /*
编写程序,计算data段中com数组里4个元素的3次方,
并将结果分别保存在对应的reslut数组单元中。(数据自行设置)
comment */

DATA SEGMENT
    COM DB 1,2,3,4
    RESULT DD 0,0,0,0
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    LEA SI,COM
    LEA DI,RESULT
    MOV CX,4
S:
    MOV AL,COM[SI]
    MUL COM[SI]
    MOV BX,AX
    MOV AX,0
    MOV AL,COM[SI]
    MUL BX
    MOV [DI],AX
    MOV [DI+2],DX
    INC SI
    ADD DI,4
    LOOP S
    
    MOV AH,4CH
    INT 21H
CODE ENDS
END START