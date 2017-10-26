n, kmax = list(map(int, input().split()))

lis = list(map(int, input().split()))
points = dict([(lis[i], i) for i in range(n)])
lenth = lis[-1] - lis[0]
ks = []
# TODO solve
for k in range(1, 10001):
    j = lis[0]

    while j in points:
        j += k

    if j - k in points:
        if lenth // k <= kmax and points[j - k] == n - 1:
            ks.append(k)

print(ks)
