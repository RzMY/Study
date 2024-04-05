#include <stdio.h>

int main()
{
    int i, j, count = 0;
    for (i = 10; i <= 20000; i++)
    {
        for (j = 2; j < i; j++)
        {
            if (i % j == 0)
                break;
        }
        if (j == i)
        {
            printf("%5d ", i);
            count++;
        }
    }
    printf("\n10～20000之间的质数个数为：%d\n", count);
    return 0;
}