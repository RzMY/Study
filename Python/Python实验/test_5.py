#本关任务：编写函数f，求1+2+3+...N的和

# num = int(input())

# def f(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum

# print(f(num))


#本关任务：编写函数，交换指定字典的key和value
# dd = eval(input())

# def reverse_dict(d):
#     new_dict = {}
#     for key,value in d.items():
#         new_dict[value] = key
#     return new_dict

# print(reverse_dict(dd))

#编写函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串

# s = input()

# def f(s):
#     new_s = ''
#     for i in s:
#         if i.isalpha():
#             new_s += i
#     return new_s

# print(f(s))

#给定两个列表，编写一个函数实现比较两个列表中对应下标位置的元素的大小，将大的元素组成一个新的列表

# l1 = eval(input())
# l2 = eval(input())

# def f(l1,l2):
#     new_l = []
#     for i in range(len(l1)):
#         if l1[i] > l2[i]:
#             new_l.append(l1[i])
#         else:
#             new_l.append(l2[i])
#     return new_l

# print(f(l1,l2))

#定义一个 compare 函数和一个max_value 函数，compare 函数用于比较两个数的大小，max_value 函数用于得到一串整型数据中的最大值,函数嵌套

def compare(a,b):
    if a > b:
        return a
    else:
        return b

def max_value(l):
    max = l[0]
    for i in range(1,len(l)):
        max = compare(max,l[i])
    return max

max_number = max_value(eval(input()))     # eval(input())是将输入的字符串转换为列表
print(max_number)