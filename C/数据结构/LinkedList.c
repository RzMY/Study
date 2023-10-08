#include <stdio.h>
#include "stdlib.h"
#include "string.h"
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
typedef int State;
typedef int ElemType;
typedef struct Node{   //结点的存储结构
    ElemType data;   //结点的数据部分
    struct Node* next;   //指向结点的下一结点
}Node;

typedef struct Node *LinkList;  //定义LinkList（其实也就是头结点）

//初始化单链表
State InitLinkList(LinkList *L){
    *L = (LinkList)malloc(sizeof(Node));   //为头结点分配内存
    if(!*L){   //如果头结点不存在，即分配内存失败则返回ERROR
        return ERROR;
    }else{   //如果头结点存在则说明初始化成功
        return OK;
    }
    (*L)->next = NULL;   //初始单链表头结点的指针域为空
}

//单链表是否为空
State isEmpty(LinkList L){
    if(L->next){   //判断头结点的指针域是否为空
        return FALSE;   //头结点的指针域非空则返回FALSE；
    }else{
        return TRUE;   //头结点指针域为空则返回TRUE；
    }
}

//获得单链表的长度
State listLength(LinkList L){
    int i=0;  //计数器，初始为0
    LinkList p;  //定义临时结点
    p = L->next;  //单链表的首个结点
    while(p){   //如果此结点存在则计数器+1，并且指向下一结点，循环遍历
        i++;
        p = p->next;
    }
    return i;  //返回单链表的长度
}

//单链表的插入
State insertList(LinkList *L, int i, ElemType e){
    LinkList p;  //定义临时结点
    p = *L;   //临时结点指向头结点
    int j=1;   //位置计数器
    while(p && j<i){  //因为单链表的插入是要插入到当前结点的后方，所以计数器初始为1
        p = p->next;  //如果还没有到指定位置的前方，则继续向下进行
        j++;  //位置计数器+1
    }
    if(!p){  //如果p不存在了说明链表中的结点数达不到插入结点的条件，无法插入，如果存在则继续向下进行
        return ERROR;
    }
    LinkList q;  //定义结点q
    q = (LinkList)malloc(sizeof(Node));  //为结点q分配内存空间
    q->data = e;  //为q结点的数据域赋指定值
    q->next = p->next;  //结点插入的经典方式，现将自身的next指向前结点的next结点
    p->next = q;  //将自身设为前结点的next结点
    return OK;
}

//单链表的删除
State deleteList(LinkList *L, int i, ElemType *e){
    LinkList p;  //定义临时结点
    p = *L;  //将临时结点指向头结点
    int j=1;  //计数器
    while(p && j<i){  //判断p结点是否存在，并且计数器不能大于要删除结点的位置
        p=p->next;  //满足条件，继续向下走
        j++;  //计数器+1
    }
    if(!p){   //如果p不存在说明单链表的结点数不够所要删除的位置，无法删除，如果存在则继续向下进行
        return ERROR;
    }
    LinkList q;  //定义临时结点
    q = p->next;  //将要删除的结点赋给q
    p->next = q->next;  //将要删除结点的下一结点赋给要删除结点的上一结点，这样就避开了要删除的结点
    *e = q->data;  //将要删除的结点的数据域赋值给e用以备份返回
    free(q);  //释放q结点的内存区域，即删除了指定的结点
    return OK;
}

//清除单链表
State clearList(LinkList *L){
    LinkList p, q;  //定义两个临时结点
    p = (*L)->next;  //将p当前作为头结点的下一结点
    while(p){  //如果p存在（即还没有删除完成）
        q = p->next;  //则将q作为p结点的下一结点，然后将p删除后再将q赋给p这样的话就相当于p一直再向后删除
        free(p);
        p = q;
    }
    (*L)->next = NULL;  //全部删除后，将头结点的指针域置空，则表明单链表为空了
    return OK;
}

