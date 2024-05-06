#include <stdio.h>
#include <stdbool.h>

void deleteString(char a[], char b[], char c[]){
    bool flag = true;
    int j;
    for(int i = 0; a[i] != '\0'; i++){
        j = 0;
        flag = true;
        while(b[j] != '\0'){
            if(a[i] == b[j]){
                i++;
                j++;
            }else{
                flag = false;
                break;
            }
        }
        if(flag){
            while(j != 0){
                a[i+j] = '0';
                j--;
            }
        }
    }
    int k = 0;
    for(int i = 0; a[i] != '\0'; i++){
        if(a[i] != '0'){
            c[k] = a[i];
            k++;
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
    printf("新a: %s\n", c);
    return 0;
}