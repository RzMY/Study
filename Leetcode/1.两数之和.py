#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        sortrd_nums = sorted(nums)
        for i in sortrd_nums:
            for j in sortrd_nums:
                if i == j:
                    continue
                else:
                    if i + j == target:
                        answer.append(nums.index(i))
                        answer.append(nums.index(j))
                        break
                    else:
                        continue
            if answer != []:
                break
            else:
                continue
        return(answer)
# @lc code=end

