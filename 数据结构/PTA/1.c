#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>
#include <string.h>
int arr[1000];

typedef struct Node
{
    int data;
    struct Node *next;
}SqQueue;

void InitQueue(SqQueue *L)
{
    L->next = NULL;
}

void InsertList(SqQueue *L, int data)
{
    SqQueue *p = L;
    while(p->next != NULL)
    {
        p = p->next;
    }
    SqQueue *q = (SqQueue *)malloc(sizeof(SqQueue));
    q->data = data;
    q->next = NULL;
    p->next = q;
}

int QuitQueue(SqQueue *L)
{
    if (L->next == NULL) {
        return -1;
    }
    SqQueue *p = L->next;
    int data = p->data;
    L->next = p->next;
    free(p);
    return data;
}

bool IsEmpty(SqQueue *L)
{
    if(L->next == NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main(){

    int num;
    int i=0;
    // int arr[1000];
    while(1){
        scanf("%d",&num);
        char c=getchar();
        arr[i++]=num;
        if(c=='\n'){
            break;
        }
    }

    SqQueue A, B;
    InitQueue(&A);
    InitQueue(&B);
    for(int j = 1; j < i; j++){
        if(arr[j] % 2 == 0){
            InsertList(&B, arr[j]);
        }
        else{
            InsertList(&A, arr[j]);
        }
    }
    int count = 0;

    while(!IsEmpty(&A) || !IsEmpty(&B)){
        if(!IsEmpty(&A)){
            printf("%d", QuitQueue(&A));
            count++;
            if(count != arr[0]) {
                printf(" ");
            }
        }
        if(!IsEmpty(&A)){
            printf("%d", QuitQueue(&A));
            count++;
            if(count != arr[0]) {
                printf(" ");
            }
        }
        if(!IsEmpty(&B)){
            printf("%d", QuitQueue(&B));
            count++;
            if(count != arr[0]) {
                printf(" ");
            }
        }
    }
    return 0;
}