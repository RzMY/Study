#这样会导致死循环
x = 1
while True:
    print(x)
    x += 1