# 贪心法求活动安排问题
# 作者: 计算机202205 邱宗森 202203792

def activity_selection(s, f):
    n = len(s)
    # 创建活动索引列表
    activities = list(range(n))
    # 按结束时间排序
    activities.sort(key=lambda x: f[x])
    
    # 选择第一个活动
    selected = [activities[0]]
    k = 0
    
    # 遍历剩余活动
    for m in range(1, n):
        if s[activities[m]] >= f[activities[k]]:
            selected.append(activities[m])
            k = m
            
    return selected

def main():
    # 测试数据
    s = [1, 3, 2, 5, 4, 5, 6, 8, 8, 2]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 13]

    result = activity_selection(s, f)
    print("选中的活动序号:", [x + 1 for x in result])
    print("活动总数:", len(result))

if __name__ == "__main__":
    main()