#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: list[str]) -> None:
        length = len(s)
        for i in range(length//2):
            re = length - 1 - i
            if re != i and re + 1 != i:
                tmp = s[i]
                s[i] = s[re]
                s[re] = tmp
# @lc code=end

