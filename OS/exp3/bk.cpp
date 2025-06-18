#define _ALLOW_COMPILER_AND_STL_VERSION_MISMATCH
#include <windows.h>
#include <iostream>
#include <stdio.h>

using namespace std;

bool lock[4]={false,false,false,false};//四把锁，分别对四个缓冲区进行同步
int buffer[4]={0,0,0,0};//缓冲区，表示资源的个数

void display(){
      cout<<"--------------------------------"<<endl;
	  cout<<"缓冲区    0   1     2         3"<<endl;
	  for(int i=0;i<4;i++){cout<<"  "<<buffer[i]<<"   ";}
	  cout<<endl;
}

DWORD WINAPI Producer(LPVOID lpParameter){
	while(true){
		for(int j=0;j<4;j++){
			if(buffer[j]==0){//找到空缓冲区
				if(lock[j]==false){//同步锁为false，可以进行操作
					lock[j]=true;//加锁，防止其他线程操作此缓冲区
					if(buffer[j]<1){//限定一个缓冲区只能存放一个资源
						++buffer[j];//模拟生产资源
						cout<<"生产一个资源，放入缓冲区"<<j<<"中"<<endl;
						lock[j]=false;//解锁
						break;//一次生产一个
					}
				}
				if(j==3){
					cout<<"找不到空缓冲区，等待中。。"<<endl;
					Sleep(2000);
				}
			}
		}
	}
	return 0;
}

DWORD WINAPI Customer(LPVOID lpParameter)
{
	while(true){
		for(int n=0;n<4;n++){
			if(buffer[n]==1){//找到满缓冲区
				if(lock[n]==false){//同步锁为false，可以进行操作
					lock[n]=true;//加锁，防止其他线程操作此缓冲区
					if(buffer[n]>=1){
						--buffer[n];//模拟消费资源
						cout<<"消费一个资源，从缓冲区"<<n<<"中取出"<<endl;
						lock[n]=false;//解锁
						break;//一次生产一个
					}
				}
			}
			if(n==3){
                cout<<"找不到满缓冲区，等待中。。"<<endl;
			    Sleep(2000);
			}
		}
	}
	return 0;
}


int main(int argc,char* argv[])
{
    display();
	HANDLE handle[5];
	DWORD dw1,dw2,dw3,dw4,dw0;

    handle[0]=CreateThread(NULL,0,Producer,NULL,0,&dw1);
    handle[1]=CreateThread(NULL,0,Producer,NULL,0,&dw2);
    handle[2]=CreateThread(NULL,0,Producer,NULL,0,&dw3);
    handle[3]=CreateThread(NULL,0,Customer,NULL,0,&dw4);
    handle[4]=CreateThread(NULL,0,Customer,NULL,0,&dw0);
    display();

    Sleep(3000);
    display();
    return 0;
}
