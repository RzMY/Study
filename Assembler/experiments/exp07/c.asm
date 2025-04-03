Data  segment
Db 'word',0
Db 'unix',0
Db 'wind',0
Db 'good',0
Data ends
Code segment
Start:
    Mov ax,data
    Mov ds,ax
    Mov bx,0
    Mov cx,4
s:		
    mov si,bx
    Call cap
    Add bx,5
    Loop s
    Mov sa,4c00h
    Int 21h

cap:
    ; mov cl,[si]
    ; mov ch,0
    ; jcxz ok
    ; and byte ptr[si],11011111b
    ; inc si
    ; jmp short cap

    cap:mov al,[si] ;al=word
	mov ah,0
	or  ax,0
	jz ok
	and byte ptr[si],11011111b
	inc si
	jmp short cap

ok:ret

code ends
end start