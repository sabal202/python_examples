import re

import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

n = int(input())
num = re.compile("[-0-9]+")
s = dict()


def cross(A, B):  # A < B
    if A[0] == "?":
        A[0] = -1 * 10 ** 9 - 1
    if A[1] == "?":
        A[1] = 10 ** 9 + 1
    if B[0] == "?":
        B[0] = -1 * 10 ** 9 - 1
    if B[1] == "?":
        B[1] = 10 ** 9 + 1
    a, b = set(), set()
    for i in range(A[0] + 1, A[1]):
        a.add(i)
    for i in range(B[0] + 1, B[1]):
        b.add(i)
    c = a.difference(b)
    print(c)
    C = [min(), 0]
    al, bl, cl = len(A)


for i in range(n):
    line = input().rstrip().replace("<", " ").split()
    if len(line) == 0:
        break
    elif line[0] == "new":
        s[line[1]] = ["?", "?"]
    elif line[0] == "state":
        a, b = line[1:]
        a_i, b_i = re.search(num, a), re.search(num, b)
        if a_i is None and b_i is None:
            pass
        elif a_i is None and not b_i is None:
            s[a][1] = int(b)
        elif not a_i is None and b_i is None:
            s[b][0] = int(a)
        elif not a_i is None and not b_i is None:
            pass
    elif line[0] == "ask":
        a, b = line[1:]
        a_i, b_i = re.search(num, a), re.search(num, b)
        if a_i is None and b_i is None:  # a < b
            cross(s[a], s[b])
        elif a_i is None and b_i is not None:  # a < 1
            cross(s[a], ["?", int(b)])
        elif a_i is not None and b_i is None:  # 1 < b
            cross([int(a), "?"], s[b])
        elif a_i is not None and b_i is not None:  # 1 < 2
            a = int(a)
            b = int(b)
            if a < b:
                print("sure")
            else:
                print("impossible")
