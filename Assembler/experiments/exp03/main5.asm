data segment
    table dw 10,20,30,40,0
    entry dw 3
data ends

code segment
    assume cs:code,ds:data

start:
    mov ax,data
    mov ds,ax

    mov bx,offset table
    add bx,entry
    mov ax,[bx]
    int 21h

code ends
end start