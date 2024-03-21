// /**
//  * Note: The returned array must be malloced, assume caller calls free().
//  */
// int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
//     int i = 0;
//     int j = numbersSize - 1;
//     int a[2];
//     while(i != j){
//         if(numbers[i] + numbers[j] > target){
//             j--;
//         }else if(numbers[i] + numbers[j] < target){
//             i++;
//         }else{
//             a[0] = i+1;
//             a[1] = j+1;
//             return(a);
//         }
//     }
// }
#include <stdio.h>

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int i = 0;
    int res;
    int count = 0;
    while(i < numsSize){
        if(nums[i] == 1){
            count++;
            i++;
        }else{
            if(count != 0){
                if(res < count){
                    res = count;
                }
                count = 0;
            }
            i++;
        }
    }
    if(res < count){
        res = count;
    }
    return(res);
}

int main(){
    int a[1] = {1};
    int res = findMaxConsecutiveOnes(a, 1);
    printf("%d", res);
    return 0;
}

