#include <stdio.h>

int main()
{
    int x;
    printf("请输入一个三位数：");
    scanf("%d",&x);
    int a,b,c;
    a = x%10;
    b = x/10%10;
    c = x/100;
    printf("三位数之和为：%d\n",a+b+c);
    return 0;
}