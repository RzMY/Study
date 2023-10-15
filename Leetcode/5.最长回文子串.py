#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 时间复杂度过高（字符串反转操作为O(n)）
        
        # for i in reversed(range(len(s) + 1)):
        #     for j in range(len(s)):
        #         if s[j:i+j][::-1] == s[j:i+j] and i + j <= len(s):
        #             return s[j:i+j]
        
        # 从待判断的字符串中间开始向外比较
        
        for i in reversed(range(len(s) + 1)):
            for j in range(len(s)):
                if i + j <= len(s):
                    if len(s[j:i+j]) % 2 != 0:
                        for k in range(len(s[j:i+j])):
                str = s[j:i+1]
                if s[j:i+j][::-1] == s[j:i+j] and i + j <= len(s):
                    return s[j:i+j]
# @lc code=end