// #include<stdio.h>

// void swap(int *a, int *b);
// void rotate(int (*matrix)[3], int matrixSize);
// void printMatrix(int (*matrix)[3], int matrixSize);

// int main() {
//     int matrix[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
//     rotate(matrix, 3);
//     printMatrix(matrix, 3);
//     return 0;
// }

// void swap(int *a, int *b) {
//     int change = *a;
//     *a = *b;
//     *b = change;
// }

// void rotate(int (*matrix)[3], int matrixSize) {
//     for (int i = 0; i < matrixSize; ++i) {
//         for (int j = 0; j < matrixSize / 2; ++j) {
//             swap(&matrix[j][i], &matrix[matrixSize - 1 - j][i]);
//         }
//     }
// }

// void printMatrix(int (*matrix)[3], int matrixSize) {
//     for (int i = 0; i < matrixSize; i++) {
//         for (int j = 0; j < 3; j++) {
//             printf("%d ", matrix[i][j]);
//         }
//         printf("\n");
//     }
// }


