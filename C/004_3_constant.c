#include <stdio.h>

#define LENGTH 10 //#define预处理器定义常量
#define WIDTH 5
#define NEWLINE '\n'

int main()
{
    int area;

    area = LENGTH * WIDTH;
    printf("value of area : %d",area);
    printf("%c%c",NEWLINE,NEWLINE);

    return 0;
}