assume cs:code,ds:data
data segment
   db 'ibm             '
   db 'dec             '
   db 'dos             '
   db 'vax             '
data ends
stack segment
    dw 0,0,0,0,0,0,0,0,0      ;定义一个段，用来做栈段，容量为16个字节   
stack ends
code segment
start: 
    mov ax,stack
    mov ss,ax
    mov sp,16       ;设置栈顶ss:sp指向stack:16  堆栈使用的时候要指向栈顶

    mov ax,data
    mov ds,ax
    mov bx,0
    mov cx,4
s0: 
    push cx     ;将外层循环的cx压栈
	mov si,0
    mov cx,3
s:		
    mov al,[bx+si]
    and al,11011111b
    mov [bx+si],al
    inc si
    loop s
    add bx,16

    pop cx       ;从栈顶将cx的值进行恢复
    loop s0     ;执行过程   loop是先将 cx减1   再判断  cx是否为0  若不为0则进行循环直到cx为零的时候为止
    mov ax,4c00h
    int 21h  
code ends
end start