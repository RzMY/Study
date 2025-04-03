data segment
    a  db  10
    b  db  20
    c  db  30,40,50
data  ends
code  segment
    assume  cs:code,ds:data
start:
    mov ax,data
    mov ds,ax
    mov al,c+1
    add al,c
    mov a,al
    mov al,c+1
    add al,c+2
    mov b,al
    add c,10
    add c+1,20
    add c+2,30
exit:
    mov ah,4ch
    int 21h
code ends
    end start