#输入任意一个字符，输出其ASCII码
a = input()
print(ord(a))
#输入任意一个ASCII码，输出其字符
a = input()
print(chr(int(a)))
#输入一个正整数，输出字母表前n个字母
a = int(input())
for i in range(97,97+a):
    print(chr(i),end="")
#输入一个正整数n，从小到大输出n的所有因子
c = int(input())
for i in range(1,c+1):
    if c % i == 0:
        print(i,end=" ")
#给定一个正整数n，从大到小输出n的所有因子
num = int(input())
for i in range(num,0,-1):
    if num % i == 0:
        print(i,end=" ")
#给出一个正整数n，求斐波那契数列的第n项
num = int(input())
for i in range(1,num+1):
    if i == 1:
        a = 1
        b = 1
    else:
        a,b = b,a+b
print(a)
#输入一个正整数n，求n的阶乘
c = int(input())
for i in range(1,c+1):
    if i == 1:
        a = 1
    else:
        a *= i
print(a)