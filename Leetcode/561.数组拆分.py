#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]
        return res
# @lc code=end