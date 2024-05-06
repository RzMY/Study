#include <stdio.h>

void count(char s[], char lower[], int *lower_count, char upper[], int *upper_count){
    int i = 0;
    *lower_count = 0;
    *upper_count = 0;
    while(s[i] != '\0'){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            upper[*upper_count] = s[i];
            (*upper_count)++;
        }else if(s[i] >= 'a' && s[i] <= 'z'){
            lower[*lower_count] = s[i];
            (*lower_count)++;
        }
        i++;
    }
    lower[*lower_count] = '\0';
    upper[*upper_count] = '\0';
}

int main(){
    char s[100];
    scanf("%s", s);
    char upper[100], lower[100];
    int upper_count, lower_count;
    count(s, lower, &lower_count, upper, &upper_count);
    printf("%s %d\n", upper, upper_count);
    printf("%s %d\n", lower, lower_count);
    return 0;
}