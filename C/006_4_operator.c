//位运算符

#include <stdio.h>

int main()
{
    int a = 60; // 60 = 0011 1100
    int b = 13; // 13 = 0000 1101
    int c;

    c = a & b; // 按位与运算符，如果两个相应的二进制位都为1，则该位的结果值为1，否则为0
    //12 = 0000 1100
    printf("Line 1 - c 的值是 %d\n", c);

    c = a | b; // 按位或运算符，只要对应的二个二进制位有一个为1时，结果位就为1
    //61 = 0011 1101
    printf("Line 2 - c 的值是 %d\n", c);

    c = a ^ b; // 按位异或运算符，当两对应的二进制位相异时，结果为1
    //49 = 0011 0001
    printf("Line 3 - c 的值是 %d\n", c);

    c = ~a; // 按位取反运算符，对数据的每个二进制位取反，即把1变为0，把0变为1
    //-61 = 1100 0011
    printf("Line 4 - c 的值是 %d\n", c);

    c = a << 2; // 左移运算符，运算数的各二进制位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
    //240 = 1111 0000
}