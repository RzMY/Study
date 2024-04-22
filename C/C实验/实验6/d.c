#include <stdio.h>

void printArray(int arr[], int size) {
    int i;
    for(i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void bubbleSort(int arr[], int size) {
    int i, j;
    for(i = 0; i < size - 1; i++) {
        for(j = 0; j < size - i - 1; j++) {
            if(arr[j] < arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int numbers[8];
    int i;

    printf("请依次输入8个数字:\n");
    for(i = 0; i < 8; i++) {
        scanf("%d", &numbers[i]);
    }

    printf("原始数组:\n");
    printArray(numbers, 8);

    bubbleSort(numbers, 8);

    printf("排序结果:\n");
    printArray(numbers, 8);

    return 0;
}