# 动态规划求硬币付款最轻重量
# 作者: 计算机202205 邱宗森 202203792

import prettytable as pt

def getMinWeightPay(coin, weight, amount):
    n = len(coin)  # 硬币种类数
    
    # 初始化dp表,dp[i][j]表示使用前i种硬币凑出金额j的最小重量
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # 记录选择,用于回溯
    choice = [[0] * (amount + 1) for _ in range(n + 1)]
    
    # 填充dp表
    for i in range(1, n + 1):
        for j in range(amount + 1):
            if j >= coin[i-1]:
                if dp[i][j-coin[i-1]] + weight[i-1] < dp[i-1][j]:
                    dp[i][j] = dp[i][j-coin[i-1]] + weight[i-1]
                    choice[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    # 回溯找出解
    result = []
    i, j = n, amount
    while i > 0:
        if choice[i][j] == 1:
            result.append(i-1)
            j -= coin[i-1]
        else:
            i -= 1
            
    return dp[n][amount], result, dp, choice

# 测试代码
if __name__ == "__main__":
    coin = [1, 4, 6, 8]  # 硬币面值
    weight = [1, 2, 4, 6]  # 对应重量
    amount = 12  # 付款金额
    min_weight, solution, dp, choice = getMinWeightPay(coin, weight, amount)
    print(f"最小重量: {min_weight}")
    print(f"使用硬币索引: {solution}")
    print("dp表:")
    tb = pt.PrettyTable()
    tb.field_names = [f"j={i}" for i in range(amount + 1)]
    for i in range(len(dp)):
        tb.add_row(dp[i])
    print(tb)
    print("选择表:")
    tb = pt.PrettyTable()
    tb.field_names = [f"j={i}" for i in range(amount + 1)]
    for i in range(len(choice)):
        tb.add_row(choice[i])
    print(tb)