from collections import deque
N = int(input())
K = 6
M = mini = 10 ** 6 + 1
buf = deque()
for i in range(N):
    buf.append(float(input()))
    if i >= K:
        mini = min(mini, buf.popleft())
        M = min(M, mini * buf[-1])
print(M)

