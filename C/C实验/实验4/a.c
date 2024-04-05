#include <stdio.h>

void main()
{ 
    int i, sum = 0;
    for(i=1; i<100; i++)
    sum = sum + i; /*累加求和，分析循环起止条件！！*/
    printf("sum=%d\n", sum);
}