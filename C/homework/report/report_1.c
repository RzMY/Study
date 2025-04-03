#include<stdio.h>

int add(int a,int b)
{
    return a+b;
}
void main()
{
int x=10,y=20,z;
z=add(x,y);
printf("Sum of %d and %d is %d",x,y,z);
}

#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 10;
    int y = 20;
    int z;

    z = add(x, y);

    printf("Sum of %d and %d is %d\n", x, y, z);

    return 0;
}
