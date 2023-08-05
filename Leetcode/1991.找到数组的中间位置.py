#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            sequence = sum(nums[:i])
            reverse_sequence = sum(nums[i+1:])
            if sequence == reverse_sequence:
                return(i)
        return(-1) 
# @lc code=end

