N = int(input())
S = 0
minR = 10001


def ra(a, b):
    return a - b if (a - b) % 4 != 0 else 10001


for i in range(N):
    a, b, c = map(int, input().split())
    if a >= b and a >= c:
        maxi = a
        minR = min(minR, ra(a, c), ra(a, b))
    elif b >= c and b >= a:
        maxi = b
        minR = min(minR, ra(b, c), ra(b, a))
    elif c >= a and c >= b:
        maxi = c
        minR = min(minR, ra(c, a), ra(c, b))
    S += maxi
if S % 4:
    print(S)
elif minR == 10001:
    print(0)
else:
    print(S - minR)
"""
6
4 4 4
4 4 4
4 4 4
4 4 4
4 4 4
4 4 4

"""