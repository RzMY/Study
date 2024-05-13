#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void strSort(char *str[], int n)
{
    int i, j;
    char *temp;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (strcmp(str[j], str[j + 1]) > 0)
            {
                temp = str[j];
                str[j] = str[j + 1];
                str[j + 1] = temp;
            }
        }
    }
}

int main()
{
    char *str[100];
    int i = 0;
    printf("请输入字符串：");
    while (1)
    {
        str[i] = (char *)malloc(100 * sizeof(char));
        gets(str[i]);
        if (str[i][0] == '\0')
            break;
        i++;
    }
    strSort(str, i);
    for (int j = 0; j < i; j++)
    {
        puts(str[j]);
    }
    for (int j = 0; j < i; j++)
    {
        free(str[j]);
    }
    return 0;
}