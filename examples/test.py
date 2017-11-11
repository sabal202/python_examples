a = bin(int(input(), 2))[2:]
s = ""
for i in range(len(a)):
    s += str(int(not bool(int(a[i]))))
y = int(a, 2)
print('{0:b}'.format(y))
print(s)
print(bool(int("0")))
