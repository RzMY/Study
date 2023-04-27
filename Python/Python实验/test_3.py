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
'''
n = input()
id = []
for i in range(1000,10000):
    a = str(i)
    if a[0] == a[1] and int(a) % 3 == 0:
        id.append(a)
    else:
        continue
print(id)
'''
'''
n = input()

n = int(n)
num = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
        num.append(n)
    elif n % 2 != 0:
        n = n * 3 + 1
        num.append(n)
print(num)
'''
