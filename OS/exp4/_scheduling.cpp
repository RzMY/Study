#include<stdio.h>
#include<stdlib.h>

#define Ready 0
#define Running 1
#define Block 3
#define Over 4

typedef struct PCBNode
{
	int ID;
	int Priority;
	int CPUtime;
	int Alltime;
	int Arrivetime;
	int state;
	int counter;
	struct PCBNode *next;
}PCB;//定义数据结构

PCB *run;
PCB *ready;
PCB *over;
PCB *head;

//定义状态量
int Min(PCB *head)//挑选出队列中的拥有最小alltime 值的块，返回块号,用于sjf算法
{
	PCB *p;//q用来记录这个块的地址
	int min,id;//记录最小值和块号
	p=head->next;
	if(p)
	{
       min=p->Alltime;
	   id=p->ID;
	while(p->next)
	{
		
		if(min>p->next->Alltime)			
		{
			min=p->next->Alltime;
			id=p->next->ID;
			p=p->next;
		}
		else
		{
			p=p->next;
		}
	}
	}
	return id;   
}
int Max(PCB *head)//挑选出队列中的拥有最大优先级的块，返回块号，用于prio算法
{
	PCB *p;//q用来记录这个块的地址
	int max,id;//记录最大和块号
	p=head->next;
	if(p)
	{
       max=p->Priority;
	   id=p->ID;
	   while(p->next)
	   {
		   if(max<=p->next->Priority)
		   {
			   max=p->next->Priority;
			   id=p->next->ID;
			   p=p->next;
		   }
		   else
		   {
			   p=p->next;
		   }
	   }
	}
	return id;   
}
PCB *CreatPCB(int n)
{
	int i;
	PCB *p,*q;
	head=(PCB*)malloc(sizeof(PCB));
	head->next=NULL;
	p=head;
	for(i=1;i<=n;i++)
	{
		q=(PCB*)malloc(sizeof(PCB));
		q->ID=i;
		q->CPUtime=0;
		q->Alltime=rand()%200;
		q->Priority=rand()%10;
		q->state=Ready;
	    q->Arrivetime=0;	
		p->next=q;
		p=q;
        q->next=NULL;		
	}
	head->next->Priority=0;
	return head;
}//创建pcb块

