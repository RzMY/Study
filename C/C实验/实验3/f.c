#include <stdio.h>

int main()
{
    int a, b, c;
    printf("请输入三个整数：");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b)
    {
        if (a > c)
            printf("最大值为：%d\n", a);
        else
            printf("最大值为：%d\n", c);
    }
    else
    {
        if (b > c)
            printf("最大值为：%d\n", b);
        else
            printf("最大值为：%d\n", c);
    }
    return 0;
}