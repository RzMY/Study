comment /*
假设数据段定义如下：
CONAME  DB  'SPACE EXPLORERS INC.'
PRLINE    DB  20 DUP ('')
用串指令,从右到左把CONAME中的字符串传送到PRLINE。
comment */

DATA SEGMENT
    CONAME  DB  'SPACE EXPLORERS INC.'
    PRLINE  DB  20 DUP (' ')
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX,DATA
    MOV DS,AX
    LEA SI,CONAME
    ADD SI,19
    LEA DI,PRLINE
    MOV CX,20
S:
    MOV AL,[SI]
    MOV [DI],AL
    DEC SI
    INC DI
    LOOP S

    MOV AH,4CH
    INT 21H
CODE ENDS
END START


DATA SEGMENT
    CONAME  DB  'SPACE EXPLORERS INC.'
    PRLINE  DB  20 DUP (' ')
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX
    MOV ES, AX
    LEA SI, CONAME + 19 ; 定位到CONAME的最后一个字符
    LEA DI, PRLINE + 19 ; 定位到PRLINE的最后一个位置
    MOV CX, 20          ; 设置复制的字符数
    STD                 ; 设置方向标志为递减
    REP MOVSB           ; 从SI复制到DI，每次复制后SI和DI递减
    CLD                 ; 清除方向标志，恢复递增方向
    MOV AH, 4CH         ; 准备退出程序
    INT 21H             ; 调用中断退出程序
CODE ENDS
END START