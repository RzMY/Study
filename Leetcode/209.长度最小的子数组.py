#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = right = 0
        length = float('inf')
        total = 0
        while(left < len(nums) and right < len(nums) + 1):
            if total >= target:
                if right - left < length:
                    length = right - left
                total -= nums[left]
                left += 1
            else:
                if(right < len(nums)):
                    total += nums[right]
                    right += 1
                else:
                    break
        return length if length != float('inf') else 0
 # @lc code=end