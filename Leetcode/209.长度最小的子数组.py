#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # min_length = 0
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return 1
        #     for j in range(i + 1 + min_length if min_length else len(nums)+1, i+1, -1):
        #         if sum(nums[i:j]) >= target and sum(nums[i:j-1]) < target:
        #             min_length = j-i if min_length == 0 or j-i < min_length else min_length
        #             break
        # return min_length
        min_length = len(nums)
        for left in range(len(nums)):
            s = nums[left]
            while s > 
                
            
# @lc code=end