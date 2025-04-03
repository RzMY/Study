#include <stdio.h>

int main(){
    int counter = 0;
    for(int i = 101; i < 200; i++){
        int isPrime = 1;
        for(int j = 2; j < i; j++){
            if(i % j == 0){
                isPrime = 0;
                break;
            }
        }
        if(isPrime){
            printf("%d ", i);
            counter++;
            if(counter % 5 == 0){
                printf("\n");
            }
        }
    }
    return 0;
}