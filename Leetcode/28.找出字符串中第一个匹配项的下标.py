#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # 暴力匹配
        for i in range(len(haystack)-len(needle)+1):
            active = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    active = False
            if active:
                return i
        return -1
        
    #     if haystack == needle:
    #         return 0
    #     if len(haystack)<len(needle):
    #         return -1
    #     next = []
    #     if len(needle) == 1:
    #         for i in range(len(haystack)-len(needle)+1):
    #             active = True
    #             for j in range(len(needle)):
    #                 if haystack[i+j] != needle[j]:
    #                     active = False
    #             if active:
    #                 return i
    #         return -1
    #     for i in reversed(range(1,len(needle))):
    #         next = Solution().match(haystack,needle[:i])
    #         if next != []:
    #             break
    #     for i in next:
    #         active = True
    #         for j in range(len(needle)):
    #             if i + j >= len(haystack):
    #                 active = False
    #                 break
    #             if haystack[i+j] != needle[j]:
    #                 active = False
    #         if active:
    #             return i
    #     return -1
            
    # def match(self, haystack: str, needle: str) -> int:
    #     next = []
    #     for i in range(len(haystack)-len(needle)+1):
    #         active = True
    #         for j in range(len(needle)):
    #             if haystack[i+j] != needle[j]:
    #                 active = False
    #         if active:
    #             next.append(i)
    #     return next
# @lc code=end

