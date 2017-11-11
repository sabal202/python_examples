import sys, codecs
import math

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

n, m = list(map(int, input().split()))
l = []
mini = 10 ** 9
marks = []
for i in range(n):
    l.append(list(map(int, input().split())))
    mini = min(min(l[i]), mini)
    marks.append([False for __ in range(m)])


def is_verh(i, j):
    ih = True
    v = l[i][j]
    marks[i][j] = True
    okr = set()
    if j not in [0, m - 1] and i not in [0, n - 1]:
        for k in range(-1, 2):
            c = l[i + k][j - 1]
            if c >= v:
                return 0, 0
            okr.add(c)
            c = l[i + k][j + 1]
            if c >= v:
                return 0, 0
            okr.add(c)
        for k in range(-1, 2):
            c = l[i + 1][j + k]
            if c >= v:
                return 0, 0
            okr.add(c)
            c = l[i - 1][j + k]
            if c >= v:
                return 0, 0
            okr.add(c)
        marks[i][j - 1] = True
        marks[i][j + 1] = True
        marks[i + 1][j] = True
        marks[i - 1][j] = True
        marks[i + 1][j - 1] = True
        marks[i - 1][j - 1] = True
        marks[i + 1][j + 1] = True
        marks[i - 1][j + 1] = True
    elif i == 0 and j not in [0, m - 1]:
        for k in range(-1, 2):
            c = l[i + 1][j + k]
            if c >= v:
                return 0, 0
            okr.add(c)
        c = l[i][j + 1]
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i][j - 1]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i][j - 1] = True
        marks[i + 1][j] = True
        marks[i + 1][j - 1] = True
        marks[i + 1][j + 1] = True
        marks[i][j - 1] = True
    elif i == n - 1 and j not in [0, m - 1]:
        for k in range(-1, 2):
            c = l[i - 1][j + k]
            if c >= v:
                return 0, 0
            okr.add(c)
        c = l[i][j + 1]
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i][j - 1]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i][j - 1] = True
        marks[i][j + 1] = True
        marks[i - 1][j] = True
        marks[i - 1][j + 1] = True
        marks[i - 1][j - 1] = True
    elif j == 0 and i not in [0, n - 1]:
        for k in range(-1, 2):
            c = l[i + k][j + 1]
            if c >= v:
                return 0, 0
            okr.add(c)
        c = l[i + 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i - 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i - 1][j] = True
        marks[i + 1][j] = True
        marks[i][j + 1] = True
        marks[i + 1][j + 1] = True
        marks[i - 1][j + 1] = True
    elif j == m - 1 and i not in [0, n - 1]:
        for k in range(-1, 2):
            c = l[i + k][j - 1]
            if c >= v:
                return 0, 0
            okr.add(c)
        c = l[i + 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i - 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i][j - 1] = True
        marks[i + 1][j - 1] = True
        marks[i - 1][j - 1] = True
        marks[i - 1][j] = True
        marks[i + 1][j] = True
    elif j == m - 1 and i == n - 1:
        c = l[i - 1][j - 1]
        if c >= v:
            return 0, 0
        c = l[i][j - 1]
        okr.add(c)
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i - 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i][j - 1] = True
        marks[i - 1][j - 1] = True
        marks[i - 1][j] = True
    elif j == 0 and i == 0:
        c = l[i + 1][j + 1]
        if c >= v:
            return 0, 0
        c = l[i][j + 1]
        okr.add(c)
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i + 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i + 1][j] = True
        marks[i][j + 1] = True
        marks[i + 1][j + 1] = True
    elif j == 0 and i == n - 1:
        c = l[i - 1][j + 1]
        if c >= v:
            return 0, 0
        c = l[i][j + 1]
        okr.add(c)
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i - 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i][j + 1] = True
        marks[i - 1][j + 1] = True
        marks[i - 1][j] = True
    elif j == m - 1 and i == 0:
        c = l[i + 1][j - 1]
        if c >= v:
            return 0, 0
        c = l[i][j - 1]
        okr.add(c)
        if c >= v:
            return 0, 0
        okr.add(c)
        c = l[i + 1][j]
        if c >= v:
            return 0, 0
        okr.add(c)
        marks[i + 1][j] = True
        marks[i][j - 1] = True
        marks[i + 1][j - 1] = True

    return ih, int(math.fabs(mini - v))


for i in range(n):
    for j in range(m):
        if not marks[i][j]:
            verh, height = is_verh(i, j)
            if verh:
                print(i + 1, j + 1, height)
