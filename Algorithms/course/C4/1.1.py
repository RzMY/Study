def length(i):
    k = 1
    i //= 2
    while i > 0:
        k += 1
        i //= 2
    return k

def compress(n, p, s, l, b):
    Lmax = 256
    header = 11
    s[0] = 0
    for i in range(1, n+1):
        b[i] = length(p[i])
        bmax = b[i]
        s[i] = s[i-1] + bmax + header
        l[i] = 1
        for j in range(2, min(i, Lmax) + 1):
            if bmax < length(p[i-j+1]):
                bmax = length(p[i-j+1])
            tmp = s[i-j] + j * bmax + header
            if s[i] > tmp:
                s[i] = tmp
                l[i] = j
                b[i] = bmax

def trace_back(n, l, b):
    stack = []
    i = n
    while i > 0:
        stack.append((l[i], b[i]))
        i -= l[i]
    stack.reverse()
    return stack

def out(segments, min_len):
    print("图像的灰度序列为： 10 12 15 255 1 2")
    print("最小长度：", min_len)
    print("共分成：{}段".format(len(segments)))
    for seg in segments:
        print("第一个段含有{}元素.   需要存储位数{}".format(seg[0], seg[1]))

def main():
    p = [0, 10, 12, 15, 255, 1, 2]
    n = len(p) - 1
    s = [0]*(n+1)
    l = [0]*(n+1)
    b = [0]*(n+1)
    compress(n, p, s, l, b)
    segs = trace_back(n, l, b)
    out(segs, s[n])

if __name__ == "__main__":
    main()