#include <stdio.h>

int main()
{
    const int LENGTH = 10;//使用const声明常量
    const int WIDTH = 5;
    const char NEWLINE = '\n';

    int area;
    area = LENGTH * WIDTH;
    printf("Value of area : %d",area);
    printf("%c%c",NEWLINE,NEWLINE);
    return 0;
}
//把常量定义为大写字母形式，是一个很好的编程习惯
//const   int    var = 5;
//关键字 数据类型 变量名 变量值;