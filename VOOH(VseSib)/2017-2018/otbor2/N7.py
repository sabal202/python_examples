import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

sym = dict()

s = input().rstrip().replace(" ", "")
for i in s:
    if i in sym:
        sym[i] += 1
    else:
        sym[i] = 1

size = len(sym)

if size == 1:
    print(1)
elif size == 2:
    print(0)
else:
    l = []
    for i in sym.values():
        l.append(i)
    l.sort(reverse=True)

    print(sum(l[2:]))
