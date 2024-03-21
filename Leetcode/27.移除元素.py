#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        fast = slow = 0
        size = len(nums)
        while(fast < size):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow
# @lc code=end

