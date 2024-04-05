#include<stdio.h>

void main()
{
    int i=1;
    long product=1;
    while(i<=10)
    {
        product*=i;
        i++;
    }
    printf("product=%ld",product);
}
