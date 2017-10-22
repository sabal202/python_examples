import sys, codecs
from math import fabs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())
if (N < 0):
    print(int(fabs(N) + 2) * (1 + N) // 2)
else:
    print(N * (1 + N) // 2)
