#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] < nums[i-1]:
        #         return nums[i]
        #     else:
        #         continue
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

# @lc code=end

