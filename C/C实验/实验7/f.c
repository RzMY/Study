#include <stdio.h>

void deleteChar(char a[], char b){
    int i = 0;
    int k = 0;
    while(a[i] != '\0'){
        if(a[i] != b){
            a[k] = a[i];
            k++;
        }
        i++;
    }
    a[k] = '\0';
}

int main(){
    char a[100];
    scanf("%s", a);
    char b;
    scanf(" %c", &b);
    deleteChar(a, b);
    printf("新a: %s\n", a);
    return 0;
}