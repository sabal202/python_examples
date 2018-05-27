N = int(input())
Sa, Sb, Sc = 0, 0, 0
minR = 10001
for i in range(N):
    a, b, c = map(int, input().split())
    t1 = a + max(Sa, Sb)
    t2 = b + max(Sa, Sb, Sc)
    t3 = c + max(Sb, Sc)
    Sa, Sb, Sc = t1, t2, t3
print(Sa, Sb, Sc)
S = max(Sa, Sb, Sc)
print(S)