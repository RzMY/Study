#include <stdio.h>

void BubbleSort(int a[], int n)
{
    int i, j, temp;
    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - 1 - i; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}

int main()
{
    printf("请输入待排序数组的元素个数：");
    int n;
    scanf("%d", &n);
    int a[n];
    printf("请输入待排序数组：");
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    BubbleSort(a, n);
    printf("排序后的数组：");
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    return 0;
}