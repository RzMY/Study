#include <stdio.h>
#include <float.h>

int main()
{
    printf("int 储存大小：%lu \n", sizeof(int));
    printf("float 储存最大字节数：%lu \n",sizeof(float));
    printf("float 最小值： %E \n",FLT_MIN);
    printf("float 最大值： %E \n",FLT_MAX);
    printf("精度值： %d \n",FLT_DIG);
    int i =10;
    float f = 3.14;
    double d = i + f;
    printf("d = %f \n",d);
    int i_int = (int)3.14159;
    printf("i_2 = %d \n",i_int);
}