# import math
# print(dir(math))

# help(len)

# import this


# # 整数
# my_integer = 10

# # 浮点数
# my_float = 3.14

# # 复数
# my_complex = 1 + 2j

# # 布尔值
# my_bool = True

my_string = 'Hello, World!'
multi_line_string = '''This is a
multi-line
string.'''

print('This is a single-quoted string with a \'single quote\'.')

print("This is a double-quoted string with a \"double quote\".")

print("This is a string with a backslash \\.")

print("This is a string with\na newline.")

print("This is a string with a\ttab.")

print("This is a string with a\rreturn.")

print("This is a string with a\bbackspace.")

print("This is a string with a\fform feed.")

print("This is a string with an octal character: \101")  # 八进制字符 'A'

print("This is a string with a hexadecimal character: \x41")  # 十六进制字符 'A'


# 使用单引号定义字符串
single_quoted_string = 'Hello, World!'

# 使用双引号定义字符串
double_quoted_string = "Hello, World!"

# 使用三重引号定义多行字符串
multi_line_string = '''This is a
multi-line
string.'''

# 使用转义字符定义包含特殊字符的字符串
escaped_string = "This is a \"quoted\" string."

# 使用原始字符串定义字符串
raw_string = r'C:\path\to\file.txt'

import math

# 加法
a = 5 + 3
print(a)

# 减法
b = 10 - 7
print(b)

# 乘法
c = 4 * 6
print(c)

# 除法
d = 15 / 5
print(d)

# 取余数
e = 17 % 4
print(e)

# 整除
f = 17 // 4
print(f)

# 幂运算
g = 2 ** 3
print(g)

# 使用math模块进行高级数学运算
h = math.sin(math.pi / 2)  # 正弦函数
print(h)

i = math.exp(2)  # 指数函数
print(i)

j = math.log(10)  # 对数函数
print(j)

# 绝对值运算
h = abs(-5)

# 增量赋值
i = 5
i += 3

# 减量赋值
j = 10
j -= 7

# 乘量赋值
k = 4
k *= 6

# 除量赋值
l = 15
l /= 5

# 幂量赋值
m = 2
m **= 3

# 取余量赋值
n = 17
n %= 4

# 整除量赋值
o = 17
o //= 4

# 布尔运算
p = True and False
q = True or False
r = not True

import math

# 数字运算
a = 5 + 3  # 加法
b = 10 - 7  # 减法
c = 4 * 6  # 乘法
d = 15 / 5  # 除法
e = 17 % 4  # 取余数
f = 17 // 4  # 整除
g = 2 ** 3  # 幂运算

# 绝对值运算
h = abs(-5)

# 增量赋值
i = 5
i += 3  # 相当于 i = i + 3

# 减量赋值
j = 10
j -= 7  # 相当于 j = j - 7

# 乘量赋值
k = 4
k *= 6  # 相当于 k = k * 6

# 除量赋值
l = 15
l /= 5  # 相当于 l = l / 5

# 幂量赋值
m = 2
m **= 3  # 相当于 m = m ** 3

# 取余量赋值
n = 17
n %= 4  # 相当于 n = n % 4

# 整除量赋值
o = 17
o //= 4  # 相当于 o = o // 4

# 布尔运算
p = True and False  # 与运算
q = True or False  # 或运算
r = not True  # 非运算

# 打印结果
print("数字运算结果：")
print(a)  # 输出：8
print(b)  # 输出：3
print(c)  # 输出：24
print(d)  # 输出：3.0
print(e)  # 输出：1
print(f)  # 输出：4
print(g)  # 输出：8

print("绝对值运算结果：")
print(h)  # 输出：5

print("增量赋值结果：")
print(i)  # 输出：8

print("减量赋值结果：")
print(j)  # 输出：3

print("乘量赋值结果：")
print(k)  # 输出：24

print("除量赋值结果：")
print(l)  # 输出：3.0

print("幂量赋值结果：")
print(m)  # 输出：8

print("取余量赋值结果：")
print(n)  # 输出：1

print("整除量赋值结果：")
print(o)  # 输出：4

print("布尔运算结果：")
print(p)  # 输出：False
print(q)  # 输出：True
print(r)  # 输出：False


# 字符串连接
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # 输出：Hello World

# 字符串复制
str1 = "Hello"
result = str1 * 3
print(result)  # 输出：HelloHelloHello

# 字符串长度
str1 = "Hello"
length = len(str1)
print(length)  # 输出：5

# 字符串索引和切片
str1 = "Hello"
print(str1[0])  # 输出：H
print(str1[1:4])  # 输出：ell

# 字符串转换为大写或小写
str1 = "Hello"
result1 = str1.upper()
result2 = str1.lower()
print(result1)  # 输出：HELLO
print(result2)  # 输出：hello

# 字符串查找和替换
str1 = "Hello, World!"
result1 = str1.find("World")
result2 = str1.replace("World", "Python")
print(result1)  # 输出：7
print(result2)  # 输出：Hello, Python!

# 字符串分割和连接
str1 = "Hello, World!"
result1 = str1.split(",")
result2 = "-".join(result1)
print(result1)  # 输出：['Hello', ' World!']
print(result2)  # 输出：Hello- World!


text = "  Hello, World!  "

# 去除两端的空格
stripped_text = text.strip()
print(stripped_text)  # 输出: "Hello, World!"

# 去除左侧的空格
left_stripped_text = text.lstrip()
print(left_stripped_text)  # 输出: "Hello, World!  "

# 去除右侧的空格
right_stripped_text = text.rstrip()
print(right_stripped_text)  # 输出: "  Hello, World!"

decimal = 10

# 转换为二进制
binary = bin(decimal)
print(binary)  # 输出: '0b1010'

# 转换为八进制
octal = oct(decimal)
print(octal)  # 输出: '0o12'

# 转换为十六进制
hexadecimal = hex(decimal)
print(hexadecimal)  # 输出: '0xa'

binary = '0b1010'

# 转换为十进制
decimal = int(binary, 2)
print(decimal)  # 输出: 10

octal = '0o12'

# 转换为十进制
decimal = int(octal, 8)
print(decimal)  # 输出: 10

hexadecimal = '0xa'

# 转换为十进制
decimal = int(hexadecimal, 16)
print(decimal)  # 输出: 10

name = "Alice"
age = 25

# 使用百分号（%）操作符进行字符串格式化
message = "My name is %s and I'm %d years old." % (name, age)
print(message)  # 输出: "My name is Alice and I'm 25 years old."

# 使用字符串的 format() 方法进行字符串格式化
message = "My name is {} and I'm {} years old.".format(name, age)
print(message)  # 输出: "My name is Alice and I'm 25 years old."

# 使用 f-strings 进行字符串格式化
message = f"My name is {name} and I'm {age} years old."
print(message)  # 输出: "My name is Alice and I'm 25 years old."


if 5 > 3:
    print("5 is greater than 3")  # 在if语句块中，需要缩进的代码

    if 4 > 2:
        print("4 is greater than 2")  # 在嵌套的if语句块中，需要进一步缩进的代码

    print("End of inner if block")  # 结束内部if语句块后，回到外部if语句块的缩进级别

print("End of if block")  # 结束外部if语句块，回到没有缩进的代码级别
