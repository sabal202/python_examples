"""
3
20
320 150
200 440
300 210
"""
N = int(input())
t = int(input())
TA, TB = 0, t
for i in range(N):
    a, b = [int(k) for k in input().split()]
    TA = TA + a
    TB = min(TA + t, TB + b)
print(TB)