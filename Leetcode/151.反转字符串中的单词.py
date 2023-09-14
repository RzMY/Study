#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # while not (s[0].isalpha() and s[-1].isalpha()):
        #     s = s.strip()
        # ret = []
        # s_part = list(s.partition(" "))
        # if s_part[-1] == '' and s_part[-2] == '':
        #     ret.append(s_part[0])
        # else:
        #     while s_part[-1]:
        #         s_part = list(s.partition(" "))
        #         ret.append(s_part.pop(0))
        #         s_part.pop(0)
        #         s = "".join(s_part)
        #         if s != '':
        #             while not (s[0].isalpha() and s[-1].isalpha()):
        #                 s = s.strip()
        # ret.reverse()
        # ret = " ".join(ret)
        # return ret
        s_part = list(s.split(' '))
        ret = []
        for word in s_part:
            if word != '':
                ret.append(word)
        ret.reverse()
        ret = ' '.join(ret)  
        return ret            
        
        
# @lc code=end