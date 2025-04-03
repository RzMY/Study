#include <stdio.h>

void count(char s[], char num[], int *num_count){
    int i = 0;
    *num_count = 0;
    while(s[i] != '\0'){
        if(s[i] >= '0' && s[i] <= '9'){
            num[*num_count] = s[i];
            (*num_count)++;
        }
        i++;
    }
    num[*num_count] = '\0';
}

int main(){
    char s[100];
    scanf("%s", s);
    char num[100];
    int num_count;
    count(s, num, &num_count);
    printf("%s %d\n", num, num_count);
    return 0;
}