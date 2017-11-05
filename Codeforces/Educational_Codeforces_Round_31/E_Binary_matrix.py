# import sys, codecs
#
# save_stdin = sys.stdin
# save_stdout = sys.stdout
# sys.stdin = codecs.open("input.txt", "r", "utf-8")
# sys.stdout = codecs.open("output.txt", "w+")

# TODO: solve
n, m = list(map(int, input().split()))

s = []
sn = ""
for i in range(n):
    x = bin(int(input(), 16))[2:].zfill(m)
    sn += x + "\n"
    s.append([int(x[i]) for i in range(len(x))])


def find(i, j):
    if s[i][j]:
        s[i][j] = 0
        if i < n - 1:
            find(i + 1, j)
        if i > 0:
            find(i - 1, j)
        if j < m - 1:
            find(i, j + 1)
        if j > 0:
            find(i, j - 1)
        return True
    else:
        return False


count = 0
for i in range(n):
    for j in range(m):
        if find(i, j):
            count += 1
print(count)
