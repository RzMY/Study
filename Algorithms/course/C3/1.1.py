# 分治法求解最大子段和

def MaxSubsequenceSum(array, left, right):
    if left == right:
        return array[left]
    
    # 计算中间索引
    middle = (left + right) // 2
    
    # 递归求解左半部分的最大子段和
    leftMaxSubsequenceSum = MaxSubsequenceSum(array, left, middle)
    # 递归求解右半部分的最大子段和
    rightMaxSubsequenceSum = MaxSubsequenceSum(array, middle + 1, right)
    
    import sys
    # 初始化跨越中间点的左边最大和
    maxLeftBorderSum = -sys.maxsize - 1
    # 初始化跨越中间点的右边最大和
    maxRightBorderSum = -sys.maxsize - 1
    tempSum = 0
    
    # 向左遍历，找到左边的最大子段和
    for i in range(middle, left - 1, -1):
        tempSum += array[i]
        if tempSum > maxLeftBorderSum:
            maxLeftBorderSum = tempSum
    
    tempSum = 0
    # 向右遍历，找到右边的最大子段和
    for i in range(middle + 1, right + 1):
        tempSum += array[i]
        if tempSum > maxRightBorderSum:
            maxRightBorderSum = tempSum
                
    # 返回左半部分、右半部分及跨中间点的最大子段和中的最大值
    return max(leftMaxSubsequenceSum, rightMaxSubsequenceSum, maxLeftBorderSum + maxRightBorderSum)

def main():
    # 测试序列
    # seq = [4, -3, 5, -2, -1, 2, 6, -2]
    seq = [1, 2, 3, 4]
    # seq = [-1, -2]
    print(MaxSubsequenceSum(seq, 0, len(seq) - 1))
        
if __name__ == '__main__':
    main()