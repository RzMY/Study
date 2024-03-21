#include<stdio.h>

int main()
{  
    int a=10,n;
    printf("\na+=a 的值为  %d",a+=a); 
    /* 除了格式符和转义字符其他字符原样输出*/
    a=10;
    printf("\na-=2 的值为 %d",a-=2);
    a=10;
    printf("\na*=2+3 的值为 %d",a*=2+3);
    a=10;
    printf("\na/=a+a 的值为 %d",a/=a+a);
    a=10;n=5;
    printf("\na%%=n%%=2 的值为 %d",a%=n%=2); 
    /*两个’%’表示只输出一个’%’*/ 
    a=10;
    printf("\na+=a-=a*=a 的值为 %d \n",a+=a-=a*=a);
}
