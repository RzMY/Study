def max_profit(n, D, L, V):
    # 初始化二维数组存储收益信息
    dp = [[0] * (D + 1) for _ in range(n + 1)]
    
    # 遍历每一个货柜
    for i in range(1, n + 1):
        # 遍历每一个库房长度
        for j in range(1, D + 1):
            if j < L[i - 1]:
                # 如果当前货柜长度大于库房长度，则无法放入
                dp[i][j] = dp[i - 1][j]
            else:
                # 否则，当前货柜可以放入，取放入和不放入的最大值
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i - 1]] + V[i - 1])
    
    return dp[n][D]

n = 4  # 货柜数量
D = 10  # 库房总长度
L = [2, 3, 4, 7]  # 每个货柜的长度
V = [1, 3, 6, 9]  # 每个货柜的收益

# 计算最大收益
result = max_profit(n, D, L, V)
print("最大收益为：", result)


def knapsack_multi_constraint(n, W, V, weights, volumes, values):
    # 初始化三维DP数组，填充为0
    dp = [[[0] * (V + 1) for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = volumes[i - 1]
        val = values[i - 1]
        for w in range(W + 1):
            for v in range(V + 1):
                if w >= wi and v >= vi:
                    dp[i][w][v] = \
                    max(dp[i - 1][w][v], dp[i - 1][w - wi][v - vi] + val)
                else:
                    dp[i][w][v] = dp[i - 1][w][v]
    return dp[n][W][V]

# 示例参数
n = 4  # 物品数量
W = 10  # 重量限制
V = 12  # 体积限制
weights = [2, 3, 4, 5]    # 物品重量
volumes = [3, 4, 5, 6]    # 物品体积
values = [3, 4, 5, 6]     # 物品价值

# 计算最大价值
max_value = knapsack_multi_constraint(n, W, V, weights, volumes, values)
print("最大价值为：", max_value)