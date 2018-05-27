N = int(input())
n1, n2, n13, n26 = 0, 0, 0, 0
s = 0
pairs14 = [0] * 14
rem14 = [0] * 14
for i in range(N):
    x = int(input())
    s += pairs14[(21 - (x % 14)) % 14]
    for j in range(14):
        pairs14[(j + x) % 14] += rem14[j]
    rem14[x % 14] += 1
print(s)
