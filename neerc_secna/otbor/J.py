import codecs
import sys

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

N, M, D = list(map(int, input().split()))
clear_el = dict()
spectrs = []


def equals(spectr, clear_s):
    b = True
    for i in range(len(spectr)):
        if clear_s[i] == "0":
            if spectr[i] != "0":
                b = False
    return b


for __ in range(N):
    spectr, name = input().split()
    clear_el[spectr] = name

for __ in range(M):
    els = []
    b = False
    spectr = input().split()[0]
    for i in clear_el.keys():
        if equals(spectr, i):
            b = True
            els.append(clear_el[i])
    if b:
        print(",".join(sorted(els)))
    else:
        print("unknown")
