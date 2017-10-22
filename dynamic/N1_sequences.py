import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())


def fib(n):
    sqrt5 = 5 ** 0.5
    phi = (sqrt5 + 1) / 2
    return int(phi ** n / sqrt5 + 0.5)


print(fib(N + 2))
