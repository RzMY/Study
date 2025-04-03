data segment                                    
    X db 6                                          
    Y db ?                                                       
data ends                                 
code segment                              
    assume cs:code,ds:data                    
start:
    mov ax,data
    mov ds,ax
    mov al,x
    mov y,5
    add y,al
    mov ah,4ch
    int 21h
code ends 
end  start