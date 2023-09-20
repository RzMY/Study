# define MaxSize 50
# include "mm_malloc.h" 
typedef int ElemType;

typedef struct SequentialList
{
    ElemType date[MaxSize];
    int length;
}SqList;

void CreateList(SqList *&L,ElemType a[],int n){
    int i = 0;
    int k = 0;
    L = (SqList *)malloc(sizeof(SqList));
    while (i < n){
        L -> date[k] = a[i];
        k++;
        i++;
    }
    L -> length = k;
}
