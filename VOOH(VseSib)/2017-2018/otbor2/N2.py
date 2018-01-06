import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N, M = map(int, input().split())

matrix = [[(False, False) for i in range(N)] for j in range(N)]
for __ in range(M):
    a, b, c = input().rstrip().split()
    a = int(a) - 1
    b = int(b) - 1
    d = c == "white"
    matrix[a][b] = (True, d)
    matrix[b][a] = (True, d)

st = list()
st.append(0)
res = []
last = -1
first = True
while st:
    v = st[-1]
    i = 0
    while i < N:
        if matrix[v][i][0]:
            if not first:
                if matrix[v][i][1] != last:
                    last = matrix[v][i][1]
                    break
            else:
                first = False
                last = matrix[v][i][1]
                break
        i += 1
    if i == N:
        res.append(st.pop())
    else:
        matrix[v][i] = (False, False)
        matrix[i][v] = (False, False)
        st.append(i)

for i in res:
    print(i + 1, end=" ")
