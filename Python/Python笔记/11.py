names=['zhangsan','lisi','chris','jerry','henry']
people_name = input()
if people_name in names:
    print("zai")
else:
    print("buzai")

#求列表中的最大数和它的索引
nums = [3, 1, 9, 4, 2, 0, 7, 9, 5]
max_num = max(nums)
for i in range(len(nums)):
    if max_num == nums[i]:
        print("最大数为：", max_num, "索引为：", i)
        
#八位老师随机安排三个办公室
import random
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rooms = [[], [], []]
for teacher in teachers:
    random.choice(rooms).append(teacher)
print(rooms)

#判断两个数相减是否为奇数
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
if (num1 - num2) % 2 != 0:
    print('两个数相减为奇数', num1 - num2)
else:
    print('两个数相减为偶数', num1 - num2)
    
#用for循环输出0~100所有奇数
for i in range(101):
    if i % 2 != 0:
        print(i)
        
        
#用while循环输出0~100所有偶数
i = 0
while i <= 100:
    print(i)
    i += 2
    
#用循环计算出1到100求和的结果
result = 0
for i in range(1, 101):
    result += i
print(result)

#统计100以内个位数是2且能被3整除的个数
count = 0
for i in range(1, 101):
    if i % 10 == 2 and i % 3 == 0:
        count += 1
print(count)
#
#输入任意一个正整数，求它是几位数
num = int(input("请输入一个正整数："))
count = 0
while True:
    num //= 10
    count += 1
    if num == 0:
        break
print(f"{count}位数")

#打印所有水仙花数
for i in range(100,1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge**3 + shi**3 + bai**3 == i:
        print(i)
        
#重复输入
while True:
    content = input("请输入内容：")
    if content == 'exit':
        break
print("循环结束")

#统计101~200中素数的个数，并且输出所有素数
count = 0
nums = []
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1
        nums.append(i)
print("素数个数为：", count)
print("素数为：", nums)

#九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "*", i, "=", i*j, end=" ")
    print()
    
#百马百担，有100匹马，驮100担货，大马驮3担，中马驮2担，两匹小马驮1担，问大，中，小马各有多少？
for i in range(1, 34):
    for j in range(1, 50):
        for k in range(1, 100):
            if i + j + k == 100 and 3*i + 2*j + k/2 == 100:
                print("大马：", i, "中马：", j, "小马：", k)
                
#0.08毫米要两倍多少次才能到达8848.13？
height = 0.08/1000
count = 0
while height < 8848.13:
    count += 1
    height *= 2
print(count)

#求斐波那契数列中第n个数的值，n是正整数,斐波那契数除了第1项和第2项是1以外，其它的每一项都等于前两项的和。
n = int(input("请输入一个正整数："))
a1 = 1
a2 = 2
for i in range(3, n+1):
    a3 = a1 + a2
    a1 , a2 = a2 , a3
# print(a3)

#让用户输入姓名，如果姓名已经存在，提示用户.如果姓名不存在，继续输入年龄，并存入列表里
persons = [
    {'name': 'zhangsan', 'age': 18},
    {'name': 'lisi', 'age': 20},
    {'name': 'wangwu', 'age': 29},
    {'name': 'jerry', 'age': 21}
]

name = input("请输入姓名：")
for person in persons:
    if name == person['name']:
        print("姓名已存在")
        break
else:
    age = int(input("请输入年龄："))
    persons.append({'name': name, 'age': age})
print(persons)


#统计列表中每个字符出现的次数
#a c x x d c f j f f g d
chars = ['a', 'c', 'x', 'x', 'd', 'c', 'f', 'j', 'f', 'f', 'g', 'd']
x ={}
for i in chars:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
print(x)

#统计列表中每个字符出现的次数
#a c x x d c f j f f g d
chars = ['a', 'c', 'x', 'x', 'd', 'c', 'f', 'j', 'f', 'f', 'g', 'd']
x ={}
for i in chars:
    if i not in x:
        x[i] = chars.count(i)\
# print(x)

#将键和值互换
dic = {
    'a':100,
    'b':200,
    'c':300
}
new_dic = {k:v for v,k in dic.items()}
print(new_dic)

#统计字母出现的次数
s = input()
a = ['python','computer','book','program']
count = 0
for word in a:
    for letter in s:
        if letter in word:
            count += 1
print(count)

# 返回一个0到1之间的随机浮点数
num = random.random() 
print(num)  # 输出：0.123456789


# 返回一个在指定范围内的随机整数，包括a和b
num = random.randint(1, 10)
print(num)  # 输出：7

# 从序列中随机选择一个元素并返回
fruit = random.choice(['apple', 'banana', 'cherry'])
print(fruit)  # 输出：'banana'

# 将序列中的元素随机排序，原地修改序列
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # 输出：[4, 2, 5, 1, 3]

# 从给定的总体中随机选择k个独立样本，返回一个新的列表
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
hand = random.sample(cards, 5)
print(hand)  # 输出：['6', 'J', 'A', '9', 'K']