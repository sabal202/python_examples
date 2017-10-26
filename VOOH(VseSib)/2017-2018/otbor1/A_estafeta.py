import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N, I = list(map(int, input().split()))
# TODO decrease time
times = []
for __ in range(N):
    times.append(list(map(int, input().split())))
#
# times2 = [[0 for __ in range(N)] for __ in range(3)]
# times3 = [[0 for __ in range(N)] for __ in range(3)]
# for j in range(3):
#     for i in range(N):
#         times3[j][i] = times[i][j]
#         times2[j][i] = {times[i][j]: i}
#     times3[j].sort()

shtafs = [0 for __ in range(N)]
for i in range(3):
    for j in range(N):
        for k in range(N):
            if times[j][i] > times[k][i]:
                shtafs[j] += 1
    if i < 2:
        for j in range(N):
            times[j][i + 1] += times[j][i]

x = shtafs[I - 1]

shtafs.sort()
print(shtafs.index(x) + 1)
