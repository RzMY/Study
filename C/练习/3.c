#include <string.h>
#include <stdio.h>

int find_substring_position(char *main_str, char *sub_str) {

    int main_len = strlen(main_str);
    int sub_len = strlen(sub_str);

    for (int i = 0; i <= main_len - sub_len; i++) {
        int j;
        for (j = 0; j < sub_len; j++) {
            if (main_str[i + j] != sub_str[j]) {
                break;
            }
        }
        if (j == sub_len) {
            return i;
        }
    }
    return -1;
}

int main() {
    char main_str[] = "Hello, world!";
    char sub_str[] = "orld";
    int position = find_substring_position(main_str, sub_str);
    printf("子串在主串的第%d个位置\n", position);
    return 0;
}