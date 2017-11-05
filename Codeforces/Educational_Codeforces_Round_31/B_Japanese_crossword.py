# import sys, codecs
#
# save_stdin = sys.stdin
# save_stdout = sys.stdout
# sys.stdin = codecs.open("input.txt", "r", "utf-8")
# sys.stdout = codecs.open("output.txt", "w+")

n, x = list(map(int, input().split()))
if n != 0:
    lens = list(map(int, input().split()))
    must_len = n - 1 + sum(lens)

    if must_len == x:
        print("YES")
    else:
        print("NO")

else:
    print("YES")
