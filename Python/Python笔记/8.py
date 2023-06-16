# while 条件:
    # 代码块


count = 0

while count < 5:
    print("Count:", count)
    count += 1

print("Loop ended.")


# while True:
#     # 代码块
#     if some_condition:
#         break  # 根据条件跳出循环


active = True

while active:
    user_input = input("请输入内容：")
    if user_input == 'quit':
        active = False
    else:
        print("输入内容为：", user_input)

print("循环结束")


for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 输出：
# 1
# 2

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 输出：
# 1
# 2
# 4
# 5


for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)

# 输出：
# 1
# 2
# 4
# 5
