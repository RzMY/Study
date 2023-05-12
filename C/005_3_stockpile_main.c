//extern 用于定义在其他文件中定义的全局变量或函数。
//当使用extern关键字时，不会分配存储空间，而只是指示编译器该变量在其他文件中定义。


#include <stdio.h>

int count;
extern void write_extern();

int main()
{
    count = 5;
    write_extern();
}