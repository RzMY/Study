#include <stdio.h>
#include <math.h>

void main(){
    printf("请输入n和a的值:");
    int n, a, sum = 0;
    scanf("%d %d", &n, &a);
    for (int i = 1; i <= n; i++){
        int count = 0;
        for (int j = 1; j <= i; j++){
        count += (a * pow(10, j - 1));
        }
        sum += count;
    }
    printf("结果为:%d\n", sum);
}