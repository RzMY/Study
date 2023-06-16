# def greet():
#     print("Hello, world!")

# greet()

# def greet(name):
#     print("Hello,", name)

# greet("Alice")

# def greet():
#     print("Hello, world!")

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print(f"Hello, {self.name}!")

# person = Person("Alice")

# print(callable(greet))          # 输出: True，函数greet是可调用的
# print(callable(person.say_hello))  # 输出: True，person对象的say_hello方法是可调用的
# print(callable(person))          # 输出: False，person对象本身不是可调用的


# def greet(name):
#     """
#     打印问候语

#     参数:
#     name (str): 要问候的人的姓名

#     返回:
#     None
#     """
#     print("Hello,", name)

# # 使用help()函数访问函数文档字符串
# help(greet)

# # 使用__doc__属性访问函数文档字符串
# print(greet.__doc__)


# 定义一个修改值的函数
def modify_value(x):
    """
    修改值的函数
    参数:
        x (int): 要修改的值
    返回:
        None
    """
    x += 10
    print("Inside function: x =", x)

# 创建一个整数对象
value = 5

# 调用函数进行值的修改
modify_value(value)

# 输出修改后的值
print("Outside function: value =", value)


# 定义一个修改列表的函数
def modify_list(lst):
    """
    修改列表的函数
    参数:
        lst (list): 要修改的列表
    返回:
        None
    """
    lst.append(4)
    print("Inside function: lst =", lst)

# 创建一个列表对象
my_list = [1, 2, 3]

# 调用函数进行列表的修改
modify_list(my_list)

# 输出修改后的列表
print("Outside function: my_list =", my_list)

# def greet(name, message):
#     """
#     打招呼的函数
#     参数:
#         name (str): 姓名
#         message (str): 信息
#     返回:
#         None
#     """
#     print(f"Hello, {name}! {message}")

# 使用关键字参数调用函数
# greet(name="Alice", message="How are you?")
# greet(message="Nice to meet you.", name="Bob")


# def greet(name, message="Hello"):
#     """
#     打招呼的函数
#     参数:
#         name (str): 姓名
#         message (str): 信息，默认值为"Hello"
#     返回:
#         None
#     """
#     print(f"{message}, {name}!")

# # 使用默认值调用函数
# greet("Alice")
# greet("Bob", message="Hi")


def sum_numbers(*numbers):
    """
    计算任意数量数字的和
    参数:
        *numbers (float): 任意数量的数字
    返回:
        float: 数字的和
    """
    total = 0
    for num in numbers:
        total += num
    return total

# 调用函数
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # 输出：15

result = sum_numbers(10, 20, 30)
print(result)  # 输出：60


def print_person_info(**person_info):
    """
    打印个人信息
    参数:
        **person_info (str): 个人信息，键值对形式
    返回:
        None
    """
    for key, value in person_info.items():
        print(f"{key}: {value}")

# 调用函数
print_person_info(name="Alice", age=25, city="New York")
print_person_info(name="Bob", occupation="Engineer")


print_person_info(name="Alice", age=25, city="New York")
# 输出：
# name: Alice
# age: 25
# city: New York

print_person_info(name="Bob", occupation="Engineer")
# 输出：
# name: Bob
# occupation: Engineer

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# 使用*解包可迭代对象
args = ["Alice", 25]
greet(*args)  # 等价于 greet("Alice", 25)

# 使用**解包字典
kwargs = {"name": "Bob", "age": 30}
greet(**kwargs)  # 等价于 greet(name="Bob", age=30)


def factorial(n):
    if n == 0:  # 基本情况
        return 1
    else:  # 递归情况
        return n * factorial(n-1)

result = factorial(5)  # 调用递归函数计算阶乘
print(result)  # 输出结果: 120

def process_data(data):
    match data:
        case 0:
            print("数据为0")
        case 1:
            print("数据为1")
        case 2 | 3:
            print("数据为2或3")
        case _:
            print("数据为其他值")

process_data(2)  # 输出结果: 数据为2或3
process_data(5)  # 输出结果: 数据为其他值
