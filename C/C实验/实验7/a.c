#include <stdio.h>
#include <math.h>

int convert(char s[]){
    int len = 0;
    while(s[len]){
        len++;
    }

    int i = 0;
    int num = 0;
    while(s[i] != '\0'){
        num += (s[i] - '0') * pow(2, len-1-i);
        i++;
    }
    return num;
}

int main(){
    char s[100] = {0};
    int i = 0;
    int num;
    while((s[i] = getchar()) != '\n'){
        i++;
    }
    s[i] = '\0';
    num = convert(s);
    printf("%d",num);
    return 0;
}