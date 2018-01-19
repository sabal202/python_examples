import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")

hd, md = map(int, input().split())
hf, mf = map(int, input().split())
d, a = map(int, input().split())
hd -= d
td = hd * 60 + md
ta = td + hf * 60 + mf
ta += a * 60
days = ta // (24 * 60)
ta %= 24 * 60
print(ta // 60, ta % 60, days)
