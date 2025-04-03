int sum_array(int arr[], int size) {
    int sum = 0;

    for (int i = 0; i < size; i++) {
        sum += arr[i];  // 使用数组索引方式
    }
    
    return sum;
}

int sum_array(int *arr, int size) {
    int sum = 0;
    int *end = arr + size;  // 指向数组末尾的指针

    // 使用指针遍历数组
    for (; arr < end; arr++) {
        sum += *arr;  // 使用指针解引用方式
    }

    return sum;
}