void Display(PCB *head)
{
	PCB *p;
	p=head->next;
	printf("ID  Arrivetime    CPUtime(已占用)  Alltime   Priority    state        \n");
	while(p)
	{	
		printf("%d         ",p->ID);
        printf("%d         ",p->Arrivetime);
        printf("%d               ",p->CPUtime);
        printf("%d         ",p->Alltime);
        printf("%d         ",p->Priority);
        printf("%d         \n",p->state);
        p=p->next;
	}
}//显示PCB块
void FCFS(PCB *head,PCB *over)
{
	PCB *p,*q;
	int j=0;
	int  n=0,s=0;
	double  m;
	ready=head;
	p=ready->next;
	q=over;
	while(p)
	{
		p->state=Running;
		ready->next=p->next;
		n=p->Alltime+n;
		p->CPUtime=p->Alltime;
		p->Alltime=0;
		s=s+n;
		p->next=NULL;
		q->next=p;
		p->state=Over;
		q=q->next;
		q->next=NULL;
		p=head->next;
		j++;
	    printf("第%d次执行算法后的就绪队列：\n",j);	
		Display(head); 
	}	
    m=(double)s/j;
	printf("完成顺寻为：\n");
	Display(over);
	printf("\n");
	printf("每个进程等待的平均时间为：%lf\n",m);	
	printf("所有进程等待的总时间为：%d",s);
}
void SJF(PCB *head,PCB *over)//sjf算法
{
	PCB *p,*q,*b,*o;//b 用来记录该块的地址
	int s;//记录块号
	int m,n,h=0,d=0,j=0;
	double f;
	p=head->next;
	q=over;
	o=head;
	printf("完成顺寻为：\n");
	m=p->ID;
	n=p->Alltime;
    s=Min(head);
	b=p->next;
	printf("%d：\n",s);
	while(head->next)
	{
		while(s!=p->ID)
		{
	        o=p;
			p=p->next;
		}
		d=p->Alltime+d;
	    p->CPUtime=p->Alltime;
		p->Alltime=0;
		h=d+h;
        b=p;
		q->next=b;
		o->next=p->next;
		p=head->next;
		b->next=NULL;
		o=head;
		q=q->next;
        s=Min(head);
		j++;
		printf("第%d次执行算法后的就绪队列：\n",j);	
		Display(head);
	}
	f=(double)h/j;
	printf("完成顺寻为：\n");
	Display(over);
    printf("每个进程等待的平均时间为：%lf\n",f);	
	printf("所有进程等待的总时间为：%d",h);
}
void Prio(PCB *head,PCB *over)
{
	PCB *p,*q,*b,*o;//b 用来记录该块的地址
	int s;//记录块号
	int m,n,h=0,d=0,j=0;
	double f;
	p=head->next;
	o=head;
	q=over;
	printf("当前拥有最大优先级的块号为：\n");
	m=p->ID;
	n=p->Alltime;
    s=Max(head);
	b=p->next;
	printf("%d：\n",s);
	while(head->next)
	{
		while(s!=p->ID)
		{
			o=p;
			p=p->next;
		}
		d=p->Alltime+d;
	    p->CPUtime=p->Alltime;
		p->Alltime=0;
		h=d+h;
        b=p;
		q->next=b;
		o->next=p->next;
		p=head->next;
		b->next=NULL;
		o=head;
		q=q->next;
        s=Max(head);
		j++;
        printf("第%d次执行算法后的就绪队列：\n",j);	
		Display(head);
	}
	f=(double)h/j;
	printf("完成顺寻为：\n");
	Display(over);
    printf("每个进程等待的平均时间为%lf\n",f);	
	printf("所有进程等待的总时间为：%d",h);
}
void RR(PCB *head,PCB *over,int t,int k)//时间片轮转法
{	                                 //k用来记录剩余要执行的进程数目
	 PCB *p,*q,*r,*o,*tail;//o用来记录当前块的地址
	 int n=0,s=0,f;
	 double h;
	 f=k;
	 p=head->next;
	 while(p->next)
	 {
		 tail=p;
		 p=p->next;
	 }
     printf("执行顺序为：\n");
	 tail=p;
     o=p;//前驱
     tail->next=head->next;    
     p=head->next;
	 q=over;	
	 while(k>0)	 
	 {	 
		 r=head->next;
		 if(p->Alltime>t)//该进程还未执行完成
		 {
			 p->Alltime=p->Alltime-t;
			 n=n+t;
			 s=s+n;
			 o=p; 
			 printf("执行进程%d      ",p->ID);
             printf("该进程的Alltime变为%d\n",p->Alltime);
			 p=p->next;
		 }
		 else//该进程可以完成了
		 {
			 printf("         完成进程：%d       \n",p->ID);
			 n=n+p->Alltime;
			 s=s+n;
			 p->Alltime=0;
			 o->next=p->next;
			 q->next=p;
			 q=q->next;     
			 q->next=NULL;
			 p=o->next;
			 k--;	
		 }
	 }
	 h=(double)s/f;
	 printf("完成顺寻为：\n");
	 Display(over);
	 printf("每个进程等待的平均时间为：%lf\n",h);	
	 printf("所有进程等待的总时间为：%d",s);
}
int main(void)
{
	int n,m,t;
	printf("|------------------------------------------------------------------------------|");    
	printf("|                       进 程 调 度 的 模 拟                                   |"); 
	printf("|------------------------------------------------------------------------------|"); 
	printf("\t\t\t|----选项--------------------|\n");
	printf("\t\t\t|         1. FCFS调度法      |\n");
	printf("\t\t\t|----------------------------|\n");
	printf("\t\t\t|         2. SJF调度算法     |\n");
	printf("\t\t\t|----------------------------|\n");
	printf("\t\t\t|         3. 优先调度算法    |\n");
	printf("\t\t\t|----------------------------|\n"); 
	printf("\t\t\t|         4. RR调度算法      |\n");
	printf("\t\t\t|----------------------------|\n"); 
	printf("\n");   
	printf("请输入要创建的进程数目：");
	scanf("%d",&n);
	head=CreatPCB(n);
	printf("创建的就绪队列为：\n");
	Display(head);  
    printf("请选择要调度的算法：");
	scanf("%d",&m);
	over=(PCB*)malloc(sizeof(PCB));
	over->next=NULL;
	switch(m)
	{
	case 1:
        system("CLS");
		FCFS(head,over);		
		break;
	case 2:
        system("CLS");
		SJF(head,over);
		break;
	case 3:
        system("CLS");
		Prio(head,over);
		break;
	case 4:
        system("CLS");
		printf("请输入时间片的大小：");
		scanf("%d",&t);
		RR(head,over,t,n);
		break;
	}
	//Release(head);
	return 0;
}
