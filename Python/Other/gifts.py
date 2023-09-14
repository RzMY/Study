n, k = map(int, input().split())
v = list(map(int, input().split()))

# dp[i][j] 表示前 i 个礼物，最多交换 j 次，能够获得的最大价值
dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # 不交换第 i 个礼物
        dp[j][i] = dp[j][i-1]
        # 交换第 i 个礼物
        for l in range(i):
            if v[i-1] <= v[l]+k:
                dp[j][i] = max(dp[j][i], dp[j-1][l] + v[i-1])

# 找到最大价值和最少星期数
max_value = 0
min_weeks = 0
for j in range(k+1):
    for i in range(n+1):
        if dp[j][i] > max_value:
            max_value = dp[j][i]
            min_weeks = j

print(max_value, min_weeks)