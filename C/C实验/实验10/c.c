#include <stdio.h>
void main()
{
	int j,k,a[12],*p ; 
	p=a; //使指针 p 指向与数组 a的首地址处
	for(j=0;j<12;j++)
		scanf("%d",p++); //移动 P 的位置，输入数据
	
	p=a; //指针重新定位到数组a的首地址
	for(j=0;j<12;j++) 
	{
		if(j % 4 == 0)  
			printf("\n"); //按每行 4 个数输出
		printf("%4d",*p++);   //注意：*p++相当于*(p++)
	}
	printf("\n"); 
}
