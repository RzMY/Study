# 递归求最大公约数
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.18 17:10

def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)
    
def main():
    print("请输入两个数：")
    a = int(input())
    b = int(input())
    print("最大公约数为：", gcd(a, b))
    
if __name__ == "__main__":
    main()