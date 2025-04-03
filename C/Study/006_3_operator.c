//逻辑运算符
#include <stdio.h>

int main()
{
    int a = 5;
    int b = 20;
    int c;

    if(a && b)//逻辑与运算符，如果两个操作数都非零，则条件为真。
    {
        printf("Line 1 - 条件为真\n");
    }
    if(a || b)//逻辑或运算符，如果两个操作数中有任意一个非零，则条件为真
    {
        printf("Line 2 - 条件为真\n");
    }
    a = 0;
    b = 10;
    if ( a && b )
    {
        printf("Line 3 - 条件为真\n");
    }
    else
    {
        printf("Line 3 - 条件为假\n");
    }
    if ( !( a && b ) )//逻辑非运算符，用来逆转操作数的逻辑状态
    {
        printf("Line 4 - 条件为真\n");
    }
}