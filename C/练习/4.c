#include <stdio.h>
#include <string.h>

#define MAX_LINES 100
#define MAX_LINE_LENGTH 100

int main() {
    char lines[MAX_LINES][MAX_LINE_LENGTH];
    int num_lines = 0;

    // 打开输入文件
    FILE *input_file = fopen("input.txt", "r");
    if (input_file == NULL) {
        printf("无法打开输入文件\n");
        return 1;
    }

    // 读取文件中的每一行
    while (fgets(lines[num_lines], MAX_LINE_LENGTH, input_file) != NULL) {
        // 删除换行符
        lines[num_lines][strcspn(lines[num_lines], "\n")] = 0;
        num_lines++;
    }

    fclose(input_file);

    // 对字符串进行排序
    for (int i = 0; i < num_lines - 1; i++) {
        for (int j = 0; j < num_lines - i - 1; j++) {
            if (strlen(lines[j]) > strlen(lines[j + 1])) {
                char temp[MAX_LINE_LENGTH];
                strcpy(temp, lines[j]);
                strcpy(lines[j], lines[j + 1]);
                strcpy(lines[j + 1], temp);
            }
        }
    }

    // 打开输出文件
    FILE *output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("无法打开输出文件\n");
        return 1;
    }

    // 将排序后的字符串写入到输出文件中
    for (int i = 0; i < num_lines; i++) {
        fprintf(output_file, "%s\n", lines[i]);
    }

    fclose(output_file);

    return 0;
}