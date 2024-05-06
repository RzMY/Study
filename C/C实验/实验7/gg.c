#include <stdio.h>
#include <string.h>

void deleteString(char a[], char b[], char c[]){
    int i = 0, j = 0, k = 0, flag = 0;
    int len_b = strlen(b);
    while(a[i] != '\0'){
        if(a[i] == b[j]){
            if(b[j+1] == '\0'){
                flag = 1;
                i++;
                j = 0;
            }else{
                i++;
                j++;
            }
        }else{
            if(flag){
                i -= j;
                flag = 0;
            }else{
                c[k++] = a[i++];
            }
            j = 0;
        }
    }
    c[k] = '\0';
}

int main(){
    char a[100];
    fgets(a, 100, stdin);
    char b[100];
    fgets(b, 100, stdin);
    char c[100];
    deleteString(a, b, c);
    printf("新a: %s", c);
    return 0;
}