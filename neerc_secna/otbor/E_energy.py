import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")
import timeit

start_time = timeit.default_timer()

n, m = list(map(int, input().split()))
l = []

for i in range(n):
    l.append(tuple(map(int, input().split())))

l.sort(key=lambda x: x[0])
p = [0 for __ in range(m)]
for i in l:
    for j in range(i[1], i[2]):
        p[j] = min(p[j], i[0]) if p[j] != 0 else i[0]
    if all(p):
        break
print(sum(p))

# your code
print(timeit.default_timer() - start_time)
