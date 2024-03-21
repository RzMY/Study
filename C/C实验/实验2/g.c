#include <stdio.h>
#include <stdbool.h>
/*
表达式	你计算的值	上机验证的值
k=(a=2,b=3,a+b)		
a=2,b=5,b++,a+b		
设a=5,b=4,c=3，表达式a>b>c的值为		
设a=1，b=2，c=3，d=4，m=5,n=6，则计算完表达式（m=a>b） && (n=c>d)后，m和n的值各为：		
i=3, 则表达式k=(i++)+i		
i=3,j=10, 则表达式k=i+++j		
*/

int main()
{
    int a,b,k;
    printf("k=(a=2,b=3,a+b)  %d\n",k=(a=2,b=3,a+b));// 逗号表达式先计算a=2,b=3,然后计算a+b并赋值给k,结果为5
    k = (a=2,b=5,b++,a+b);
    printf("a=2,b=5,b++,a+b  %d\n",k);// 逗号表达式先依次计算a=2,b=5,b++,然后计算a+b并赋值给k,结果为8
    a=5; b=4; int c=3;
    printf("a>b>c  %d\n",a>b>c);// 先计算a>b,结果为1,然后计算1>c,结果为0
    a=1; b=2; c=3; int d=4,m=5,n=6;
    bool f = (m=a>b) && (n=c>d);
    printf("m=%d  n=%d\n",m,n);// 先计算a>b,结果为0并赋值给m,&&具有短路特性,所以不会计算n=c>d,结果为m=0,n=6
    int i=3;
    k = (i++)+i;
    printf("k=(i++)+i  %d\n",k);// 先计算i++,结果为3,然后计算i++,结果为4,然后计算3+4,结果为7
    i=3; int j=10;
    k = i+++j;
    printf("k=i+++j  %d\n",k);// 先计算i++,结果为3,然后计算i++,结果为4,然后计算3+10,结果为13
    return 0;
}