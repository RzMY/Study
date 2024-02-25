#include  <stdio.h>
int main()
{
	char str[100],*p;
	int num=0;
	p=str;
	printf("请输入一串字符：");
	gets(str);
	printf("其中大写字母有：");
	while(*p != '\0')
	{
		if(*p>=65 && *p<=90)
			{
				printf("%c",*p);
				num++;
		}
		*(p++);
	}
	printf("\n大写字母个数为：%d",num);
}