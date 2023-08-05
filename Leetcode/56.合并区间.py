#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # while循环
        
        # if len(intervals) == 1:
        #     return intervals
        # intervals.sort(key = lambda x:x[0])
        # i = 0;new_intervals = []
        # while i < len(intervals):
        #     new_intervals.append([intervals[i][0],intervals[i][-1]])
        #     if i < len(intervals) - 1:
        #         while i < len(intervals) - 1 and new_intervals[-1][-1] >= intervals[i+1][0]:
        #             new_intervals[-1][-1] = max(new_intervals[-1][-1],intervals[i+1][-1])
        #             i += 1
        #         i += 1
        #     else:
        #         i += 1
        # return new_intervals
        
        # for循环
        
        intervals.sort(key = lambda x:x[0])
        new_intervals = [intervals[0]]
        for interval in intervals:
            if interval[0] <= new_intervals[-1][-1]:
                new_intervals[-1][-1] = max(new_intervals[-1][-1],interval[-1])
            else:
                new_intervals.append(interval)
        return new_intervals
                    
# @lc code=end