#include <stdio.h>

void findNumbers(int arr[], int n, int a, int b) {
    for(int i = 0; i < n; i++) {
        if(arr[i] > a && arr[i] < b) {
            printf("%d ", arr[i]);
        }
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int a = 3;
    int b = 7;
    findNumbers(arr, n, a, b);
    return 0;
}