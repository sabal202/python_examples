N = int(input())
Smax = mi = ma = int(input())
for i in range(1, N):
    cur = int(input())
    t = min(mi * cur, cur * ma, cur)
    ma = max(ma * cur, cur * mi, cur)
    mi = t
    Smax = max(Smax, ma)
print(Smax)