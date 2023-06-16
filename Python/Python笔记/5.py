# 字典的创建
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 dict() 函数创建字典
person = dict(name='John', age=30, city='New York')

# 使用键值对列表创建字典
person = dict([('name', 'John'), ('age', 30), ('city', 'New York')])

# 使用键的迭代创建字典
keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']
person = dict(zip(keys, values))


# 创建字典
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 访问键
keys = person.keys()
print(keys)  # 输出: dict_keys(['name', 'age', 'city'])

# 访问值
values = person.values()
print(values)  # 输出: dict_values(['John', 30, 'New York'])

# 访问键值对
items = person.items()
print(items)  # 输出: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# 遍历字典的键
for key in person.keys():
    print(key)
# 输出:
# name
# age
# city

# 遍历字典的值
for value in person.values():
    print(value)
# 输出:
# John
# 30
# New York

# 遍历字典的键值对
for key, value in person.items():
    print(key, value)
# 输出:
# name John
# age 30
# city New York


# 创建字典
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用键来查询值
name = person['name']
print(name)  # 输出: John

age = person['age']
print(age)  # 输出: 30

# 使用 get() 方法查询值
city = person.get('city')
print(city)  # 输出: New York

# 查询不存在的键
country = person.get('country')
print(country)  # 输出: None

# 使用 get() 方法并提供默认值
country = person.get('country', 'Unknown')
print(country)  # 输出: Unknown

# 使用 in 关键字检查键是否存在
if 'name' in person:
    print('Name is present')  # 输出: Name is present

if 'country' in person:
    print('Country is present')
else:
    print('Country is not present')  # 输出: Country is not present
    
    
# 创建一个空字典
person = {}

# 向字典添加键值对
person['name'] = 'John'
person['age'] = 30
person['city'] = 'New York'
print(person)  # 输出: {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 update() 方法添加多个键值对
person.update({'occupation': 'Engineer', 'country': 'USA'})
print(person)  # 输出: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Engineer', 'country': 'USA'}

# 使用字典推导式添加键值对
# numbers = {1: 'one', 2: 'two', 3: 'three'}
# squared_numbers = {key: value ** 2 for key, value in numbers.items()}
# print(squared_numbers)  # 输出: {1: 1, 2: 4, 3: 9}


# 创建字典
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 修改键对应的值
person['age'] = 35
print(person)  # 输出: {'name': 'John', 'age': 35, 'city': 'New York'}


# 创建字典
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 del 关键字删除键值对
del person['age']
print(person)  # 输出: {'name': 'John', 'city': 'New York'}

# 使用 pop() 方法删除键值对，并返回被删除的值
city = person.pop('city')
print(person)  # 输出: {'name': 'John'}
print(city)  # 输出: New York

# 删除不存在的键值对时，可以提供默认值
country = person.pop('country', 'Unknown')
print(person)  # 输出: {'name': 'John'}
print(country)  # 输出: Unknown

# 清空字典
person.clear()
print(person)  # 输出: {}


# 创建字典
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 popitem() 方法删除并返回键值对
key, value = person.popitem()
print(key, value)  # 输出: city New York
print(person)  # 输出: {'name': 'John', 'age': 30}


import copy

# 创建字典
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 copy() 方法进行浅复制
person_copy = person.copy()

# 修改原字典的值
person['age'] = 35

print(person)        # 输出: {'name': 'John', 'age': 35, 'city': 'New York'}
print(person_copy)   # 输出: {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 dict() 函数进行浅复制
person_copy = dict(person)

# 修改原字典的值
person['age'] = 35

print(person)        # 输出: {'name': 'John', 'age': 35, 'city': 'New York'}
print(person_copy)   # 输出: {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用 copy 模块进行深复制
person_copy = copy.deepcopy(person)

# 修改原字典的值
person['age'] = 35

print(person)        # 输出: {'name': 'John', 'age': 35, 'city': 'New York'}
print(person_copy)   # 输出: {'name': 'John', 'age': 30, 'city': 'New York'}