import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N = int(input())
list_input = list(map(int, input().split()))
list_sorted = list_input.copy()
list_sorted.sort()

l = -1
r = -1

for i in range(N):
    if list_sorted[i] != list_input[i]:
        l = i + 1
        print(l, end=" ")
        break

for i in range(1, N + 1):
    if list_sorted[-i] != list_input[-i]:
        r = N - i + 1
        print(r)
        break
        # else:
        #     r = i + 1
        #     print(r)
        #     break
