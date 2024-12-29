# 动态规划求解最大子段和

def MaxSubsequenceSum(array):
    # 初始化最大和为数组的第一个元素
    maxSum = array[0]
    # 当前子段的和初始化为第一个元素
    thisSum = array[0]
    # 从第二个元素开始遍历数组
    for i in range(1, len(array)):
        # 选择将当前元素加入现有子段或重新开始一个新子段
        thisSum = max(thisSum + array[i], array[i])
        # 更新最大子段和
        maxSum = max(maxSum, thisSum)
    # 返回最大子段和
    return maxSum

def main():
    # 测试序列
    seq = [4, -3, 5, -2, -1, 2, 6, -2]
    # seq = [1, 2, 3, 4]
    # seq = [-1, -2]
    # 计算并打印最大子段和
    print(MaxSubsequenceSum(seq))
        
if __name__ == '__main__':
    main()