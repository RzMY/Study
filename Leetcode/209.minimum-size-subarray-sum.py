#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30122
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = right = 0
        sum = 0
        min_len = 0
        while(right < len(nums) + 1):
            if(sum < target):
                right += 1
                sum += nums[right]
            elif(sum > target):
                left += 1
                sum -= nums[left]
            else:
                left += 1
                right += 1
                cur_len = right - left
                min_len = cur_len if cur_len < min_len else min_len
        return min_len
# @lc code=end

#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#