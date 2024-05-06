#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int age;
    int sum;
} Stats;

void BubbleSort(int age[], int n)
{
    int i, j, temp;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (age[j] > age[j + 1])
            {
                temp = age[j];
                age[j] = age[j + 1];
                age[j + 1] = temp;
            }
        }
    }
}

Stats* counter(int age[], int n)
{
    BubbleSort(age, n);
    int i = 0;
    Stats *s = (Stats *)malloc(15 * sizeof(Stats));
    for (i = 0; i < 15; i++)
    {
        s[i].age = i + 16;
        s[i].sum = 0;
    }
    for (i = 0; i < n; i++)
    {
        s[age[i]-16].sum++;
    }
    return s;
}

int main()
{
    printf("请输入年龄：");
    int age[100];
    int i = 0;
    while (1)
    {
        scanf("%d", &age[i]);
        if (age[i] == -1)
            break;
        i++;
    }
    Stats *s = counter(age, i);
    for (int j = 0; j < 15; j++)
    {
        printf("年龄：%d，人数：%d\n", s[j].age, s[j].sum);
    }
    free(s);
    return 0;
}