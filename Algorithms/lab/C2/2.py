"""
问题描述：
设 A = {a1, a2, ..., an} 是一个有 n 个元素的集合, B = {b1, b2, ..., bm} 是一个有 m 个元素的集合。
其中 m = O(logn). 设计算 C = (A - B) ∪ (B - A) 的算法并分析复杂度。
"""
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.25 17:10

def Ca(A, B):
    # 利用字典模拟hash表分别存储A和B
    A_hash = {}
    B_hash = {}
    for a in A:
        A_hash[a] = 1
    for b in B:
        B_hash[b] = 1
    C = set()
    # 计算 A - B
    for a in A:
        if a not in B_hash:
            C.add(a)
    # 计算 B - A
    for b in B:
        if b not in A_hash:
            C.add(b)
    return C

def main():
    A = set(map(int, input("请输入集合A: ").split()))
    B = set(map(int, input("请输入集合B: ").split()))
    print(Ca(A, B))
    
if __name__ == "__main__":
    main()