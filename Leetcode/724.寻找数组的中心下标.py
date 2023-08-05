#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(0,len(nums)):
            sequence = sum(nums[:i])
            reverse_sequence = sum(nums[i+1:])
            if sequence == reverse_sequence:
                return(i)
        return(-1) 
# @lc code=end