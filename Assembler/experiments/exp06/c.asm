DATA  SEGMENT
    ORG 0100H
    AA_1 DB     1,3,5,7,2,4,6
    ORG 0150H
    BB_1 DB     7 dup(?)
    COUNT  DW     7
DATA  ENDS
CSEG  SEGMENT
      ASSUME CS:CSEG,DS:DATA
START:
    MOV    AX,DATA
    MOV    DS,AX
    MOV    CX,COUNT
    LEA    SI,AA_1      
    LEA    DI,BB_1     
LP1:  
    MOV    AL,[SI]      
    ADD    AL,2       
    MOV   [DI],AL       
    INC SI            
    INC DI           
    LOOP  LP1      
    LEA   SI,BB_1    
    MOV CX,COUNT
DISP: 
    MOV  DL,[SI]
    ADD  DL,30H     
    MOV    AH,  02    
    INT    21H     
    MOV   DL, ' '     
    MOV   AH,  2   
    INT   21H    
    INC   SI
    LOOP  DISP     
    MOV   AH,4CH   
    INT    21H
CSEG  ENDS
END  START
