DATA SEGMENT
    NUM1 DB(12 OR 6 AND 2) GE 0EH   
    NUM2 DB(12 XOR 6 AND 2) LE 0EH
    STR DB '$'
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
    START:
        MOV AX,DATA
        MOV DS,AX
        MOV AH,4CH
        INT 21H
CODE ENDS
END START  