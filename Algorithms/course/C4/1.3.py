# 动态规划求投资问题
# 作者: 计算机202205 邱宗森 202203792

def investment_dp(total_money, n, profits):

    dp = [[0] * (total_money + 1) for _ in range(n + 1)]
    decisions = [[0] * (total_money + 1) for _ in range(n + 1)]
    
    # 动态规划过程
    for i in range(1, n + 1):  # 遍历每个项目
        for j in range(total_money + 1):  # 遍历每个资金量
            max_profit = 0
            best_invest = 0
            
            # 尝试不同投资金额
            for k in range(min(j + 1, 6)):  # 最多投资5万
                current_profit = dp[i-1][j-k] + profits[k][i-1]
                if current_profit > max_profit:
                    max_profit = current_profit
                    best_invest = k
                    
            dp[i][j] = max_profit
            decisions[i][j] = best_invest
    
    # 获取最优解决方案
    result = []
    remaining = total_money
    for i in range(n, 0, -1):
        invest = decisions[i][remaining]
        result.insert(0, invest)
        remaining -= invest
    
    return dp[n][total_money], result

def main():
    profits = [
        [0, 0, 0, 0],
        [11, 0, 2, 20],
        [12, 5, 10, 21],
        [13, 10, 30, 22],
        [14, 15, 32, 23],
        [15, 20, 40, 24]
    ]
    
    total_money = 5
    projects = 4
    
    max_profit, investments = investment_dp(total_money, projects, profits)
    print(f"最大收益: {max_profit}")
    print(f"投资方案: {investments}")

if __name__ == "__main__":
    main()