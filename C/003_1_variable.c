/*
int i, j, k;
char c, ch;
float f, salary;
double d;

extern int d = 3,f = 5; // d 和 f 的声明与初始化
int d = 3,f = 5; // 定义并初始化 d 和 f
char x = 'x'; // 变量 x 的值为 'x'


extern int i; //声明，不是定义
int i; //声明并定义
*/
#include <stdio.h>
//函数外定义变量 x 和 y
int x;
int y;
int addtwonum()
{
    //函数内声明变量 x 和 y 为外部变量
    extern int x;
    extern int y;
    //给外部变量（全局变量）x 和 y 赋值
    x = 1;
    y = 2;
    return x + y;
}

int main()
{
    int result;
    //调用函数 addtwonum
    result = addtwonum();

    printf("result = %d \n",result);
    return 0;
}