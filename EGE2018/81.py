N = int(input())
K = 5
buf = []
n1, n2, n13, n26 = 0, 0, 0, 0
s = 0

for i in range(N):
    buf.append(int(input()))
    if i >= K:
        n = buf.pop(0)
        if n % 26 == 0:
            n26 += 1
        elif n % 13 == 0:
            n13 += 1
        elif n % 2 == 0:
            n2 += 1
        else:
            n1 += 1
        if buf[-1] % 26 == 0:
            s += n13 + n1
        elif buf[-1] % 13 == 0:
            s += n26 + n2
        elif buf[-1] % 2 == 0:
            s += n13
        else:
            s += n26
print(s)
