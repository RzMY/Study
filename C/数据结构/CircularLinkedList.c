#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;
typedef int Status;

struct CircularLinkedList
{
    int data;
    struct CircularLinkedList *next;
    struct CircularLinkedList *prior;
};

typedef struct CircularLinkedList CircularList;

void initList(CircularList **rear){
    *rear = (CircularList *)malloc(sizeof(struct CircularLinkedList));
    (*rear) -> data = 0;
    (*rear) -> next = *rear;
    (*rear) -> prior = *rear;
}

void insertList(CircularList **rear, ElemType e){
    CircularList *new_rear = (CircularList *)malloc(sizeof(struct CircularLinkedList));
    new_rear -> data = e;
    new_rear -> prior = *rear;
    new_rear -> next = (*rear) -> next;
    (*rear) -> next = new_rear;
    (*rear) = new_rear;
}

void printList(CircularList *rear){
    CircularList *p = rear -> next -> next;
    int i = 0;
    while(p != rear -> next){
        printf("%d",p -> data);
        printf(" ");
        p = p -> next;
    }
    printf("\n");
}

void deleteLastElem(CircularList **rear){
    CircularList *p = *rear;
    p -> prior -> next = p -> next;
    p -> next -> prior = p -> prior;
    *rear = p -> prior;
    free(p);
}

void unionList(CircularList **rear1, CircularList **rear2){
    CircularList *p = (*rear1) -> next;
    CircularList *q = (*rear2) -> next;
    (*rear1) -> next -> prior = *rear2;
    (*rear1) -> next = (*rear2) -> next -> next;
    (*rear2) -> next -> next -> prior = *rear1;
    (*rear2) -> next = p;
    free(q); 
}

int main(){
    CircularList *L1;
    initList(&L1);
    insertList(&L1,1);
    insertList(&L1,2);
    insertList(&L1,3);
    insertList(&L1,3);
    printList(L1);
    deleteLastElem(&L1);
    printList(L1);
    CircularList *L2;
    initList(&L2);
    insertList(&L2,4);
    insertList(&L2,5);
    insertList(&L2,6);
    unionList(&L1, &L2);
    printList(L2);
    return 0;
}
