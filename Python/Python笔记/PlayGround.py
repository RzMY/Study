#求斐波那契数列中第 n 个数的值，n 是正整数,斐波那契数除了第 1 项和第 2 项是 1 以外，其它的每一项都等于前两项的和。

# n = int(input())
# a1 , a2 = 1 , 1
# if n == 1 or n == 2:
#     print(1)
# elif n > 2:
#     x = 0
#     for i in range(2,n):
#         x = 2
#         x , a2 = x + a2 , x
#     print(x)

# n = int(input())
# a1, a2 = 1, 1
# if n == 1 or n == 2:
#     print(1)
# elif n > 2:
#     for i in range(3, n+1):
#         a1, a2 = a2, a1 + a2
#     print(a2)

# chars = ['a', 'c', 'x', 'x', 'd', 'c', 'f', 'j', 'f', 'f', 'g', 'd']

# c = input()
# count = 0
# for char in chars:
#     if char == c:
#         count += 1
# print(f"字母{c}出现的次数为{count}")

# result = {}
# chars = ['a', 'c', 'x', 'x', 'd', 'c', 'f', 'j', 'f', 'f', 'g', 'd']
# for i in chars:
#     if i not in result:
#         result[i] = 1
#     else:
#         result[i] += 1
# print(result)

# dic = {
# 'a':100,
# 'b':200,
# 'c':300
# }

# new_dic = {k:v for v , k in dic.items()}
# print(new_dic)

# words = ['python','computer','book','program']
# s = input()
# count = 0
# for word in words:
#     for letter in word:
#         if letter == s:
#             count += 1
# print(f"字母{s}出现的次数是{count}")

# s = input()
# s = s.upper()
# result = {}
# for letter in s:
#     if letter not in result:
#         result[letter] = 1
#     else:
#         result[letter] += 1
# print(result)

# s = input()
# s = s.split(',')
# max_word = max(s,key = len)
# print(max_word)

# s = input()
# s = s.lower
# table = str.maketrans("abcdefghijklmnopqrstuvwxyz","xyzabcdefghijklmnopqrstuvw")
# s = s.translate(table)
# print(s)

# students = [
# {'name':'张三','age':18,'score':98,'tel':'13888889988','gender':'female'},
# {'name':'李四','age':28,'score':95,'tel':'13886666666','gender':'male'},
# {'name':'王五','age':17,'score':47,'tel':'13888889999','gender':'unknown'},
# {'name':'刘六','age':16,'score':16,'tel':'13886666668','gender':'unknown'},]

# n = input()

# if n == 'socre':
#     students = sorted(students,key = lambda x:x["score"],reverse=True)
#     print(students)
# elif n == 'age':
#     students = sorted(students,key = lambda x:x["age"],reverse=True)
#     print(students)

# n = int(input())
# new_words = []
# words = ['hello','good','','','yes','','ok','']
# for word in words:
#     if word != '':
#         new_words.append(word)
#     else:
#         if n > 0:
#             n -= 1
#         else:
#             new_words.append(word)
# print(new_words)

# n = int(input())
# result = [n]
# while n != 1:
#     if n % 2 == 0:
#         n //= 2
#         result.append(n)
#     else:
#         n = 3*n + 1
#         result.append(n)
# print(result)

# str1 = "Hello,World!"
# result1 = str1.find("World")# 查找第一次出现的位置，不存在返回-1
# result2 = str1.rfind("o")# 查找最后一次出现的位置，不存在返回-1
# result3 = str1.index("World")# 查找第一次出现的位置，不存则异常
# result4 = str1.rindex("o")# 查找最后一次出现的位置，不存则异常
# print(result1) # 输出：7
# print(result2) # 输出：8
# print(result3) # 输出：7
# print(result4) # 输出：8

print (list(enumerate([4,5,8])))