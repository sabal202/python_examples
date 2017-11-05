import timeit

test1 = lambda: [[3 for x in range(5000)] for x in range(5000)]

print(timeit.timeit("test1()", setup="from __main__ import test1", number=1))
