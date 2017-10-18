import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())
lest = [0] + list(map(int, input().split())) + [0]

for i in range(2, len(lest)):
    lest[i] += min(lest[i - 1], lest[i - 2])

print(lest[-1])
