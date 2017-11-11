import codecs
import sys

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

n, t = [int(s) for s in input().split()]
arrA, arrB = [], []

for i in range(n):
    a, b = [int(s) for s in input().split()]
    arrA.append(a)
    arrB.append(b)

totalA = 0
totalB = sum(arrB) + t

mini = -1

for i in range(0, n):
    if mini < 0 or totalA + totalB < mini:
        mini = totalA + totalB

    totalA += arrA[i]
    totalB -= arrB[i]
    b = 1

print(mini)
