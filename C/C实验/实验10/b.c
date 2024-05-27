#include <stdio.h>
void main()
{
	int a=3,b;
	int *p;
	p=&a;
	b=*p;
	printf("%d\n",b);
	a=100;
	b=*p;
	printf("%d\n",b);
}
