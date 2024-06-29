//static 在程序运行期间一直存在，不会被销毁，只会被初始化一次
//static 修饰的全局变量和函数只能在本文件中使用

#include <stdio.h>

void func1(void);

static int count = 10; /* 全局变量 - static 是默认的 */

int main()
{
    while (count--){
        func1();
    }
    return 0;
}

void func1(void)
{
    static int thingy = 5; /* 局部变量 - static 是持久的 */
    thingy++;
    printf("thingy = %d,count = %d\n",thingy,count);
}