#include<stdio.h>
void main()
{ 
	char a[30]="C program.";
    char b[30],*p1,*p2;

    p1=a;  p2=b;	//两个指针分别指向两个字符串的起始位置
    for( ;*p1!='\0';p1++,p2++) //当串1没有到串尾时，进行复制
        *p2=*p1;	//将串1的字符复制到串2
	* p2='\0';	//给串2加上结束标志
	
	printf("string a is:%s\n",a);
	printf("string b is:%s\n",b);
}
