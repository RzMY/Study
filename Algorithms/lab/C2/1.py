# 分治法快速排序 + 分治法二分查找 实现查找特定元素下标
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.25 17:10

# 分治法二分查找
def dcSort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        dcSort(arr, left, mid-1)
        dcSort(arr, mid+1, right)
        
def partition(arr, left, right):
    base = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= base:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

# 分治法二分查找
def dcFind(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return dcFind(arr, target, left, mid-1)
    else:
        return dcFind(arr, target, mid+1, right)

def main():
    debug = 1
    arr = []
    if debug:
        target = 95
        arr = [56, 87, 789, 54, 12, 35, 11, 102, 456, 7821, 2, 44, 245, 56, 879, 45, 82, 57, 62, 30]
    else:
        target = int(input("请输入需要查找的数"))
        print("请输入数组")
        for i in range(20):
            arr.append(int(input()))
    dcSort(arr, 0, len(arr)-1)
    print(dcFind(arr, target, 0, len(arr)-1))
    
if __name__ == "__main__":
    main()