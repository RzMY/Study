# 百鸡问题
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.18 17:10

for x in range(0,100):
    for y in range(0,100):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print("鸡翁：%d只，鸡母：%d只，鸡雏：%d只" % (x, y, z))