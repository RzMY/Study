/*
 * @lc app=leetcode.cn id=48 lang=c
 *
 * [48] 旋转图像
 */

// @lc code=start


void rotate(int** matrix, int matrixSize, int* matrixColSize){
    for(int i = 0;i < matrixSize;i++){
        for(int j = 0;j < matrixSize/2;j++){
            swap(&matrix[j][i],&matrix[matrixSize-1-j][i]);
        }
    }
    for(int i = 0;i < matrixSize;i++){
        for(int j = i + 0;j < matrixSize;j++){
            swap(&matrix[i][j],&matrix[j][i]);
        }
    }
}
void swap(int* a,int* b){
    int change;
    change = *b;
    *b = *a;
    *a = change;
}
// @lc code=end

