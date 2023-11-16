#include <stdio.h>

long int Factorial(int n){
    return n == 1 ? 1 : n * Factorial(n - 1);
}

void main(){
    double e = 1.0;
    int i = 0;
    do{
        i++;
        e += 1.0 / Factorial(i);
    }while(1.0 / Factorial(i) > 1e-5);
    printf("结果为:%lf, 所加项数为:%d", e, i + 1);
}