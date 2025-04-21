# 动态规划求解0-1背包问题
# 作者: 计算机202205 邱宗森 202203792

def knapsack_dp(values, weights, capacity):
    n = len(values)
    # 创建dp数组
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]
    
    # 填充dp表
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
                
    # 找出选择的物品
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
            
    return dp[n][capacity], selected

def main():
    values = [12, 11, 9, 8]
    weights = [8, 6, 4, 3]
    capacity = 13
    
    dp_value, dp_selected = knapsack_dp(values, weights, capacity)
    print("动态规划解法:")
    print(f"最大价值: {dp_value}")
    print(f"选择的物品索引: {dp_selected}")

if __name__ == "__main__":
    main()