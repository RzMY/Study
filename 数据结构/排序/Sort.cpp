#include <stdio.h>
#include <mm_malloc.h>
#define MAXSIZE 10

typedef struct
{
    int r[MAXSIZE+1];
    int length;
}SqList;

void Init(SqList *&L, int list[10]){
     L = (SqList*)malloc(sizeof(SqList));
    for(int i = 0; i < 10; i++){
        L->r[i+1] = list[i];
    }
    L->length = 10;
}

void Disp(SqList *&L){
    int counter = 1;
    while(counter != L->length + 1){
        printf("%d", L->r[counter]);
        counter++;
    }
}

void Swap(SqList *&L, int i, int j){
    int temp=L->r[i];
    L->r[i]=L->r[j];
    L->r[j]=temp;
}

void BubbleSort(SqList *&L){
    for(int i = 1; i < L->length; i++){
        for(int j = i + 1; j <= L->length; j++){
            if(L->r[i] > L->r[j]){
                Swap(L, i, j);
            }
        }
    }
}

void SelectSort(SqList *&L){
    for(int i = 1; i < L->length; i++){
        int min = i;
        for(int j = i + 1; j <= L->length; j++){
            // 应比较更新后的最小值r[min]
            if(L->r[j] < L->r[min]){
                min = j;
            }
        }
        Swap(L, i, min);
    }
}

void InsertSort(SqList *&L){
    int i, j;
    for(int i = 2; i <= L->length; i++){
        if(L->r[i] < L->r[i - 1]){
            L->r[0] = L->r[i];
            for(j = i - 1; L->r[0] < L->r[j]; j--){
                L->r[j+1] = L->r[j];
            }
            L->r[j+1] = L->r[0];// 多运行了一次j--,所以空出的位置由j变为j+1
        }
    }
}

void ShellSort(SqList *&L){
    int i, j;
    int increment = L->length;
    do{
        increment = increment / 3 + 1;
        for(i = increment + 1;i <= L->length;i++){
            if(L->r[i] < L->r[i - increment]){
                L->r[0] = L->r[i];
                // 如果当前元素小于前面的元素，那么将前面的元素向后移动 increment 个位置，即将其复制到当前元素的位置
                for(j = i - increment; j > 0 & L->r[0] < L->r[j]; j -= increment){
                    L->r[j + increment] = L->r[j];
                }
                L->r[j + increment] = L->r[0];// 多运行一次j -= increment，所以的得加上increment
            }
        }
    }while(increment > 1);
}

void HeapAdjust(SqList *L, int s, int m){
    int temp,j;
    temp = L->r[s];
    for(j = 2*s; j <= m; j *= 2){
        if(j < m && L->r[j] < L->r[j+1]){
            ++j;
        }
        if(temp >= L->r[j]){
            break;
        }
        L->r[s] = L->r[j];
        s=j;
    }
    L->r[s] = temp;
}

void HeapSort(SqList *&L){
    int i;
    for(i = L->length / 2; i > 0; i--){
        HeapAdjust(L, i, L->length);
    }
    for(i = L->length; i > 1; i--){
        Swap(L, 1, i);
        HeapAdjust(L, 1, i - 1);
    }
}

void Merge(int SR[], int TR[], int i, int m, int n){
    int j, k, l;
    for (j = m + 1, k = i; i <= m && j <= n; k++){
        if (SR[i] < SR[j]){
            TR[k] = SR[i++];
        }else{
            TR[k] = SR[j++];
        }
        if (i <= m){
            for (l = 0; l <= m - i; l++){
                TR[k + 1] = SR[i + l];
            }
        }
        if (j <= n){
            for (l = 0; l <= n - j; l++){
                TR[k + l] = SR[j + l];
            }
        }
    }
}

void MSort(int SR[], int TR1[], int s, int t){
    int m;
    int TR2[MAXSIZE + 1];
    if (s == t){
        TR1[s] = SR[s];
    }else{
        m = (s + t) / 2;
        MSort(SR, TR2, s, m);
        MSort(SR, TR2, m+1, t);
        Merge(TR2, TR1, s, m, t);
    }
}

void MergeSort(SqList *L){
    MSort(L->r, L->r, 1, L->length);
}

int partition(SqList *&L, int low, int high) {
    int pivot = L->r[low];
    while (low < high) {
        while (low < high && L->r[high] >= pivot) {
            --high;
        }
        Swap(L, low, high);
        while (low < high && L->r[low] <= pivot) {
            ++low;
        }
        Swap(L, low, high);
    }
    return low;
}

void QuickSort(SqList *&L, int low, int high) {
    if (low < high) {
        int pivot = partition(L, low, high);
        QuickSort(L, low, pivot - 1);
        QuickSort(L, pivot + 1, high);
    }
}

int main(){
    SqList *L;
    int list[10] = {7,3,9,4,6,7,1,0,4,3};
    Init(L, list);
    // BubbleSort(L);// 冒泡排序
    // SelectSort(L);// 选择排序
    // InsertSort(L);// 插入排序
    // ShellSort(L);// 希尔排序
    // HeapSort(L);// 堆排序
    // MergeSort(L);// 归并排序
    // QuickSort(L, 1, 10);// 快速排序
    Disp(L);
    return 0;
}
