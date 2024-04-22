#include <stdio.h>

int main() {
    int i, j;
    int count = 0;
    int oddCount = 0;

    for(i = 1; i <= 7; i++) {
        for(j = 1; j <= 7; j++) {
            if(j != i) {
                int num = i * 10 + j;
                if(num < 100 && num % 2 != 0) {
                    printf("%d ", num);
                    count++;
                    oddCount++;
                    if(count % 5 == 0) {
                        printf("\n");
                    }
                }
            }
        }
    }

    printf("\n奇数数量: %d\n", oddCount);

    return 0;
}