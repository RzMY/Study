/*
 * @lc app=leetcode.cn id=73 lang=c
 *
 * [73] 矩阵置零
 */

// @lc code=start
void setZeroes(int** matrix, int matrixSize, int* matrixColSize){

    //计算数组中出现0的次数
    int count1 = 0;
    for(int i = 0;i < matrixSize;i++){
        for(int j = 0;j < *matrixColSize;j++){
            if(matrix[i][j] == 0){
                count1++;
            }
        }
    }
    if(count1 == 0){
        return;
    }
    int temp[count1][2];//创建对应大小的数组用于存储行列信息

    //写入行列信息
    int count2 = 0;
    for(int i = 0;i < matrixSize;i++){
        for(int j = 0;j < *matrixColSize;j++){
            if(matrix[i][j] == 0){
                temp[count2][0] = i;
                temp[count2][1] = j;
                count2++;
            }
        }
    }

    for(int i = 0;i < count1;i++){

        //行归零
        for(int j = 0;j < *matrixColSize;j++){
            matrix[temp[i][0]][j] = 0;
        }

        //列归零
        for(int k = 0;k < matrixSize;k++){
            matrix[k][temp[i][1]] = 0;
        }
    }
}
// @lc code=end

