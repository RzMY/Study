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
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i == j:
                    continue
                else:
                    if num1 + num2 == target:
                        answer.append(i)
                        answer.append(j)
                        break
                    else:
                        continue
            if answer != []:
                break
            else:
                continue
        return(answer)
# @lc code=end

