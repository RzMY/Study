#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAXN 100000

int couple[MAXN];
bool isGuest[MAXN] = {false};
bool isSingle[MAXN] = {false};

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j)
    {
        do i ++ ; while (q[i] < x);
        do j -- ; while (q[j] > x);
        if (i < j) swap(&q[i], &q[j]);
    }
    quick_sort(q, l, j), quick_sort(q, j + 1, r);
}

int main(){
    int couple_length;
    scanf("%d", &couple_length);
    int x, y;
    for(int i = 0; i < couple_length; i++){
        scanf("%d %d", &x, &y);
        couple[x] = y;
        couple[y] = x;
    }
    int guest_length;
    scanf("%d", &guest_length);
    int guest_list[guest_length];
    for(int i = 0; i < guest_length; i++){
        scanf("%d", &guest_list[i]);
        isGuest[guest_list[i]] = true;
    }
    quick_sort(guest_list, 0, guest_length - 1);
    int single_list[guest_length];
    int single_length = 0;
    for(int i = 0; i < guest_length; i++){
        int partner = couple[guest_list[i]];
        if(partner == 0 || !isGuest[partner]){
            single_list[single_length++] = guest_list[i];
        }
    }
    printf("%d\n", single_length);
    for(int i = 0; i < single_length; i++){
        printf("%d", single_list[i]);
        if(i != single_length - 1){
            printf(" ");
        }
    }
}