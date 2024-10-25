# 分治法快速排序 + 分治法二分查找 实现查找特定元素下标
# 作者: 计算机202205 邱宗森 202203792
# 日期: 2024.10.25 17:10

def dcSort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        dcSort(arr, left, mid-1)
        dcSort(arr, mid+1, right)
        
def partition(arr, left, right):
    base = arr[right]
    print("base", base)
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= base:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[right] = arr[right], arr[i+1]
    print("mid", i+1)
    return i + 1

arr = [3, 6, 8, 10, 1, 2, 1]
dcSort(arr, 0, len(arr) - 1)
print(arr)