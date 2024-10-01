#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
import re


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            arr = [1]
            last = self.getRow(rowIndex-1)
            for i in range(1, rowIndex):
                arr.append(last[i-1]+last[i])
            arr.append(1)
            return arr
                
# @lc code=end

