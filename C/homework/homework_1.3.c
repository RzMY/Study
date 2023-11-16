#include <stdio.h>
#include <math.h>

long int Factorial(int n){
    long int result = 1;
    for(int i = 2; i <= n; i++){
        result *= i;
    }
    return result;
}

void main(){
    printf("请输入x的值:");
    double x, sin = 0;
    scanf("%lf", &x);
    int i = 0;
    do{
        i++;
        sin += pow(-1, i - 1) * pow(x, 2 * i - 1) / Factorial(2 * i - 1);
    }while(fabs(pow(-1, i - 1) * pow(x, 2 * i - 1) / Factorial(2 * i - 1)) > 1e-5);
    printf("结果为:%lf, 所加项数为:%d", sin, i);
}