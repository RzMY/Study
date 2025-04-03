comment /*
假设数据段定义如下：
DATA  SEGMENT
STRING1  DB   'Visual C++  '
STRING2  DB   'Visual Basic'
COUNT   EQU  $-STRING2 ;计算串长度
MESS1    DB   'MATCH!',13,10,'$'
MESS2    DB   'NO MATCH!',13,10,'$'
DATA  ENDS
试编写一程序,要求比较两个字符串STRING1和STRING2所含字符是否相同,
若相同则显示'MATCH',若不相同则显示'NO MATCH'。
comment */

DATA SEGMENT
    STRING1  DB  'Visual C++  '  ;定义字符串1
    STRING2  DB  'Visual Basic'  ;定义字符串2
    COUNT   EQU  $-STRING2 ;计算串长度
    MESS1   DB  'MATCH!',13,10,'$'  ;定义匹配消息
    MESS2   DB  'NO MATCH!',13,10,'$'  ;定义不匹配消息
DATA ENDS    
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA,ES:DATA  ;设定段寄存器
START:
    MOV AX, DATA  ;将数据段地址加载到AX
    MOV DS, AX  ;将AX的值(数据段地址)加载到DS
    MOV ES, AX  ;将AX的值(数据段地址)加载到ES

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

    MOV AH,4CH  ;设置AH为4CH，准备退出程序
    INT 21H  ;调用DOS中断，退出程序
CODE ENDS
END START