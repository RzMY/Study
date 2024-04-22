#include <stdio.h>

int main() {
    int i, j, k;
    int count = 0;

    for(i = 2; i <= 8; i+=2) {
        for(j = 0; j <= 8; j+=2) {
            if(j != i) {
                for(k = 0; k <= 8; k+=2) {
                    if(k != i && k != j) {
                        printf("%d%d%d ", i, j, k);
                        count++;
                        if(count % 5 == 0) {
                            printf("\n");
                        }
                    }
                }
            }
        }
    }

    return 0;
}