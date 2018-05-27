"""
10
1
2
3
4
5
6
7
8
9
10
"""
from collections import deque
N = int(input())
K = 7
que = deque()
S = maxi = 0
for i in range(N):
    que.append(int(input()))
    if i > K:
        maxi = max(maxi, que.popleft())
        S = max(S, que[-1] + maxi)
print(S)
