assume cs:code,ds:data,ss:stack
stack segment
   dw 0,0,0,0,0,0,0,0
stack ends
data segment
   db '1. display......'
data ends
code segment
start: mov ax,data
       mov ds,ax
       mov ax,stack
       mov ss,ax 
       mov sp,16
       mov bx,0
       mov cx,4
	   mov si,0
s:	   mov al,[bx+si+3]
       and al,11011111b ;将字符转换为大写
       mov [bx+si+3],al
       inc si
       loop s
       mov ax,4c00h
       int 21h  
code ends
end start
