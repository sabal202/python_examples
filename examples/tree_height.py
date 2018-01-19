import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

n = int(input())
parents = list(map(int, input().split()))

hs = [0] * n
flags = [False] * n


def height(r, h):
    if r == -1:
        hs = 1
        return h
    else:
        if hs[r] != 0:
            hs[r] = height(parents[r]) + h
        else:
            return hs[r]


for i in range(n):
    if hs[i] != 0:
        continue
    else:
        if parents[i] == -1:
            hs[i] = 1
        else:
            if not flags[i]:
                pass
print(max(hs))
