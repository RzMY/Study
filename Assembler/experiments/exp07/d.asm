DATA SEGMENT
    COM  DW 1, 2, 3, 4       
    RESULT  DW 4 DUP(?)      
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA

CUBE PROC NEAR ; 计算AX的立方
    MOV BX,AX
    MUL AX                   
    MUL BX                   
    RET                      
CUBE ENDP

MAIN PROC FAR
    MOV AX, DATA             
    MOV DS, AX

    LEA SI, COM ; SI指向COM
    LEA DI, RESULT ; DI指向RESULT

    MOV CX, 4 ; 循环4次

CALCLOOP:
    MOV AX, [SI] ; 取出COM中的一个数  
    CALL CUBE ; 计算立方  
    MOV [DI], AX  ; 结果存入RESULT  
    ADD SI, 2 ; 指向COM中的下一个数
    ADD DI, 2 ; 指向RESULT中的下一个位置
    LOOP CALCLOOP ; 循环        

    MOV AH, 4CH              
    INT 21H
MAIN ENDP

CODE ENDS
END MAIN