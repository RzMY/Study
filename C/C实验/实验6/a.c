#include <stdio.h>

void main()
{ 
	int count=0;
	int i;
	float number[20];	//输入的数据存放于该数组中
	float summary;
	float average;
	summary=0;
	printf("请输入要计算的个数:");//输入要计算的个数
	scanf("%d",&count );
	
	if(count<20)		//判断合法个数
	{
		for(i=0;i<count;i++)	//输入 count 个实数
		{  
			printf("请输入第 %d 个数:",i+1); //提示用户输入第i个数据
			
			scanf("%f",&number[i]);	//将输入的数据依次放入数组中
			
			summary+=number[i];	//对数组中的元素依次累加求和
		}
		
        average = summary / count;	//计算平均值
		
		printf("输入数据的平均值为 %5.2f\n",average);	//  输出平均值
	}
	else		//输入的个数大于20个，程序结束
		printf("输入的个数大于20个.");
}