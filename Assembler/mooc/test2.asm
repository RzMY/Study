CODE SEGMENT
    ASSUME CS:CODE
START:
    MOV AX , 6A6AH
    MOV DX , 6A6AH
    
    SHL AX , 1 
    RCL DX , 1
    ADC AX , 0

    MOV AH , 4CH
    INT 21H
CODE ENDS
END START