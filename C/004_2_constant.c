#include <stdio.h>

int main()
{
    printf("Hello\tWorld\n\n");
    char myChar = 'a';
    int myAsciiValue = (int) myChar;//将myChar转换为ASCII值
    printf("%d",myAsciiValue);
    return 0;
}