//获取单链表中某个位置的元素
State getElem(LinkList L, int i, ElemType *e){
    LinkList p;  //定义临时结点
    p = L->next;   //将p设置为首个结点
    int j = 1;  //计数器
    while(p && j<i){   //在还不到对应的位置且p存在的情况下继续循环
        p = p->next;   //沿着链表向下进行
        j++;   //计数器+1
    }
    if(!p){   //如果跳出循环是因为p不存在了，则说明此位置没有结点，返回ERROR
        return ERROR;
    }
    *e = p->data;   //将对应位置上的元素的赋值给e用于返回
    return *e;   //返回指定位置上的数据域
}

//判断单链表中是否含有某个元素,如果有，返回它所在的位置信息
State localElem(LinkList L, ElemType *e){
    LinkList p;  //定义临时结点
    p = L->next;  //将临时结点设为首个结点
    int j=1;  //计数器，因为当前为首个结点，所以计数器的初始值为1
    while(p){   //如果p存在则循环向下进行判断
        if(p->data==e){   //如果找到了对应的数值则将对应的计数器数值返回即为对应位置信息
            return j;
        }
        p = p->next;  //如果不是对应数值则继续向下寻找
        j++;  //计数器+1
    }
    return ERROR;  //一直p为空了跳出循环，则说明没有对应的数值
}

//创建单链表（前插法）
State headCreatList(LinkList *L){
    *L = (LinkList)malloc(sizeof(Node));  //创建单链表首先为头结点分配内存
    (*L)->next = NULL;   //空链表头结点的指针域为空
    for(int i=1;i<9;i++){   //将1-9按照前插法的方式插入单链表
        LinkList p = (LinkList)malloc(sizeof(Node));  //新建结点且为其分配内存
        p->data = i; //将新建结点的数据域设置为i的值
        p->next = (*L)->next;  //插队到头结点的下一结点，即头插法
        (*L)->next = p;  //将头结点的指针域设置为新新结点，头插完成
    }
    return OK;
}

//创建单链表（后插法）
State tailCreatList(LinkList *L){
    (*L) = (LinkList)malloc(sizeof(Node));  //创建单链表首先为头结点分配内存
    LinkList t;  //设置临时结点表示尾指针
    t = (*L);  //尾指针指向头结点，说明此时还为空链表
    for(int i=5;i<14;i++){   //将5-14数值按照尾插法插入单链表
        LinkList p = (LinkList)malloc(sizeof(Node));  //新建结点并分配内存
        p->data = i;  //将新建结点的数据域设置为当前i值
        t->next = p;  //尾指针指向新建结点
        t = p;  //将新建结点设置为尾结点
    }
    t->next = NULL;  //尾结点的指针域为空
    return OK;
}
//单链表的打印
State printLinkList(LinkList L){
    LinkList p;  //定义临时结点
    p = L->next;  //将p设置为首个结点
    int i=1;  //计数器
    while(p){  //判断当前结点是否存在
        printf("第%d个结点的元素值为%d\n", i, p->data);  //如果存在则将数据域进行打印
        p = p->next;  //向下继续进行
        i++;  //计数器+1
    }
    return OK;
}

int main(){
    LinkList L1, L2;
    int e;
    printf("使用头插法创建单链表可得结果L1：\n");
    headCreatList(&L1);
    printLinkList(L1);
    printf("使用尾插法创建单链表可得结果L2：\n");
    tailCreatList(&L2);
    printLinkList(L2);
    printf("其中L1的长度为%d, L2的长度为%d\n",listLength(L1), listLength(L2));
    printf("向单链表L1的第三个位置插入一个666元素可得：\n");
    insertList(&L1, 3, 666);
    printLinkList(L1);
    printf("将单链表L2的第三个位置的元素删除可得：\n");
    deleteList(&L2, 3, &e);
    printf("删除的元素为：%d\n", e);
    printf("现在的单链表L2为：\n");
    printLinkList(L2);
    printf("单链表是否存在元素666？存在则返回其位置，不存在则返回0:\n");
    printf("单链表L1中666元素的位置为：%d\n", localElem(L1, 666));
    printf("单链表L2中666元素的位置为：%d\n", localElem(L2, 666));
    getElem(L1, 8, &e);
    printf("获得L1中的第8个元素为：%d\n", e);
    printf("清空单链表可得L1: \n");
    clearList(&L1);
    printLinkList(L1);
}