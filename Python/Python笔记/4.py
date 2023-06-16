# 直接使用方括号创建空列表
my_list1 = []

# 在方括号内使用逗号分隔元素创建列表
my_list2 = [1, 2, 3, 4, 5]

# 使用list()函数将其他可迭代对象转换为列表
my_string = "Hello"
my_list3 = list(my_string)

# 使用列表解析创建列表
my_list4 = [x for x in range(1, 6)]


my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# 使用索引访问单个元素
print(my_list[0])  # 输出：apple，访问第一个元素
print(my_list[2])  # 输出：cherry，访问第三个元素

# 使用负索引从列表末尾开始访问元素
print(my_list[-1])  # 输出：elderberry，访问最后一个元素
print(my_list[-3])  # 输出：cherry，访问倒数第三个元素

# 使用切片访问多个元素
print(my_list[1:3])  # 输出：['banana', 'cherry']，访问索引为1和2的元素
print(my_list[:3])  # 输出：['apple', 'banana', 'cherry']，从头部开始访问前三个元素
print(my_list[2:])  # 输出：['cherry', 'date', 'elderberry']，从索引为2的元素开始访问到最后一个元素

# 使用步长访问元素
print(my_list[::2])  # 输出：['apple', 'cherry', 'elderberry']，每隔一个元素访问

my_list = [1, 2, 3, 4, 5]

# 添加元素
my_list.append(6)  # 在列表末尾添加一个元素
my_list.insert(0, 0)  # 在指定位置插入一个元素
my_list.extend([7, 8, 9])  # 将多个元素添加到列表末尾

# 删除元素
my_list.remove(3)  # 删除指定元素
del my_list[0]  # 删除指定位置的元素
popped_element = my_list.pop()  # 删除并返回列表末尾的元素

# 修改元素
my_list[0] = 10  # 修改指定位置的元素

# 查找元素
index = my_list.index(4)  # 返回指定元素的索引
count = my_list.count(2)  # 返回指定元素在列表中出现的次数

# 排序
my_list.sort()  # 对列表进行升序排序
my_list.reverse()  # 反转列表元素的顺序

# 切片操作
sub_list = my_list[1:4]  # 获取指定范围内的子列表

# 列表长度
length = len(my_list)  # 返回列表的长度

# 列表拷贝
new_list = my_list.copy()  # 创建列表的副本

# 清空列表
my_list.clear()  # 清空列表中的所有元素

# 列表的迭代
for item in my_list:
    print(item)

# 列表的包含性检查
if 3 in my_list:
    print("3 is in the list")

# 列表的连接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2  # 连接两个列表

# 列表的长度
length = len(my_list)  # 返回列表的长度

# 创建初始列表
my_list = [1, 2, 3]

# 使用 append() 方法在列表末尾添加一个元素
my_list.append(4)  # [1, 2, 3, 4]

# 使用 insert() 方法在指定位置插入一个元素
my_list.insert(1, 5)  # [1, 5, 2, 3, 4]

# 使用 extend() 方法将多个元素添加到列表末尾
my_list.extend([6, 7, 8])  # [1, 5, 2, 3, 4, 6, 7, 8]

# 使用 + 运算符连接两个列表
new_elements = [9, 10]
my_list = my_list + new_elements  # [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]

# 打印最终的列表
print("最终的列表：", my_list)


# 创建初始列表
my_list = [1, 2, 3, 4, 5]

# 输出修改前的列表
print("修改前的列表：", my_list)  # 输出：修改前的列表： [1, 2, 3, 4, 5]

# 修改列表元素
my_list[0] = 10  # 修改第一个元素为 10
my_list[2] = 30  # 修改第三个元素为 30
my_list[-1] = 50  # 修改最后一个元素为 50

# 输出修改后的列表
print("修改后的列表：", my_list)  # 输出：修改后的列表： [10, 2, 30, 4, 50]

# 创建初始列表
my_list = [1, 2, 3, 4, 5]

# 输出删除前的列表
print("删除前的列表：", my_list)  # 输出：删除前的列表： [1, 2, 3, 4, 5]

# 使用 del 语句删除指定位置的元素
del my_list[0]  # 删除第一个元素
del my_list[2]  # 删除第三个元素

# 输出删除后的列表
print("删除后的列表：", my_list)  # 输出：删除后的列表： [2, 3, 5]

