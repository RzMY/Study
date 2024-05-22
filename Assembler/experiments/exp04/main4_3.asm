data segment
    x dw 5678H,1234H
    y dw 6789H,2345H
    z dw 1111H,1111H
    w dw ?,?
data ends
code segment
    assume cs:code,ds:data
start: 
    mov ax,data
    mov ds,ax
    mov ax,x
    add ax,y
    mov bx,x+2
    adc bx,y+2
    add ax,24
    adc bx,0
    sub ax,z
    sbb bx,z+2
    mov w,ax
    mov w+2,bx

    mov ah,4ch
    int 21h
code ends
end start