#include<stdio.h>

int main()
{
    float a,b,c;
    int flag=1;
    char d;
    printf("输入格式：如1*2（回车）\n");
    printf("请输入：\n");
    scanf("%f%c%f", &a ,&d ,&b);
    switch(d)
    { 
        case '+': c=a+b; break;
        case '-': c=a-b; break;
        case '*': c=a*b; break;
        case '/': c=a/b; break;
        default:  flag=0;//flag=0表示输入有错
    }
    if(flag==1)//判断flag的值，如果为1，输入正确，否则输入错误
        printf("\n计算结果：%5f%c%f=%f",a,d,b,c);
    else
        printf("\n输入格式有错！");
    return 0;
}