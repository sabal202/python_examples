import sys, codecs
import re

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")


def sovp(subs, s):
    c = 0
    for i in range(len(subs)):
        if re.match(subs[:i + 1], s) is not None:
            c += 1

    return c


def genSovpDict(i, s):
    dic1 = []
    c = sovp(ideas[i], s)

    while c != 0 and i < K:
        dic1.append((c, ideas[i]))
        if i < K - 1:
            c = sovp(ideas[i + 1], s)
        i += 1
    return dict(dic1)


N = int(input())
S = input().replace("\r", "").replace("\n", "")
K = int(input())
M = 0
ideas = [input().replace("\r", "").replace("\n", "") for __ in range(K)]
S1 = ""

# TODO сделать так, чтобы он мог возвращаться на значение и игнорировать больше, чем проигнорировал
i = 0
S3 = S
while i < K:
    col = genSovpDict(i, S3)
    if (len(col) != 0):
        M += 1
        X = max(col)
        S1 += col[X][:X]
        S3 = S[len(S1):]

    i += 1
print(K - M)
