import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

A, B = list(map(int, input().split()))
d, D = list(map(lambda x: int(x) * 2, input().split()))

if (d + D <= A and D <= B and d <= B) or (d + D <= B and D <= A and d <= A):
    print("YES")
else:
    print("NO")
