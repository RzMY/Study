# 统计某个子串在字符串中出现的次数
sentence = "Hello, hello, hello!"
count = sentence.count("hello")
print(count)  # 输出结果: 2

# partition()方法从左往右查找第一个出现的分隔符，并将字符串分成三部分：分隔符左边的子串、分隔符本身、分隔符右边的子串。
message = "Hello, world!"
result = message.partition(",")
print(result)  # 输出结果: ('Hello', ',', ' world!')

# rpartition()方法从右侧开始查找分隔符，将字符串从分隔符最后一次出现的位置进行分割。
rpartition_result = sentence.rpartition("in")
print(rpartition_result)
# 输出结果: ('I love programming ', 'in', ' Python')

# capitalize()是Python字符串对象的方法，用于将字符串的第一个字符转换为大写，并将其余字符保持为小写。
text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)
# 输出结果: "Hello, world!"

# title()是Python字符串对象的方法，用于将字符串中每个单词的首字母转换为大写，而其他字母保持小写。该方法返回一个新的字符串，原始字符串保持不变。
text = "hello, world!"
title_text = text.title()
print(title_text)
# 输出结果: "Hello, World!"

# swapcase()是Python字符串对象的方法，用于将字符串中的大写字母转换为小写字母，同时将小写字母转换为大写字母。该方法返回一个新的字符串，原始字符串保持不变。
text = "Hello, World!"
swapped_text = text.swapcase()
print(swapped_text)
# 输出结果: "hELLO, wORLD!"

# 字符串替换
str1 = "Hello, World!"
result = str1.replace("World", "Python")
print(result)  # 输出：Hello, Python!

# maketrans()用于创建字符映射转换表，该表可以被translate()方法使用
table = str.maketrans("aeiou", "12345")
text = "hello world"
translated_text = text.translate(table)
print(translated_text)
# 输出结果: "h2ll4 w4rld"


# cneter居中对齐，返回指定宽度的新字符串，原字符串居中，两侧填充指定字符，默认空格
text = "Hello"
centered_text = text.center(10, "*")
print(centered_text)
# 输出结果: "**Hello***"

# ljust左对齐，返回指定宽度的新字符串，原字符串左对齐，右侧填充指定字符，默认空格
text = "Hello"
left_aligned_text = text.ljust(10, "*")
print(left_aligned_text)
# 输出结果: "Hello*****"

# rjust右对齐，返回指定宽度的新字符串，原字符串右对齐，左侧填充指定字符，默认空格
text = "Hello"
right_aligned_text = text.rjust(10, "*")
print(right_aligned_text)
# 输出结果: "*****Hello"

# 测试字符串的特定属性

# isalnum() - 测试字符串是否为数字或字母字符
text = "Hello123"
print(text.isalnum())  # True

text = "Hello123!"
print(text.isalnum())  # False

# isalpha() - 测试字符串是否为字母字符
text = "Hello"
print(text.isalpha())  # True

text = "Hello123"
print(text.isalpha())  # False

# isdigit() - 测试字符串是否为数字字符
text = "123"
print(text.isdigit())  # True

text = "Hello123"
print(text.isdigit())  # False

# isspace() - 测试字符串是否为空白字符
text = "  \t\n"
print(text.isspace())  # True

text = "Hello 123"
print(text.isspace())  # False

# isupper() - 测试字符串是否为大写字母
text = "HELLO"
print(text.isupper())  # True

text = "Hello"
print(text.isupper())  # False

# islower() - 测试字符串是否为小写字符
text = "hello"
print(text.islower())  # True

text = "Hello"
print(text.islower())  # False

# exec(source, globals=None, locals=None)


# 定义一个包含动态生成代码的字符串
code = """
for i in range(5):
    print(i)
"""

# 执行字符串中的代码
# exec(code)

# eval(expression, globals=None, locals=None)

# 定义一个包含表达式的字符串
expression = "2 + 3 * 4"

# 执行字符串中的表达式
result = eval(expression)
print(result)  # 输出：14


# enumerate(iterable, start=0)

fruits = ['apple', 'banana', 'orange']

# 遍历列表并获取索引和元素值
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 输出：
# 0 apple
# 1 banana
# 2 orange

# sum(iterable, start=0)

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 输出：15

# 指定起始值为 10
total_with_start = sum(numbers, 10)
print(total_with_start)  # 输出：25

# 对字符串中的数字进行求和
digits = '12345'
total_digits = sum(int(digit) for digit in digits)
print(total_digits)  # 输出：15

text = "Hello, 你好"
encoded_text = text.encode('utf-8')
print(encoded_text)  # 输出：b'Hello, \xe4\xbd\xa0\xe5\xa5\xbd'

encoded_text = b'Hello, \xe4\xbd\xa0\xe5\xa5\xbd'
decoded_text = encoded_text.decode('utf-8')
print(decoded_text)  # 输出：Hello, 你好


# ord()和chr()是用于字符和Unicode码点之间转换的内置函数
# ord()函数示例
print(ord('A'))  # 输出：65
print(ord('你'))  # 输出：20320

# chr()函数示例
print(chr(65))  # 输出：A
print(chr(20320))  # 输出：你


lambda arguments: expression

# 使用lambda函数计算两个数的和
add = lambda x, y: x + y
result = add(3, 4)
print(result)  # 输出：7

# 使用lambda函数进行平方运算
square = lambda x: x ** 2
result = square(5)
print(result)  # 输出：25

