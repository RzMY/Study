#include <stdio.h>

//打印倒三角形
int main() 
{
    int i, j;
    for(i = 6; i >= 0; i--){
        for(j = 0; j < 6-i; j++){
            printf(" ");
        }
        for(j = 0; j < 2*i-1; j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}