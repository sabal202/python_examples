N = int(input())
Smax = 0
dp = int(input())
for i in range(1, N):
    cur = int(input())
    dp = min(cur, dp)
    Smax = max(Smax, cur - dp)
print(Smax)