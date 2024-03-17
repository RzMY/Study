#
# @lc app=leetcode.cn id=344 lang=python3
# @lcpr version=30118
#
# [344] 反转字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseString(self, s: list[str]) -> None:
        length = len(s)
        for i in range(length // 2):
            re = length - 1 - i
            if re != i and i + 1 != re:
                tmp = s[i]
                s[i] = s[re]
                s[re] = tmp
                
    
# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

