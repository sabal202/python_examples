from collections import deque
import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())

l = [N]
s = N
ll = deque(reversed(range(1, N)))
bad = False
for i in range(1, N):
    c = s
    for j in ll:
        if s % j == 0:
            l.append(j)
            s += j
            ll.remove(j)
            break
    if c == s:
        bad = True
        break

if bad:
    print(-1)
else:
    print(" ".join(map(str, l)))
