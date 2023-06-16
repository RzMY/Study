n = input()
a = [42,80,43,62,72,48,12,55,40,65,34,82,82,87,34,60,46,48,41,35]


n = int(n)
b = sorted(a[:n])
c = sorted(a[-n:],reverse=True)
d = a[n:-n]
print(b + d + c)
