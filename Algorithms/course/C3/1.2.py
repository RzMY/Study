# 穷举法求解最大子段和

import sys
def MaxSubsequenceSum(array) :
    maxSum = -(sys.maxsize)
    for i in range(1, len(array) + 1):
        left = 0
        right = i
        while(right <= len(array)):
            tempSum = 0
            for j in range(left, right):
                tempSum += array[j]
            if tempSum > maxSum:
                maxSum = tempSum
            left += 1
            right += 1
    return max(maxSum, sum(array))
            
def main():
    # seq = [4, -3, 5, -2, -1, 2, 6, -2]
    # seq = [1, 2, 3, 4]
    seq = [-1, -2]
    print(MaxSubsequenceSum(seq))
    
if __name__ == '__main__':
    main()