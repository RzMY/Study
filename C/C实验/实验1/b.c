#include <stdio.h>

//打印正空心三角形
int main(){
    int i, j;
    for(i = 1; i < 7; i++){
        for(j = 0; j < 6-i; j++){
            printf(" ");
        }
        for(j = 1; j < 2*i; j++){
            if(j == 1 || j == 2*i-1 || i == 6){
                printf("*");
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}