# 使用 remove() 方法删除指定值的元素
my_list.remove(3)  # 删除值为 3 的元素

# 输出删除后的列表
print("再次删除后的列表：", my_list)  # 输出：再次删除后的列表： [2, 5]

# 使用 pop() 方法删除指定位置的元素，并返回被删除的元素值
popped_element = my_list.pop(0)  # 删除第一个元素，并将其值保存到 popped_element 变量中

# 输出删除后的列表和被删除的元素
print("最终的列表：", my_list)  # 输出：最终的列表： [5]
print("被删除的元素：", popped_element)  # 输出：被删除的元素： 2


# 创建初始列表
my_list = [1, 2, 3, 4, 5]

# 方法一：使用切片复制整个列表
copied_list = my_list[:]  # 通过切片复制整个列表

# 方法二：使用 list() 函数复制列表
copied_list = list(my_list)  # 使用 list() 函数复制列表

# 方法三：使用 copy() 方法复制列表
copied_list = my_list.copy()  # 使用 copy() 方法复制列表

# 输出原始列表和复制后的列表
print("原始列表：", my_list)  # 输出：原始列表： [1, 2, 3, 4, 5]
print("复制后的列表：", copied_list)  # 输出：复制后的列表： [1, 2, 3, 4, 5]

import copy

# 创建原始列表
original_list = [1, [2, 3], 4, 5]

# 浅复制
shallow_copy = original_list.copy()

# 深复制
deep_copy = copy.deepcopy(original_list)

# 修改原始列表的元素
original_list[1][0] = 100

# 输出浅复制和深复制后的列表
print("浅复制：", shallow_copy)  # 输出：浅复制： [1, [100, 3], 4, 5]
print("深复制：", deep_copy)  # 输出：深复制： [1, [2, 3], 4, 5]


# 创建列表
my_list = [10, 20, 30, 40, 50]

# 查找元素索引
index = my_list.index(30)  # 查找元素值为 30 的索引位置

# 输出结果
print("元素索引：", index)  # 输出：元素索引： 2

# 创建列表
my_list = [1, 2, 3, 4, 5]

# 方法一：使用 reverse() 方法翻转列表
my_list.reverse()
print("方法一翻转后的列表：", my_list)  # 输出：方法一翻转后的列表： [5, 4, 3, 2, 1]

# 方法二：使用 reversed() 函数翻转列表
reversed_list = list(reversed(my_list))
print("方法二翻转后的列表：", reversed_list)  # 输出：方法二翻转后的列表： [1, 2, 3, 4, 5]

# 创建列表
my_list = ["apple", "banana", "cherry", "date"]

# 方法一：使用 sort() 方法进行原地排序
my_list.sort()
print("方法一原地排序：", my_list)  # 输出：方法一原地排序： ['apple', 'banana', 'cherry', 'date']

# 方法二：使用 sorted() 函数进行排序并返回新列表
sorted_list = sorted(my_list)
print("方法二排序后的列表：", sorted_list)  # 输出：方法二排序后的列表： ['apple', 'banana', 'cherry', 'date']

# 方法三：自定义排序
my_list.sort(key=len)  # 按照字符串长度进行排序
print("按照字符串长度排序：", my_list)  # 输出：按照字符串长度排序： ['date', 'apple', 'cherry', 'banana']

my_list.sort(reverse=True)  # 按照字符串反向排序
print("按照字符串反向排序：", my_list)  # 输出：按照字符串反向排序： ['date', 'cherry', 'banana', 'apple']


# for item in iterable:
#     # 在每次迭代中执行的代码块

# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
# 输出:
# apple
# banana
# cherry

# 使用 range() 函数生成数字范围
for i in range(1, 5):
    print(i)
# 输出:
# 1
# 2
# 3
# 4


# 遍历可迭代对象
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# 输出:
# apple
# banana
# cherry

# 使用 range() 函数生成数字范围
for i in range(1, 5):
    print(i)
# 输出:
# 1
# 2
# 3
# 4

# 遍历字典的键或值
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in person.keys():
    print(key)
# 输出:
# name
# age
# city

for value in person.values():
    print(value)
# 输出:
# John
# 30
# New York

for key, value in person.items():
    print(key, value)
# 输出:
# name John
# age 30
# city New York

# 遍历多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(name, age)
# 输出:
# Alice 25
# Bob 30
# Charlie 35
