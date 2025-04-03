#include <stdio.h>

int main() {
    int i, j, k;
    int count = 0;

    for(i = 1; i <= 4; i++) {
        for(j = 1; j <= 4; j++) {
            if(j != i) {
                for(k = 1; k <= 4; k++) {
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