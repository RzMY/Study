#include <iostream>
using namespace std;


void input(int array[]);  //此函数实现输入10个元素
void max_min_value(int array[]);  //此函数实现交换数组的对应元素
void output(int array[]);  //此函数实现输出10个元素

int main()
{   
    int array[10];
    input(array);
    max_min_value(array);
    output(array);
    return 0;
}

void input(int array[])
{
    for(int i=0;i<10;i++)
    {
        cin>>array[i];
    }
}

void max_min_value(int array[])
{
    int max=array[0],min=array[0],max_index=0,min_index=0;
    for(int i=0;i<10;i++)
    {
        if(array[i]>max)
        {
            max=array[i];
            max_index=i;
        }
        if(array[i]<min)
        {
            min=array[i];
            min_index=i;
        }
    }
    int tmp=0;
    tmp=array[0];
    array[0]=min;
    array[min_index]=tmp;
    tmp=array[9];
    array[9]=max;
    array[max_index]=tmp;
}

void output(int array[])
{
    for(int i=0;i<10;i++)
    {
        cout<<array[i]<<" ";
    }
}