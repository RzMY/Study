'''
n = input()
words = ['hello','good','','','yes','','ok','']


n = int(n)
if n == 0:
    while '' in words:
        words.remove('')
    print(words)
else:
    while n > 0:
        words.remove('')
        n -= 1
    print(words)
    
    
'''
'''
n = input()
a = [42,80,43,62,72,48,12,55,40,65,34,82,82,87,34,60,46,48,41,35]


n = int(n)
b = sorted(a[:n])
c = sorted(a[-n:],reverse=True)
d = a[n:-n]
print(b + d + c)


'''
#判断一个数字能否同时被3、5、7整除
'''
num = input()


num = int(num)
if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
    print('Yes')
else:
    print('No')
    
    
'''
'''
n = input()


id = []
for i in range(1000,10000):
    a = str(i)
    if a[0] == a[1] and int(a[3]) % 2 != 0 and int(a[2]) + int(a[3]) == 5 and int(a) % 3 == 0 :
        id.append(int(a))
    else:
        continue
print(id[:int(n)])


'''
#12345 41235
'''
num = input()


a = str(num[0])
b = str(num[1])
c = str(num[2])
d = str(num[3])
e = str(num[4])
b , e = e , b
a , c = c , a
a , b , c , d = d , a , b , c
print(int(a + b + c + d + e))


'''


num = input()

n = int(num)
num = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
        num.append(n)
    elif n % 2 != 0:
        n = n * 3 + 1
        num.append(n)
print(num)
