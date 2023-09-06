#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # if len(min(strs,key=len)) == 1:
        #     return min(strs,key=len)
        ret = ""
        for i in range(1,len(min(strs,key=len)) + 1):
            re = strs[0][:i]
            for word in strs:
                if word[:i] != re:
                    return ret
            ret = re
        return ret
            
            
# @lc code=end