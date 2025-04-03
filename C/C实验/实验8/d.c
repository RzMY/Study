#include <stdio.h>
int factor(int n)
{
  if(1==n) return 1;
  else return n*factor(n-1);
}

void main()
 { 
	int a;
    
	a=factor(5);
	printf("%d \n",a);
}
