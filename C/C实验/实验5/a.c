#include <stdio.h>

int main(){
    int counter = 0;
    for(int i = 100; i < 1000; i++){
        if(i % 3 == 0 && i % 5 == 0 && i / 10 % 10 != 0){
            printf("%d ", i);
            counter++;
            if(counter % 5 == 0){
                printf("\n");
            }
        }
    }
    return 0;
}