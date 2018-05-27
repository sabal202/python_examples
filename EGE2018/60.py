from collections import deque
N = int(input())
K = 6
M = mini = 10 ** 6 + 1
buf = deque()
for i in range(N):
    buf.append(int(input()))
    if i >= K:
        if buf[0] % 2 == 1:
            mini = min(mini, buf.popleft())
        else:
            buf.popleft()
        if buf[-1] % 2 == 1:
            M = min(M, mini * buf[-1])
if M == 10 ** 6 + 1:
    print(-1)
else:
    print(M)