# 使用小括号创建元组
my_tuple = (1, 2, 3)
print(my_tuple)  # 输出: (1, 2, 3)

# 空元组
empty_tuple = ()
print(empty_tuple)  # 输出: ()

# 元组中的元素可以是不同的数据类型
mixed_tuple = (1, "hello", True)
print(mixed_tuple)  # 输出: (1, 'hello', True)

# 使用 tuple() 函数创建元组
my_tuple = tuple([1, 2, 3])
print(my_tuple)  # 输出: (1, 2, 3)

# 创建一个包含三个元素的元组
my_tuple = (1, 2, 3)

# 使用元组解包将元组的值分配给多个变量
a, b, c = my_tuple

print(a)  # 输出: 1
print(b)  # 输出: 2
print(c)  # 输出: 3


my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[0])  # 输出: 1，访问第一个元素
print(my_tuple[2])  # 输出: 3，访问第三个元素
print(my_tuple[-1])  # 输出: 5，访问最后一个元素


my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[1:4])  # 输出: (2, 3, 4)，获取索引 1 到索引 3 的元素
print(my_tuple[:3])  # 输出: (1, 2, 3)，获取索引 0 到索引 2 的元素
print(my_tuple[2:])  # 输出: (3, 4, 5)，获取索引 2 到最后一个元素的元素
#使用花括号 {} 来创建集合，将元素逐个放入花括号内
my_set = {1, 2, 3}
print(my_set)  # 输出: {1, 2, 3}

#使用 set() 函数创建集合，可以传入可迭代对象作为参数，例如列表、元组或字符串
my_set = set([1, 2, 3])
print(my_set)  # 输出: {1, 2, 3}

my_set = set((1, 2, 3))
print(my_set)  # 输出: {1, 2, 3}

my_set = set("hello")
print(my_set)  # 输出: {'h', 'l', 'e', 'o'}

#如果要创建空集合，不能使用空花括号 {}，因为这样会创建一个空字典。要创建空集合，必须使用 set() 函数
empty_set = set()
print(empty_set)  # 输出: set()

my_set = {1, 2, 3}
my_set.add(4)  # 向集合中添加元素 4
print(my_set)  # 输出: {1, 2, 3, 4}


my_set = {1, 2, 3}
my_set.update([4, 5, 6])  # 向集合中添加元素 4, 5, 6
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3}
my_set.update((4, 5, 6))  # 向集合中添加元素 4, 5, 6
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3}
my_set.update({4, 5, 6})  # 向集合中添加元素 4, 5, 6
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # 删除元素 3
print(my_set)  # 输出: {1, 2, 4, 5}

my_set.remove(6)  # 尝试删除不存在的元素 6，引发 KeyError 异常

my_set = {1, 2, 3, 4, 5}
my_set.discard(3)  # 删除元素 3
print(my_set)  # 输出: {1, 2, 4, 5}

my_set.discard(6)  # 尝试删除不存在的元素 6，不会引发异常
print(my_set)  # 输出: {1, 2, 4, 5}


my_set = {1, 2, 3, 4, 5}
element = my_set.pop()  # 删除任意一个元素，并将其返回
print(element)  # 输出: 随机返回集合中的一个元素
print(my_set)  # 输出: 删除了一个元素后的集合


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 并集
union = set1.union(set2)
print(union)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 交集
intersection = set1.intersection(set2)
print(intersection)  # 输出: {4, 5}

# 差集
difference = set1.difference(set2)
print(difference)  # 输出: {1, 2, 3}

# 对称差集
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # 输出: {1, 2, 3, 6, 7, 8}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 并集
union = set1 | set2
print(union)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 交集
intersection = set1 & set2
print(intersection)  # 输出: {4, 5}

# 差集
difference = set1 - set2
print(difference)  # 输出: {1, 2, 3}

# 对称差集
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # 输出: {1, 2, 3, 6, 7, 8}


