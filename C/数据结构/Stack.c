#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 50
typedef int SElemType;
typedef int Status;
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

struct Stack
{
    SElemType data[MAXSIZE];
    int top;
}SqStack;

Status InitStack()