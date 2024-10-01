#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        last_space = 0
        new_s = []
        for i in range(len(s)):
            if s[i] == ' ':
                for j in range(last_space, i):
                    new_s.append(s[last_space+i-j-1])
                new_s.append(' ')
                last_space = i+1
            else:
                pass
        for i in range(last_space, len(s)):
            new_s.append(s[last_space+len(s)-i-1])
        return ''.join(new_s)
        # words = s.split(' ')
        # reversed_words = [word[::-1] for word in words]
        # return ' '.join(reversed_words)
                    
            
# @lc code=end

