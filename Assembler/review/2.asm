comment /*
编写汇编程序，实现如下功能：从键盘接收一个小写字母，然后找出它的后续字符并显示。
comment */

CODE SEGMENT
    ASSUME CS:CODE
START:
    MOV AH, 01H
    INT 21H
    INC AL
    MOV DL, AL
    MOV AH, 02H
    INT 21H

    MOV AH, 4CH
    INT 21H
CODE ENDS
END START