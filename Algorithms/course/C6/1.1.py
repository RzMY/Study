# 回溯法求0-1背包问题
# 作者: 计算机202205 邱宗森 202203792

def backtrack(i, cw, cv, w, v, n, C):
    global bestv  # 全局最优值
    global x      # 最优解向量
    global bestx  # 当前最优解

    if i >= n:  # 到达叶节点
        if bestv < cv and cw <= C:
            bestv = cv
            bestx = x[:]
        return
    
    # 不放入第i个物品
    x[i] = 0
    if cw <= C:  # 满足约束条件才继续
        backtrack(i+1, cw, cv, w, v, n, C)
    
    # 放入第i个物品
    x[i] = 1
    if cw + w[i] <= C:  # 满足约束条件才继续
        backtrack(i+1, cw+w[i], cv+v[i], w, v, n, C)
    x[i] = 0  # 回溯

def knapsack(w, v, n, C):
    global bestv, x, bestx
    bestv = 0            # 初始化最优值
    x = [0] * n         # 当前解向量
    bestx = [0] * n     # 最优解向量
    
    backtrack(0, 0, 0, w, v, n, C)
    return bestv, bestx

def main():
    n = 10
    C = 50
    w = [12, 3, 11, 5, 6, 8, 9, 4, 7, 10]
    v = [6, 2, 7, 3, 2, 9, 8, 10, 4, 5]
    maxValue, solution = knapsack(w, v, n, C)
    
    print(f"最大价值: {maxValue}")
    print("选择物品: ", end="")
    for i in range(n):
        if solution[i] == 1:
            print(f"{i+1} ", end="")

if __name__ == "__main__":
    main()