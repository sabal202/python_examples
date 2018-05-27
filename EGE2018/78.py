N = int(input())
K = 3
buf = []
n1, n2, n3, n6 = 0, 0, 0, 0
s = 0

for i in range(N):
    buf.append(int(input()))
    if i >= K:
        n = buf.pop(0)
        if n % 6 == 0:
            n6 += 1
        elif n % 3 == 0:
            n3 += 1
        elif n % 2 == 0:
            n2 += 1
        else:
            n1 += 1
        if buf[-1] % 6 == 0:
            s += n1 + n2 + n3 + n6
        elif buf[-1] % 3 == 0:
            s += n2 + n6
        elif buf[-1] % 2 == 0:
            s += n3 + n6
        else:
            s += n6
print(s)
