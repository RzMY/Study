#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if (len(nums) < 5):
            return sorted(nums)[len(nums) - k]
        group_length = len(nums) // 5
        nums_groups = []
        for i in range(4):
            nums_groups.append(sorted(nums[i * group_length : (i + 1) * group_length]))
        nums_groups.append(sorted(nums[4 * group_length : ]))
        # print(nums_groups)
        mid = group_length // 2
        nums_groups.sort(key=lambda x: x[mid])
        print(nums_groups)
        s1 = []
        s2 = []
        
        
        
# @lc code=end