# 穷举法求解最大子段和

import sys

def MaxSubsequenceSum(array):
    # 初始化最大和为最小可能值
    maxSum = -(sys.maxsize)
    # 遍历所有可能的子数组长度
    for i in range(1, len(array) + 1):
        left = 0
        right = i
        # 滑动窗口遍历所有长度为i的子数组
        while(right <= len(array)):
            tempSum = 0
            # 计算当前子数组的和
            for j in range(left, right):
                tempSum += array[j]
            # 更新最大和
            if tempSum > maxSum:
                maxSum = tempSum
            # 移动窗口位置
            left += 1
            right += 1
    # 返回最大子数组和与数组总和中的较大值
    return max(maxSum, sum(array))
                
def main():
    # 示例序列，可以修改以测试不同情况
    # seq = [4, -3, 5, -2, -1, 2, 6, -2]
    # seq = [1, 2, 3, 4]
    seq = [-1, -2]
    # 计算并打印最大子段和
    print(MaxSubsequenceSum(seq))
        
if __name__ == '__main__':
    main()