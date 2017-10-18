# Примеры
# входные данные
# 2 3
# 4 2
# 5 7 6
# выходные данные
# 25

# входные данные
# 8 8
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# выходные данные
# 1
n, m = list(map(int, input().split()))
a = list([i for i in map(int, input().split())])
b = list([i for i in map(int, input().split())])

am = min(a)
bm = min(b)
c = a + b
t = True
c.sort()
for i in c:
    if c.count(i) > 1:
        print(i)
        t = False
        break

if t:
    print(str(min(am, bm)) + str(max(am, bm)))
