#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        for i in range(1, numRows+1):
            if i == 1:
                res = [[1]]
            elif i == 2:
                res.append([1, 1])
            else:
                arr = [1]
                for j in range(2, i):
                    arr.append(res[-1][j-2]+res[-1][j-1])
                arr.append(1)
                res.append(arr)
        return res
# @lc code=end