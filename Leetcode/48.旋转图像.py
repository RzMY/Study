#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 类似创建一个辅助矩阵
        
        # matrix.reverse()
        
        # i = 0
        # while i < len(matrix):
        #     j = 0
        #     while j < len(matrix):
        #         matrix[i].append(matrix[j][i])
        #         j += 1
        #     i += 1
                
        # i = len(matrix) - 1
        # while i >= 0:
        #     j = len(matrix) - 1
        #     while j >= 0:
        #         del matrix[j][0]
        #         j -= 1
        #     i -= 1
        
        # 原地翻转
        
        # 对称
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
        # 对角线翻转
        x = len(matrix) - 1
        for i in range(len(matrix)-1):
            for j in range(x):
                matrix[i][j],matrix[len(matrix)-1-j][len(matrix)-1-i] = matrix[len(matrix)-1-j][len(matrix)-1-i],matrix[i][j]
            x -= 1
# @lc code=end

