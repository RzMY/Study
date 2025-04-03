#include <stdio.h>

int convert(char s[]){
    return (s[0] - '0')*100 + (s[1] - '0')*10 + (s[2] - '0');
}

int main(){
    char s[3];
    scanf("%s", s);
    printf("%d", convert(s));
    return 0;
}