#include <stdio.h>

int whatDay(int year, int month, int day)
{
    int i, sum = 0;
    int a[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
    {
        a[1] = 29;
    }
    for (i = 0; i < month - 1; i++)
    {
        sum += a[i];
    }
    sum += day;
    return sum;
}

int main()
{
    int year, month, day;
    printf("请输入年月日：");
    scanf("%d %d %d", &year, &month, &day);
    printf("这是这一年的第%d天\n", whatDay(year, month, day));
    return 0;
}