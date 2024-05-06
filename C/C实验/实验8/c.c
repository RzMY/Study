#include <stdio.h>

int counter(char str[])
{
    int i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    return i;
}

int main()
{
    printf("请输入一个字符串：");
    char str[100];
    scanf("%s", str);
    printf("字符串长度：%d\n", counter(str));
    return 0;
}