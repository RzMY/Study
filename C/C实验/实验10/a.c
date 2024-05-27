#include <stdio.h>
void main()
{
	int *p1,*p2,*p,a,b,t;
	scanf("%d,%d",&a,&b);
	p1=&a; p2=&b;
	if(a<b)
	{ 
		p=p1; p1=p2; p2=p;
	}
    // if(a<b)
	// { 
	// 	t=*p1; *p1=*p2; *p2=t;
	// }
	printf("a=%d,b=%d\n",a,b);
	printf("max=%d,min=%d\n",*p1,*p2);
}
