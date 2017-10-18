import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N, M = input().split()

count = len([i for i in range(int(N), int(M) + 1) if sum([int(j) for j in str(i)]) % 13 == 0])
print(count)