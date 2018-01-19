from collections import deque
import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())

l = []
s = 0
ll = deque(range(N, 0, -1))
bad = False
badbad = False
for k in range(1, N):
    bad = False
    for i in range(0, N):
        c = s
        ll1 = list(ll)
        for j in ll1:
            if s % j == 0:
                l.append(j)
                s += j
                ll1.remove(j)
                break
        if c == s:
            bad = True
            break
        if len(l) == N:
            badbad = True
            break
    if badbad:
        break

if bad:
    print(-1)
else:
    print(" ".join(map(str, l)))
