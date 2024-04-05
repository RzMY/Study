#include<stdio.h>

void main()
{ 
    int i = 100, a, b, c;
    while(i++ < 1000)
    {
        a = i/100;
        b = i/10%10;
        c = i%10;
        if(b!=a+c)
            continue;//继续循环，continue后面的语句则不执行，回到循环开始部分继续执行循环。
        printf("%5d",i);
    }
}
