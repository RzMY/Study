#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.MaxSubsequenceSum(nums, 0, len(nums) - 1)
    def MaxSubsequenceSum(self, array, left, right) :
        if left == right :
            return array[left]
        
        middle = (left + right) // 2
        
        leftMaxSubsequenceSum = self.MaxSubsequenceSum(array, left, middle)
        rightMaxSubsequenceSum = self.MaxSubsequenceSum(array, middle + 1, right)
        
        import sys
        maxLeftBorderSum = -sys.maxsize - 1
        maxRightBorderSum = -sys.maxsize - 1
        tempSum = 0
        
        for i in range(middle, left - 1, -1):
            tempSum += array[i]
            if (tempSum > maxLeftBorderSum):
                maxLeftBorderSum = tempSum
        
        tempSum = 0
        for i in range(middle + 1, right + 1):
            tempSum += array[i]
            if (tempSum > maxRightBorderSum):
                maxRightBorderSum = tempSum
                
        return max(leftMaxSubsequenceSum, rightMaxSubsequenceSum, maxLeftBorderSum + maxRightBorderSum)
# @lc code=end

