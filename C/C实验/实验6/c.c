#include <stdio.h>

int main() {
    double numbers[8];
    double sum = 0, average, max, min;
    int i;

    printf("请依次输入8个数:\n");
    for(i = 0; i < 8; i++) {
        scanf("%lf", &numbers[i]);
        sum += numbers[i];
        if(i == 0) {
            max = min = numbers[i];
        } else {
            if(numbers[i] > max) {
                max = numbers[i];
            }
            if(numbers[i] < min) {
                min = numbers[i];
            }
        }
    }

    average = sum / 8;

    printf("总和: %.2lf\n", sum);
    printf("平均值: %.2lf\n", average);
    printf("最大值: %.2lf\n", max);
    printf("最小值: %.2lf\n", min);

    return 0;
}