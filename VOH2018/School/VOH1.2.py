import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

# glasny = ("`a", "e", "i", "o", "u", "y", "`e", "`u", "a")
glasny = ("e", "i", "o", "u", "y", "a")


def lines_length(stih):
    ll = list(sum(i.count(j) for j in glasny) for i in stih)
    print("{}-{}-{}-{}".format(ll[0], ll[1], ll[2], ll[3]))


def rifma(stih):
    stih = list([i.replace("'", "") for i in stih]) \
        # if i[-2:].count("'") == 0 else i[-3:]
    rifm = ""
    ss = list([i[-2:] for i in stih])
    if ss[0] == ss[1] and ss[0] == ss[2] and ss[0] == ss[3]:
        rifm = "CCCC"
    elif ss[0] == ss[1] and ss[2] == ss[3]:
        rifm = "CCDD"
    elif ss[0] == ss[2] and ss[1] == ss[3]:
        rifm = "CDCD"
    elif ss[0] == ss[3] and ss[1] == ss[2]:
        rifm = "CDDC"

    print("NO" if len(rifm) == 0 else rifm)


stih = list([input().replace('\r', '').replace('\n', '').replace(' ', '').lower() for i in range(4)])

rifma(stih)
lines_length(stih)
