#include<stdio.h>
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define maxsize 100
typedef int Status;
typedef int ElemType;
//线性表的存储结构
typedef struct{
    int data[maxsize];  //数据存储
    int length;         //目前线性表的长度
}SqList;
//创建线性表
Status CreatList(SqList *L){
    int tempdata;  //临时数据，用来保存输入的值
    L->length=0;  //初始长度为0
    for(int i=0;i<=maxsize;i++){
        printf("请输入第%d个元素的值，-1结束\n", i+1);
        scanf("%d", &tempdata);   //接受控制台的输入，并保存在临时数据中
        if(tempdata==-1){   //判断是否为输入结束语句
            return OK;   //若为输入结束语句，则直接结束方法
        }
        L->data[i] = tempdata;   //若不是结束语句则将临时数据存放在对应位置中
        L->length++;   //每放入一个数据，则长度length+1
    }
    return OK;
}
//获取线性表的长度
Status getLength(SqList *L){
    return L->length;
}
//插入线性表
Status insertList(SqList *L, int i, ElemType e){
    if(L->length==maxsize){  //判断线性表是否已满
        printf("目前线性表的长度已满，不可再插入元素");
        return ERROR;
    }
    if(i<1||i>L->length+1){   //判断插入位置是否合法
        printf("您输入的插入位置有误");
        return ERROR;
    }
    if(i!=L->length+1){   //判断是否是插在线性表的最后，如果不是的话要进行线性表的元素后移操作
        for(int i=i;i<L->length;i++){
            L->data[i]=L->data[i-1];
        }
    }
    L->data[i-1]=e;   //如果是插在线性表的最后，则直接写入就可。如果不是最后则已经后移完成，将插入元素写入对应位置即可
    return OK;
}
//打印线性表
Status printList(SqList *L){
    for(int i=0;i<L->length;i++){   //for循环遍历的方式访问线性表的元素并进行打印
        printf("\n第%d个元素为%d", i+1, L->data[i]);
    }
    return OK;
}
//删除线性表
Status deleteList(SqList *L, int i, int *e){
    if(L->length==0){   //判断目前的顺序表是否为空，若为空则不可进行删除操作
        printf("线性表的长度为0，不可进行删除操作");
        return ERROR;
    }
    if(i==0||i>L->length){
        printf("您输入的删除位置有误，不可进行删除操作");
        return ERROR;
    }
    e = L->data[i-1];  //将要删除位置的元素存储起来
    if(i!=L->length){  //如果要删除的位置不在最后，那么要进行顺序表的前移操作
        for(int n=i;n<L->length;n++){
            L->data[n-1] = L->data[n];
        }
        L->length--;
        return e;
    }
    L->data[i-1] = 0;  //如果要删除的位置在最后，那么直接将最后一个元素置0
    return e;
}
//合并线性表（集合相并）
Status Union(SqList *LA, SqList *LB){
    int lengtha = LA->length;
    int lengthb = LB->length;
    int isEqual = 0;   //判断是否存在相同元素的标志
    for(int i=0;i<lengthb;i++){
        if(searchList(LA, LB->data[i])){   //判断LA中是否含有与制定元素相等的元素
            isEqual = 1;   //若含有，则判断置1（TRUE）
        }
        if(!isEqual){    //若判断为！1（0）即不想等的时候执行插入操作，并将LA的长度+1
            insertList(LA, ++lengtha, LB->data[i]);
            LA->length++;
        }
        isEqual = 0;   //判断完一个后再次循环判断下一个，对应的判断标志初始化为0
    }
    return OK;
}
//线性表查找元素
Status searchList(SqList *LA, int e){
    int lengtha = LA->length;  //线性表的长度
    for(int i=0;i<lengtha;i++){   //遍历线性表
        if(LA->data[i]==e){   //比较当前线性表元素是否相等
            return TRUE;
        }
    }
    return FALSE;
}
//删除线性表中指定的元素
Status deleteValue(SqList *L, int e){
    int i=0;  //循环遍历的计数位
    while(L->data[i]!=e&&i<L->length){  //循环要么找到相同元素要么全部遍历
        i++;
    }
    if(i<L->length){   //如果不是全部遍历，则表明是找到了相同的元素
        for(int n=i;n<L->length;n++){  //按照线性表删除元素的做法进行遍历向前移动
            L->data[n]=L->data[n+1];
        }
        L->length--;  //进行删除操作后将线性表的长度-1
        return OK;
    }
    printf("线性表中没有对应的元素，无法删除");  //如果是全部遍历，则表明线性表中没有指定的元素
    return ERROR;
}
//相交线性表（两集合的交集）
Status mergeList(SqList *LA, SqList *LB){
    int lengthb = LB->length;  //遍历循环使用B线性表的长度
    int isEqual = 0;  //判断是否相等的标志位
    for(int i=0;i<lengthb;i++){   //循环便利线性表B中的元素线性表A进行比较
        if(searchList(LA, LB->data[i])){   //判断当前A中是否有这个B中的元素
            isEqual = 1;   //如果有的话，标识位置1（true）
        }
        if(isEqual){   //如果相等则需要进行删除操作
            deleteValue(LA,LB->data[i]);   //将匹配到的与B中的元素相等的元素进行删除
        }
        isEqual = 0;  //新的一轮将标识位初始化置0
    }
    return OK;
}
int main(int argc, const char * argv[]) {
    SqList sqlistA;
    SqList sqlistB;
    int e;
    printf("请输入线性表A的内容：\n");
    CreatList(&sqlistA);
    printList(&sqlistA);
    printf("\n请输入线性表B的内容：\n");
    CreatList(&sqlistB);
    printList(&sqlistB);
    printf("\n目前线性表A的长度为%d", getLength(&sqlistA));
    printf("\n目前线性表B的长度为%d", getLength(&sqlistB));
    Union(&sqlistA, &sqlistB);
    printf("\n合并后的线性表A的长度为%d, 线性表A的内容为：", getLength(&sqlistA));
    printList(&sqlistA);
    mergeList(&sqlistA, &sqlistB);
    printf("\n再与线性表B进行相交的线性表A的变成了：");
    printList(&sqlistA);
    insertList(&sqlistA, 2, 9);
    printf("\n向线性表A中的第二个位置插入元素9操作后得：");
    printList(&sqlistA);
    deleteList(&sqlistA, 2, e);
    printf("\n将线性表A的中第二个位置元素删除操作后得：");
    printList(&sqlistA);
    return 0;
}