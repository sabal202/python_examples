from collections import deque
N = int(input())
K = 9
M = maxi = maxi2 = -1
buf = deque()
for i in range(N):
    buf.append(int(input()))
    if i >= K:
        if buf[0] % 2 == 1:
            maxi = max(maxi, buf.popleft())
        else:
            maxi2 = max(maxi2, buf.popleft())
        if buf[-1] % 2 == 1:
            M = max(M, maxi2 * buf[-1])
        else:
            M = max(M, maxi * buf[-1], maxi2 * buf[-1])
print(M)