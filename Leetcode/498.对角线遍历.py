#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        # 生成遍历序列
        v_length = len(mat)
        c_length = len(mat[0])
        # temp_list = []
        # re_times = abs(v_length - c_length) + 1
        # num = 1
        # for i in range(1 , v_length + c_length):
        #     if num == min(v_length,c_length):
        #         if re_times > 1:
        #             temp_list.append(num)
        #             re_times -= 1
        #         elif re_times == 1:
        #             temp_list.append(num)
        #             num -= 1
        #             re_times -= 1
        #         else:
        #             continue
        #     elif i < min(v_length,c_length):
        #         temp_list.append(num)
        #         num += 1
        #     elif i > min(v_length,c_length) + abs(v_length - c_length):
        #         temp_list.append(num)
        #         num -= 1
        # 对角线遍历
        control = 0
        ret = []
        for i in range(0 , v_length + c_length -1):
            # 反向遍历
            if control == 0:
                for j in reversed(range(0 , i + 1)):
                    if j < v_length and i - j < c_length:
                        ret.append(mat[j][i-j])
                control = 1
            # 正向遍历
            else:
                for j in range(0 , i + 1):
                    if j < v_length and i - j < c_length:
                        ret.append(mat[j][i-j])
                control = 0
        return(ret)
# @lc code=end

