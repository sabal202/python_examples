import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())
colonna = input()
result = 0

while True:
    is_continues = True
    for i in range(N - 1):
        if colonna[i] + colonna[i + 1] == '><':
            is_continues = False
            result += 1
            colonna = colonna[:i] + '<>' + colonna[i + 2:]

    if is_continues:
        break

print(result)