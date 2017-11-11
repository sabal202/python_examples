a = bin(int(input()))[2:]
b = bin(int(input()))[2:]
y = int(a, 2) ^ int(b, 2)
print('{0:b}'.format(y))
print(y)


#
# def invert(sp):
#     s = ""
#     for i in range(len(sp)):
#         s += str(int(not bool(int(sp[i]))))
#     return s
#
#
# def AND(spectr, clear_s):
#     y = int(spectr, 2) & int(clear_s, 2)
#     if '{0:b}'.format(y).zfill(D) == clear_s:
#         return True
#     return False
