#include<stdio.h>
#include<string.h>
void main( )
{
	char * str[]={"C program", "Basic", "Foxbase+", "Fortran", "Pascal"};
	int i,j;   char *  temp;
	
	for(i=0;i<4;i++)  /*选择法排序*/
		for(j=i+1;j<5;j++)
			if(strcmp(str[i],str[j])>0)	//当前面串比后面的大时，交换位置
			{ temp=str[i]; str[i]=str[j]; str[j]=temp; }
			
	for(i=0;i<5;i++)
		printf("%s\n",str[i]);
}
