#include <stdio.h>
#include "stdlib.h"
#include "string.h"
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
typedef int State;
typedef int ElemType;

typedef struct Node
{
    ElemType data;
    Node* next;
}Node;

typedef struct Node *LinkList;

State InitLinkList(LinkList *L){
    *L = (LinkList)malloc(sizeof(Node));
    if(!*L){
        return ERROR;
    }else{
        return OK;
    }
    (*L) -> next = NULL;
}

State isEmpty(LinkList L){
    if(L -> next){
        return FALSE;
    }else{
        return TRUE;
    }
}

State listLength(LinkList L){
    int i = 0;
    LinkList p;
    p = L -> next;
    while(p){
        i++;
        p = p -> next;
    }
    return i;
}

State insertList(LinkList *L, int i, ElemType e){
    LinkList p;
    p = *L;
    int j = 1;
    while(p && j < i){
        p = p -> next;
        j++;
    }
    if(!p){
        printf("位置非法");
        return ERROR;
    }
    LinkList q;
    q -> data = e;
    q -> next = p -> next;
    p -> next = q;
    return OK;
}

State deleteList(LinkList *L, int i, ElemType *e){
    LinkList p;
    p = *L;
    int j = 1;
    while(p && j < i){
        p = p -> next;
        j++;
    }
    if(!p){
        printf("位置非法");
        return ERROR;
    }
    LinkList q;
    q = p -> next;
    p -> next = q -> next;
    *e = q -> data;
    free(q);
    return OK;
}

State clearList(LinkList *L){
    LinkList p, q;
    p = (*L) -> next;
    while(p){
        q = p -> next;
        free(p);
        p = q;
    }
    (*L) -> next = NULL;
    return OK;
}

State getElem(LinkList L, int i, ElemType *e){
    LinkList p;
    p = L -> next;
    int j = 1;
    while(p && j < i){
        p = p -> next;
        j++;
    }
    if(!p){
        printf("位置非法");
        return ERROR;
    }
    *e = p -> next;
    return OK;
}

State searchList(LinkList L, ElemType e, ElemType *i){
    LinkList p;
    p = L -> next;
    int j = 1;
    while(p){
        if(p -> data = e){
            *i = j;
            return TRUE;
        }
        p  = p -> next;
        j++;
    }
    printf("查不到此元素");
    return FALSE;
}

State headCreateList(LinkList *L){
    
}