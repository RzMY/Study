# 非递归求两数的最大公约数
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.18 17:10

def measure(a, b):
    while (a % b != 0):
        a, b = b, a % b
    return b

def main():
    print("请输入两个数：")
    a = int(input())
    b = int(input())
    print("最大公约数为：", measure(a, b))
    
if __name__ == "__main__":
    main()