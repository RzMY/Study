#include <stdio.h>

void strcatee(char *s1, char *s2)
{
    while (*s1)
        s1++;
    while (*s2)
    {
        *s1 = *s2;
        s1++;
        s2++;
    }
    *s1 = '\0';
}

int main()
{
    char s1[100], s2[100];
    printf("输入第一个字符串：");
    scanf("%s", s1);
    printf("输入第二个字符串：");
    scanf("%s", s2);
    strcatee(s1, s2);
    printf("连接后的字符串：%s\n", s1);
    return 0;
}