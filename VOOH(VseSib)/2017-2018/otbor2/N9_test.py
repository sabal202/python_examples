import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

pp = []
c = 0
for n in range(2, 20):
    for m in range(2, 20):
        if (n * m - 1) % 3 == 0 and n + m < 20:
            if (m, n) not in pp:
                print("n={},  m={}: P  ".format(n, m), end=" ")
            else:
                print("n={},  m={}: Inverted ".format(n, m), end=" ")
            print("SQ" if n == m else "")
            pp.append((n, m))
            c += 1
print("c={}".format(c))
