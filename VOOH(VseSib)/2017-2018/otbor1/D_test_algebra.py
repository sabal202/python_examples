import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

A, N = list(map(int, input().split()))
B = -1

X = False
for x in range(1, 10 ** 6):
    if (A + 1) % (N * x + 1) == 0:
        B = (x * N + 1) / (A + 1) - 1
        break

print(B)
