import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

A, N = list(map(int, input().split()))
B = -1
# TODO decrease time
for b in range(10 ** 9):
    if (b * (A + 1) + A) % N == 0:
        B = b
        break

print(B)
