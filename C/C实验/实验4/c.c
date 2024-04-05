#include<stdio.h>

void main()
{
    int i,flag = 1;
    double s = 1;
    for(i = 2; i <= 41; i++)
    {
        s += flag * 1 / (float)i;  //同学们可以试试用1/i，看看结果。1/i是取整，1.0/i或1/(float)i才表示除//法运算。
        flag = -1 * flag;  //实现正负交替。
    }
    printf("1/(float)i的情况下：\n");
    printf("s=%lf", s);
}
