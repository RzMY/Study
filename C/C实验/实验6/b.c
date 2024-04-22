#include <stdio.h>
#define N 5		//定义N代表值5
void main( )
{
	int i, j;
	int x[N][N] = {{17,24,1,8,15},{23,5,7,14,16}, {4,6,13,20,22}, {10,12,19,21,3}, {11,18,25,2,9}};	//对二维数组中的元素进行初始化
	int rowSum, colSum, diagSum;
	int flag = 1;
	
	for (i=0; i<N; i++)		//行求和
	{
		rowSum = 0;
		for (j=0; j<N; j++)
		{
			rowSum += x[i][j];
		}
		printf("第%d行的和为:%d\n",i,rowSum);
	}
	
	for (j=0; j<N; j++)		//列求和
	{
		colSum = 0;
		for (i=0; i<N; i++)
		{
			colSum += x[i][j];
		}
		printf("第%d列的和为:%d\n",j,rowSum);
	}

	
	diagSum = 0;
	for (i=0; i<N; i++)  //主对角线求和
	{
		diagSum = diagSum + x[i][i];  //填空，完成语句
	}
	printf("主对角线求和为:%d\n",diagSum);
	
	diagSum = 0;
	for (j=0; j<N; j++)  //次对角线求和
	{
		diagSum = diagSum + x[j][N-1-j];
	}
	printf("次对角线求和为:%d\n",diagSum);
}
