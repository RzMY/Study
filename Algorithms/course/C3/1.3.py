# 动态规划求解最大子段和

def MaxSubsequenceSum(array):
    maxSum = array[0]
    thisSum = array[0]
    for i in range(1, len(array)):
        thisSum = max(thisSum + array[i], array[i])
        maxSum = max(maxSum, thisSum)
    return maxSum

def main():
    seq = [4, -3, 5, -2, -1, 2, 6, -2]
    # seq = [1, 2, 3, 4]
    # seq = [-1, -2]
    print(MaxSubsequenceSum(seq))
    
if __name__ == '__main__':
    main()