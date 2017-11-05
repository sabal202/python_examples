import random

print(" ".join(list(map(str, [random.randint(1, 10 ** 9) for i in range(200000)]))))
