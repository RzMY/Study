#include <stdio.h>
#include <math.h>

int count(int a, int n)
{
    int sum = 0;
    int num = 0;
    for (int i = 0; i < n; i++)
    {
        num = 0;
        for (int j = 0; j <= i; j++)
        {
            num += a * pow(10, j);
        }
        sum += num;
    }
    return sum;
}

int main()
{
    int a, n;
    printf("请输入a和n：");
    scanf("%d %d", &a, &n);
    printf("结果：%d\n", count(a, n));
    return 0;
}