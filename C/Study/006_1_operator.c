//算数运算符
#include <stdio.h>

int main()
{
    int a = 21;
    int b = 10;
    int c;

    c = a + b;
    printf("Line 1 - c 的值是 %d\n",c);
    c = a - b;
    printf("Line 2 - c 的值是 %d\n",c);
    c = a * b;
    printf("Line 3 - c 的值是 %d\n",c);
    c = a / b;
    printf("Line 4 - c 的值是 %d\n",c);
    c = a % b;//取余
    printf("Line 5 - c 的值是 %d\n",c);
    c = a++; // 赋值后再加 1 ，c 为 21，a 为 22
    printf("Line 6 - c 的值是 %d\n",c);
    //a=22
    c = a--; // 赋值后再减 1 ，c 为 22 ，a 为 21
    printf("Line 7 - c 的值是 %d\n",c);
    printf("Line 8 - a 的值是 %d\n",a);

    a = 10;
    c = a++;
    printf("先赋值后运算：\n");
    printf("Line 1 - c 的值是 %d\n",c);
    printf("Line 2 - a 的值是 %d\n",a);
    a = 10;
    c = a--;
    printf("Line 3 - c 的值是 %d\n",c);
    printf("Line 4 - a 的值是 %d\n",a);

    printf("先运算后赋值：\n");
    a = 10;
    c = ++a;
    printf("Line 5 - c 的值是 %d\n",c);
    printf("Line 6 - a 的值是 %d\n",a);
    a = 10;
    c = --a;
    printf("Line 7 - c 的值是 %d\n",c);
    printf("Line 8 - a 的值是 %d\n",a);
}