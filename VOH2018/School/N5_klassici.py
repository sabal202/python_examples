import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")


def col(a):
    c = 1
    count = 1
    if a < 1:
        return -2

    while count < a:
        a -= count
        count += 2
        c += 1
    return c


def neibors(N):
    neibor = []
    if (col(N) - col(N - col(N) * 2 + 2) == 1):
        neibor.append(N - col(N) * 2 + 2)

    if (col(N) - col(N - 1) == 0):
        neibor.append(N - 1)

    if (col(N) - col(N + 1) == 0):
        neibor.append(N + 1)

    if (col(N) - col(N + col(N) * 2) == -1):
        neibor.append(N + col(N) * 2)

    return neibor


N = int(input())
print(" ".join(map(str, neibors(N))))