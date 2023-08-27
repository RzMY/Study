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
        matrix.reverse()
        
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix):
                matrix[i].append(matrix[j][i])
                j += 1
            i += 1
                
        i = len(matrix) - 1
        while i >= 0:
            j = len(matrix) - 1
            while j >= 0:
                del matrix[j][0]
                j -= 1
            i -= 1
# @lc code=end

