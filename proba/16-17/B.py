import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

n = int(input())
h = list(map(int, input().split()))
maxv = h[0]
mp1 = 0
mp2 = 0
for i in range(n):
    if h[i] == maxv:
        mp2 = i
    if h[i] > maxv:
        mp1 = i
        mp2 = i
        maxv = h[i]
    none = 1
ans = 0
nowm = 0
for i in range(mp1):
    if h[i] > nowm:
        nowm = h[i]
    ans += nowm - h[i]
for i in range(mp1, mp2):
    ans += maxv - h[i]
nowm = 0
for i in range(n - 1, mp2, -1):
    if h[i] > nowm:
        nowm = h[i]
    ans += nowm - h[i]
print(ans)
