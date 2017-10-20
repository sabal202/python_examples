a = bin(int(input()))[2:]
b = bin(int(input()))[2:]
y = int(a, 2) ^ int(b, 2)
print('{0:b}'.format(y))
print(y)
