"""
11
12
45
5
4
25
23
21
20
10
12
26

"""
from collections import deque
N = int(input())
K = 5
que = deque()
Smin = mini = 2 * 1000 ** 2
for i in range(N):
    que.append(int(input()))
    if i > K:
        mini = min(mini, que.popleft())
        Smin = min(Smin, que[-1] ** 2 + mini ** 2)
print(Smin)
