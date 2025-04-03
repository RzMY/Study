DATA SEGMENT
    STRING1  DB  'Visual C++  '  ;定义字符串1
    STRING2  DB  'Visual Basic'  ;定义字符串2
    COUNT   EQU  $-STRING2 ;计算串长度
    MESS1   DB  'MATCH!',13,10,'$'  ;定义匹配消息
    MESS2   DB  'NO MATCH!',13,10,'$'  ;定义不匹配消息
DATA ENDS    
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA,ES:DATA  ;设定段寄存器
MAIN PROC FAR
START:
    MOV AX, DATA  ;将数据段地址加载到AX
    MOV DS, AX  ;将AX的值(数据段地址)加载到DS
    MOV ES, AX  ;将AX的值(数据段地址)加载到ES
    ; MAIN PROGRAM
    MOV CX, COUNT  ;将字符串2长度加载到CX
    LEA SI, STRING1  ;将字符串1的地址加载到SI
    LEA DI, STRING2  ;将字符串2的地址加载到DI
    CLD  ;清除方向标志
    REPZ CMPSB   ;比较字符串，如果相同则重复
    JZ MES1  ;如果零标志被设置（字符串匹配），则跳转到MES1
    MOV DX, OFFSET MESS2  ;否则，加载不匹配消息的地址到DX
    JMP DISP0  ;跳转到DISP0
MES1:  
    MOV DX, OFFSET MESS1  ;加载匹配消息的地址到DX
DISP0:  
    MOV AH,9  ;设置AH为9，准备显示字符串
    INT 21H  ;调用DOS中断，显示字符串
EXIT: RET  ;返回DOS
MAIN ENDP
CODE ENDS
END START