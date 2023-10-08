#include <stdio.h>
#include <stdbool.h>
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define MaxSize 100
typedef int Status;
typedef int ElemType;

typedef struct{
    int data[MaxSize];
    int length;
}SqList;

Status CreateList(SqList *L){
    int tempdata;
    L -> length = 0;
    for(int i = 0; i <= MaxSize; i++){
        printf("请输入第%d元素,-1结束\n", i+1);
        scanf("%d", &tempdata);
        if(tempdata == -1){
            return OK;
        }
        L -> data[i] = tempdata;
        L -> length++;
    }
    return OK;
}

Status getLength(SqList *L){
    return L -> length;
}

Status insertList(SqList *L, int i, ElemType e){
    if(L -> length == MaxSize){
        printf("长度溢出");
        return ERROR;
    }
    if(i < 1 || i > L -> length + 1){
        printf("插入位置非法");
        return ERROR;
    }
    if(i != L -> length + 1){
        L -> length++;
        for(int j = L -> length; j >= i - 1; j--){
            L -> data[j + 1] = L -> data[j];
        }
    }
    L -> data[i-1] = e;
    return OK;
}

Status printList(SqList *L){
    printf("[");
    int flag = 0;
    for(int i = 0; i < L -> length; i++){
        if(flag){
            printf(",");
        } else {
            flag = 1;
        }
        printf("%d", L -> data[i]);
    }
    printf("]");
    return OK;
}

Status deleteIndex(SqList *L, int i, int *e){
    if(L -> length == 0){
        printf("线性表已空");
        return ERROR;
    }
    if(i == 0|| i > L -> length){
        printf("位置非法");
        return ERROR;
    }
    e = L -> data[i - 1];
    if(i != L -> length){
        for(int k = i; k < L -> length; k++){
            L -> data[k - 1] = L -> data[k];
        }
        L -> length--;
        return e;
    }
}

Status searchList(SqList *L, int e){
    int length = L -> length;
    for(int i = 0;i < length; i++){
        if(L -> data[i] == e){
            return TRUE;
        }
    }
    return FALSE;
}

Status Union(SqList *LA, SqList *LB){
    int lengtha = LA -> length;
    int lengthb = LB -> length;
    bool isEqual = FALSE;
    for(int i = 0; i < lengthb; i++){
        if(searchList(LA, LB -> data[i])){
            isEqual = TRUE;
        }
        if(!isEqual){
            insertList(LA, ++lengtha, LB -> data[i]);
            LA -> length++;
        }
        isEqual = FALSE;
    }
    return OK;
}

Status deleteValue(SqList *L, int e){
    int i = 0;
    while(L -> data[i] != e && i < L -> length){
        i++;
    }
    if(i < L -> length){
        int e;
        deleteIndex(L, i + 1, &e);
    }
    printf("没有该元素");
    return ERROR;
}

Status mergeList(SqList *LA, SqList *LB, SqList *LC){
    int lengtha = LA -> length;
    int lengthb = LB -> length;
    bool isEqual = FALSE;
    if(lengtha >= lengthb){
        for(int i = 0; i < lengthb; i++){
            if(searchList(LA, LB -> data[i])){
                isEqual = TRUE;
            }
            if(!isEqual){
                deleteValue(LB, LB -> data[i]);
            }
            isEqual = FALSE;
        }
        int lengthb_after = getLength(LB);
        for(int i = 0; i < lengthb_after; i++){
            LC -> data[i] = LB -> data[i];
            LC -> length++;
        }
    }else{
        for(int i = 0; i < lengtha; i++){
            if(searchList(LB, LA -> data[i])){
                isEqual = TRUE;
            }
            if(!isEqual){
                deleteValue(LA, LA -> data[i]);
            }
            isEqual = FALSE;
        }
        int lengtha_after = getLength(LA);
        for(int i = 0; i < lengtha_after; i++){
            LC -> data[i] = LA -> data[i];
            LC -> length++;
        }
    }
    return OK;
}

int main(int argc, const char * argv[]){
    SqList sqlistA;
    SqList sqlistB;
    SqList sqlistC;
    int e;
    printf("请输入线性表A的内容：\n");
    CreateList(&sqlistA);
    printList(&sqlistA);
    printf("\n请输入线性表B的内容：\n");
    CreateList(&sqlistB);
    printList(&sqlistB);
    printf("\nA的长度为%d", getLength(&sqlistA));
    printf("\nB的长度为%d", getLength(&sqlistB));
    printf("\n元素3是否在A中：");
    if(searchList(&sqlistA, 3)){
        printf("是");
    }else{
        printf("否");
    }
    printf("\n元素3是否在B中：");
    if(searchList(&sqlistB, 3)){
        printf("是");
    }else{
        printf("否");
    }
    Union(&sqlistA, &sqlistB);
    printf("\n合并后的线性表A的长度为%d, 线性表A的内容为：", getLength(&sqlistA));
    printList(&sqlistA);
    mergeList(&sqlistA, &sqlistB, &sqlistC);
    printf("\n再将线性表A与线性表B相交变成了线性表C：");
    printList(&sqlistC);
    insertList(&sqlistA, 2, 9);
    printf("\n向线性表A中的第二个位置插入元素9操作后得：");
    printList(&sqlistA);
    deleteIndex(&sqlistA, 2, e);
    printf("\n将线性表A的中第二个位置元素删除操作后得：");
    printList(&sqlistA);
    return 0;
}