#include <stdio.h>

void findMiddleElement(int A[], int n) {
    if (n < 3) {
        printf("数组元素个数必须大于等于3\n");
        return;
    }
    int minIndex = 0, maxIndex = 0;
    
    // 找到最小值和最大值的索引
    for (int i = 1; i < n; i++) {
        if (A[i] < A[minIndex]) {
            minIndex = i;
        } else if (A[i] > A[maxIndex]) {
            maxIndex = i;
        }
    }

    // 找到不是最小值也不是最大值的元素
    for (int i = 0; i < n; i++) {
        if (i != minIndex && i != maxIndex) {
            printf("找到一个既不是最大值也不是最小值的元素：%d\n", A[i]);
            return;
        }
    }
}

int main() {
    int A[] = {3, 8, 1, 6, 2, 7, 5};  // 例子数组
    int n = sizeof(A) / sizeof(A[0]);
    findMiddleElement(A, n);
    return 0;
}
