# import sys, codecs
#
# save_stdin = sys.stdin
# save_stdout = sys.stdout
# sys.stdin = codecs.open("input.txt", "r", "utf-8")
# sys.stdout = codecs.open("output.txt", "w+")

n, t = list(map(int, input().split()))
times = list(map(int, input().split()))

for i in range(n):
    t -= 86400 - times[i]
    if t <= 0:
        print(i + 1)
        break
