# 递归求汉诺塔问题
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.18 17:10
# 描述: 该程序通过递归算法解决汉诺塔问题，并输出每一步的移动过程以及总的移动次数。

def hanoi(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
        return 1
    else:
        count = hanoi(n-1, a, c, b)
        print(a, "-->", c)
        count += 1
        count += hanoi(n-1, b, a, c)
        return count

def main():
    print("汉诺塔问题，请输入盘子的个数：")
    n = int(input())
    print(f"开始搬${n}个盘子：")
    count = hanoi(n, "A", "B", "C")
    print("移动次数：", count)
    
if __name__ == "__main__":
    main()