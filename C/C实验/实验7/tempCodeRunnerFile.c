#include <stdio.h>

void sstrcat(char a[], char b[]){
    for(int i = 5; i < 10; i++){
        a[i] = b[i-5];
    }
}

int main(){
    char a[5];
    scanf("%s", a);
    char b[100];
    scanf("%s", b);
    sstrcat(a, b);
    printf("新a: %s\n", a);
}