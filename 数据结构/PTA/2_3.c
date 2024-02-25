#include <stdio.h>
#include <stdbool.h>

#define MAX_ID 100000

int couple[MAX_ID];

void initCoupleList(){
    for(int i = 0; i < MAX_ID; i++){
        couple[i] = -1;
    }
}

void addCouple(int x, int y){
    couple[x] = y;
    couple[y] = x;
}

int findCouple(int target){
    return couple[target];
}

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

bool BinarySearch(int *list, int length, int target){
    int left = 0, right = length - 1;
    while(left <= right){
        int mid = (left + right) / 2;
        if(list[mid] == target){
            return true;
        }
        else if(list[mid] > target){
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }
    return false;
}

int main(){
    int couple_length;
    scanf("%d", &couple_length);
    int x, y;
    initCoupleList();
    for(int i = 0; i < couple_length; i++){
        scanf("%d %d", &x, &y);
        addCouple(x, y);
    }
    int guest_length;
    scanf("%d", &guest_length);
    int guest_list[guest_length];
    for(int i = 0; i < guest_length; i++){
        scanf("%d", &guest_list[i]);
    }
    quick_sort(guest_list, 0, guest_length - 1);
    int single_list[guest_length];
    int single_length = 0;
    for(int i = 0; i < guest_length; i++){
        if(findCouple(guest_list[i]) == -1){
            single_list[single_length++] = guest_list[i];
        }else{
            if(!BinarySearch(guest_list, guest_length, findCouple(guest_list[i]))){
                single_list[single_length++] = guest_list[i];
            }
        }

    }
    printf("%d\n", single_length);
    for(int i = 0; i < single_length; i++){
        printf("%05d", single_list[i]);
        if(i != single_length - 1){
            printf(" ");
        }
    }
}