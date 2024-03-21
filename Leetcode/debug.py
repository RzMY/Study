# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# # 对称
# for i in range(len(matrix)):
#     for j in range(len(matrix)//2):
#         matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
# # 对角线翻转
# x = len(matrix)//2 + 1
# for i in range(len(matrix)//2 + 1):
#     for j in range(x):
#         matrix[i][j],matrix[len(matrix)-1-j][len(matrix)-1-i] = matrix[len(matrix)-1-j][len(matrix)-1-i],matrix[i][j]
#     x -= 1

# print(matrix)

# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# # 对称
# for i in range(len(matrix)):
#     for j in range(len(matrix)//2):
#         matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
# # 对角线翻转
# x = len(matrix) - 1
# for i in range(len(matrix)-1):
#     for j in range(x):
#         matrix[i][j],matrix[len(matrix)-1-j][len(matrix)-1-i] = matrix[len(matrix)-1-j][len(matrix)-1-i],matrix[i][j]
#     x -= 1

# print(matrix)

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# # 生成遍历序列
# v_length = len(mat)
# c_length = len(mat[0])
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
# # 对角线遍历
# control = 0
# ret = []
# temp_list_2 = []
# for i in range(0 , v_length + c_length -1):
#     # 反向遍历
#     if control == 0:
#         for j in reversed(range(i + 1)):
#             if j < v_length and i - j < c_length:
#                 temp_list_2.append([j,i-j])
#                 ret.append(mat[j][i-j])
#             else:
#                 continue
#         control = 1
#     # 正向遍历
#     elif control == 1:
#         for j in range(0 , i + 1):
#             if j < v_length and i - j < c_length:
#                 temp_list_2.append([j,i-j])
#                 ret.append(mat[j][i-j])
#             else:
#                 continue
#         control = 0
# print(ret)

# strs = ["flower","flower","flower","flower"]
# if  len(min(strs,key=len)) == 1:
#     print(min(strs,key=len))
# ret = ""
# for i in range(1,len(min(strs,key=len))):
#     re = strs[0][:i]
#     for word in strs:
#         if word[:i] != re:
#             print(ret)
#     ret = re
# print(ret)
# import sys

# s = "glwhcebdjbdroiurzfxxrbhzibilmcfasshhtyngwrsnbdpzgjphujzuawbebyhvxfhtoozcitaqibvvowyluvdbvoqikgojxcefzpdgahujuxpiclrrmalncdrotsgkpnfyujgvmhydrzdpiudkfchtklsaprptkzhwxsgafsvkahkbsighlyhjvbburdfjdfvjbaiivqxdqwivsjzztzkzygcsyxlvvwlckbsmvwjvrhvqfewjxgefeowfhrcturolvfgxilqdqvitbcebuooclugypurlsbdfquzsqngbscqwlrdpxeahricvtfqpnrfwbyjvahrtosovsbzhxtutyfjwjbpkfujeoueykmbcjtluuxvmffwgqjgrtsxtdimsescgahnudmsmyfijtfrcbkibbypenxnpiozzrnljazjgrftitldcueswqitrcvjzvlhionutppppzxoepvtzhkzjetpfqsuirdcyqfjsqhdewswldawhdyijhpqtrwgyfmmyhhkrafisicstqxokdmynnnqxaekzcgygsuzfiguujyxowqdfylesbzhnpznayzlinerzdqjrylyfzndgqokovabhzuskwozuxcsmyclvfwkbimhkdmjacesnvorrrvdwcgfewchbsyzrkktsjxgyybgwbvktvxyurufsrdufcunnfswqddukqrxyrueienhccpeuqbkbumlpxnudmwqdkzvsqsozkifpznwapxaxdclxjxuciyulsbxvwdoiolgxkhlrytiwrpvtjdwsssahupoyyjveedgqsthefdyxvjweaimadykubntfqcpbjyqbtnunuxzyytxfedrycsdhkfymaykeubowvkszzwmbbjezrphqildkmllskfawmcohdqalgccffxursvbyikjoglnillapcbcjuhaxukfhalcslemluvornmijbeawxzokgnlzugxkshrpojrwaasgfmjvkghpdyxt"
# for i in reversed(range(len(s) + 1)):
#     for j in range(len(s)):
#         if s[j:i+j][::-1] == s[j:i+j] and i + j <= len(s):
#             print(s[j:i+j])
#             sys.exit()


# s = "a good   example"
# while not (s[0].isalpha() and s[-1].isalpha()):
#     s = s.strip()
# ret = []
# s_part = list(s.partition(" "))
# while s_part[-1]:
#     s_part = list(s.partition(" "))
#     ret.append(s_part.pop(0))
#     s_part.pop(0)
#     s = "".join(s_part)
#     if s != '':
#         while not (s[0].isalpha() and s[-1].isalpha()):
#             s = s.strip()
# ret.reverse()
# ret = " ".join(ret)
# print(ret)

# s = "  hello world  "
# s_part = list(s.split(' '))
# ret = []
# for word in s_part:
#     if word != '':
#         ret.append(word)
# ret.reverse()
# ret = ' '.join(ret)  
# print(ret)    

# haystack = "hello"
# needle = "ll"
# for i in range(len(haystack)-len(needle)+1):
#     active = True
#     for j in range(len(needle)):
#         if haystack[i+j] != needle[j]:
#             active = False
#     if active:
#         print(i)
# print(-1)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
        
#         # 暴力匹配
#         # for i in range(len(haystack)-len(needle)+1):
#         #     active = True
#         #     for j in range(len(needle)):
#         #         if haystack[i+j] != needle[j]:
#         #             active = False
#         #     if active:
#         #         return i
#         # return -1
        
#         if haystack == needle:
#             return 0
#         if len(haystack)<len(needle):
#             return -1
#         next = []
#         if len(needle) == 1:
#             for i in range(len(haystack)-len(needle)+1):
#                 active = True
#                 for j in range(len(needle)):
#                     if haystack[i+j] != needle[j]:
#                         active = False
#                 if active:
#                     return i
#             return -1
#         for i in reversed(range(1,len(needle))):
#             next = Solution().match(haystack,needle[:i])
#             if next != []:
#                 break
#         for i in next:
#             active = True
#             for j in range(len(needle)):
#                 if i + j >= len(haystack):
#                     active = False
#                     break
#                 if haystack[i+j] != needle[j]:
#                     active = False
#             if active:
#                 return i
#         return -1
            
#     def match(self, haystack: str, needle: str) -> int:
#         next = []
#         for i in range(len(haystack)-len(needle)+1):
#             active = True
#             for j in range(len(needle)):
#                 if haystack[i+j] != needle[j]:
#                     active = False
#             if active:
#                 next.append(i)
#         return next
    
# result = Solution().strStr("mississippi","sippia")
# print(result)
# nums = [1,1,0,1,1,1]
# fast = 0
# size = len(nums)
# res = []
# count = 0
# while(fast < size):
#     if(nums[fast] == 1):
#         count += 1
#         fast += 1
#     else:
#         if count != 0:
#             res.append(count)
#             count = 0
#         fast += 1
# print(res)

nums = [1,1,0,1,1,1]
cur , max = 0 , 0
for i in range(len(nums)):
    if nums[i] == 1:
        cur += 1
    else:
        if max < cur:
            max = cur
        cur = 0
print(max(cur,max))