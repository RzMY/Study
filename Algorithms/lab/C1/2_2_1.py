# 递归求斐波那契数列
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.18 17:10

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def main():
    print("请输入斐波那契数列的项数：")
    n = int(input())
    print("第", n, "项的值为：", fib(n))
    
if __name__ == "__main__":
    main()