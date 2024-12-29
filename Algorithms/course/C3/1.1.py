# 分治法求解最大子段和

def MaxSubsequenceSum(array, left, right) :
    if left == right :
        return array[left]
    
    middle = (left + right) // 2
    
    leftMaxSubsequenceSum = MaxSubsequenceSum(array, left, middle)
    rightMaxSubsequenceSum = MaxSubsequenceSum(array, middle + 1, right)
    
    import sys
    maxLeftBorderSum = -sys.maxsize - 1
    maxRightBorderSum = -sys.maxsize - 1
    tempSum = 0
    
    for i in range(middle, left - 1, -1):
        tempSum += array[i]
        if (tempSum > maxLeftBorderSum):
            maxLeftBorderSum = tempSum
    
    tempSum = 0
    for i in range(middle + 1, right + 1):
        tempSum += array[i]
        if (tempSum > maxRightBorderSum):
            maxRightBorderSum = tempSum
            
    return max(leftMaxSubsequenceSum, rightMaxSubsequenceSum, maxLeftBorderSum + maxRightBorderSum)

def main():
    # seq = [4, -3, 5, -2, -1, 2, 6, -2]
    seq = [1, 2, 3, 4]
    # seq = [-1, -2]
    print(MaxSubsequenceSum(seq, 0, len(seq) - 1))
    
if __name__ == '__main__':
    main()