N = int(input())
Smax = dp = int(input())
for i in range(1, N):
    cur = int(input())
    dp = max(dp + cur, cur)
    Smax = max(Smax, dp)
print(Smax)