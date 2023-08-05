#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # 暴力遍历

        # for i in nums:
        #     if i == target:
        #         return(nums.index(i))
        # for i in range(len(nums)-1):
        #     if target in range(nums[i],nums[i+1]):
        #         return(i+1)
        # if target < nums[0]:
        #     return(0)
        # else:
        #     return(len(nums))

        # 二分查找
        
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        left = 0;right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return left
# @lc code=end