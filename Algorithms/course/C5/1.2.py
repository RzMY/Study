# 贪心算法解决背包问题
# 作者: 计算机202205 邱宗森 202203792

def knapsack_greedy(values, weights, capacity):
    n = len(values)
    # 计算价值密度
    density = [(values[i]/weights[i], i) for i in range(n)]
    density.sort(reverse=True)  # 按价值密度降序排序
    
    total_value = 0
    selected = []
    remaining_capacity = capacity
    
    # 按价值密度选择物品
    for _, i in density:
        if weights[i] <= remaining_capacity:
            selected.append(i)
            total_value += values[i]
            remaining_capacity -= weights[i]
            
    return total_value, selected

def main():
    values = [12, 11, 9, 8]
    weights = [8, 6, 4, 3]
    capacity = 13

    greedy_value, greedy_selected = knapsack_greedy(values, weights, capacity)
    print("贪心算法解法:")
    print(f"最大价值: {greedy_value}")
    print(f"选择的物品索引: {greedy_selected}")

if __name__ == "__main__":
    main()