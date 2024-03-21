#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        fast = 0
        size = len(nums)
        res = []
        count = 0
        while(fast < size):
            if(nums[fast] == 1):
                count += 1
                fast += 1
            else:
                if count != 0:
                    res.append(count)
                    count = 0
                fast += 1
        res.append(count)
        return max(res)
# @lc code=end

