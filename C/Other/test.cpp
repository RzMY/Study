#define SQSTACK_H_INCLUDED
#include <iostream>
#include <stdio.h>
#include <mm_malloc.h>

#define MaxSize 100
typedef char ElemType;
typedef struct
{
    ElemType data[MaxSize];
    int top;                //栈指针
} SqStack;      

void InitStack(SqStack *&s)
{
    s=(SqStack *)malloc(sizeof(SqStack));
    s->top=-1;
}
void DestroyStack(SqStack *&s)
{
    free(s);
}
int StackLength(SqStack *s)  //返回栈中元素个数——栈长度
{
    return(s->top+1);
}
bool StackEmpty(SqStack *s)
{
    return(s->top==-1);
}
bool Push(SqStack *&s,ElemType e)
{
    if(s->top==MaxSize - 1)
    {
        return false;
    }

    s->top++;
    s->data[s->top] = e;
    return true;
}
bool Pop(SqStack *&s,ElemType &e)
{
    if(s->top==-1)
    {
        return false;
    }
    e = s->data[s->top];
    s->top--;
    return true;
}
bool GetTop(SqStack *s,ElemType &e)
{
    if (s->top==-1)         //栈为空的情况，即栈下溢出
        return false;
    e=s->data[s->top];
    return true;
}

void DispStack(SqStack *s)  //输出栈
{
    int i;
    for (i=s->top; i>=0; i--)
        printf("%c ",s->data[i]);
    printf("\n");
}




bool MatchBrackets(ElemType exp[],SqStack *&s)
{
    char e;

    for(int i=0; exp[i]!='\0'; i++)
    {
        if(exp[i] == '(' | exp[i] == '[' | exp[i] == '{'){
            Push(s, exp[i]);
            printf("K");
        }else{
            if(!Pop(s, e)){
                break;
            }
            printf("K");
        }
    }
    if (StackEmpty(s))
        return true;
    else
        return false;
}


int main()
{
    SqStack *s;
    printf("(1)初始化栈！\n");
    InitStack(s);
    char st[100];
    printf("(2)请输入表达式：\n");
    scanf("%s", st);
    MatchBrackets(st, s);
    if(MatchBrackets(st, s)){
        printf("括号匹配！");
    }else{
        printf("括号不匹配！");
    }
    return 0;
}
