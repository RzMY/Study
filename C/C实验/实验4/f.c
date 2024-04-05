#include <stdio.h>

long factorial(int n)
{
    long product = 1;
    for (int i = 1; i <= n; i++)
    {
        product *= i;
    }
    return product;
}

int main()
{
    int n;
    printf("请输入一个整数：");
    scanf("%d", &n);
    printf("%d的阶乘是%ld\n", n, factorial(n));
    return 0;
}