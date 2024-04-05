#include <stdio.h>

int main()
{
    float f;
    printf("请输入华氏温度：");
    scanf("%f", &f);
    printf("摄氏温度为：%f\n", 5.0 / 9.0 * (f - 32));
    return 0;
}