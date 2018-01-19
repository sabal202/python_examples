from collections import deque
import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")


def print_f(F):
    for i in F:
        print(" ".join(list(map(str, i))))


N, M = map(int, input().split())
INF = -11
f = [[-1 for j in range(M + 2)] for i in range(N + 2)]
for i in range(N + 2):
    f[i][0] = INF
    f[i][M + 1] = INF
for i in range(M + 2):
    f[0][i] = INF
    f[N + 1][i] = INF

K = int(input())

rs = deque()
cs = deque()

for i in range(K):
    r, c = map(int, input().split())
    rs.append(r)
    cs.append(c)
    f[r][c] = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while rs:
    r = rs.popleft()
    c = cs.popleft()
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if f[nr][nc] == -1:
            f[nr][nc] = f[r][c] + 1
            rs.append(nr)
            cs.append(nc)

print_f(f)
left = 0
right = N + M

while left < right:
    used = set()
    med = (left + right + 1) // 2
    good = False
    for i in range(1, N + 1):
        rs.append(i)
        cs.append(1)
        used.add((i, 1))

    while rs:
        r = rs.popleft()
        c = cs.popleft()
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if f[nr][nc] >= med and (nr, nc) not in used:
                used.add((nr, nc))
                rs.append(nr)
                cs.append(nc)
                if nc == M:
                    good = True
    if not good:
        right = med - 1
    else:
        left = med
    print(left, right, med)
print(left)
