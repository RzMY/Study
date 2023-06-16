# print('Hello World!')
# # 这是一个单行注释
# x = 5  # 设置变量 x 的值为 5

'''
这是一个
多行注释的示例
'''

"""
这也是一个
多行注释的示例
"""

# print('Hello World!\nI love Python!')

# x = 10 + \
#     20 + \
#     30
    
# my_list = [
#     'apple',
#     'banana',
#     'orange',
# ]

# result = (10 +
#           20 +
#           30)

# x=100;y=200;z=300

# 整数类型
x = 5
y = 10

# 浮点数类型
pi = 3.14159
radius = 2.5

# 字符串类型
name = "Alice"
greeting = "Hello, world!"

# 布尔类型
is_valid = True
has_finished = False

# 列表类型
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]

# 字典类型
person = {"name": "Bob", "age": 25, "city": "New York"}

# 元组类型
point = (3, 5)

# 集合类型
grades = {85, 90, 92, 88}

# None 类型
result = None

x = 5
print(type(x))  # 输出：<class 'int'>

name = "Alice"
print(type(name))  # 输出：<class 'str'>

numbers = [1, 2, 3, 4, 5]
print(type(numbers))  # 输出：<class 'list'>

person = {"name": "Bob", "age": 25}
print(type(person))  # 输出：<class 'dict'>

x = 5
print(x)  # 输出：5

x = 10
print(x)  # 输出：10

x = "Hello"
print(x)  # 输出："Hello"

x = [1, 2, 3]
print(x)  # 输出：[1, 2, 3]

x.append(4)
print(x)  # 输出：[1, 2, 3, 4]

# 列表解包赋值
a, b, c = [1, 2, 3]
print(a, b, c)  # 输出：1 2 3

# 元组解包赋值
x, y = (4, 5)
print(x, y)  # 输出：4 5

# 字符串解包赋值
name, age = "Alice", 25
print(name, age)  # 输出："Alice" 25

# 交换两个变量的值
x, y = y, x
print(x, y)  # 输出：5 4

# 多重赋值
a, b, c = 1, 2, 3
x, y, z = "a", "b", "c"
name, age, city = "Alice", 25, "New York"

print(a, b, c)         # 输出：1 2 3
print(x, y, z)         # 输出："a" "b" "c"
print(name, age, city) # 输出："Alice" 25 "New York"

x = 5
print(x, type(x))  # 输出：5 <class 'int'>

x = "Hello"
print(x, type(x))  # 输出："Hello" <class 'str'>

x = [1, 2, 3]
print(x, type(x))  # 输出：[1, 2, 3] <class 'list'>

x = {"name": "Alice", "age": 25}
print(x, type(x))  # 输出：{'name': 'Alice', 'age': 25} <class 'dict'>

x = 5
y = x
z = x

print(x, y, z)  # 输出：5 5 5

x = 5
print(id(x))  # 输出：140733553051616

x = 10
print(id(x))  # 输出：140733553051776

#正确命名的变量示例
age = 25
name = "Alice"
is_student = True
person_name = "Bob"
num_students = 10

