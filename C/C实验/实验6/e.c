#include <stdio.h>
#include <stdlib.h>
#include <time.h>		//必须包含该头文件，以使用下面的time()函数
void main( )
{
	int k,i,j,n;

	printf("请输入机选注数：");	
	scanf("%d",&n);

	srand(time(NULL));	//srand函数产生随机种子
	
	for(j=0;j<n;j++)	//外循环控制产生n注
	{
		for(i=0;i<7;i++)//用循环产生7个随机数；对10取余，只取个位
		{
			k=rand()%10;
			printf("%d ",k);
		}
		printf("\n");	//每注号码生成后换行
	}
}