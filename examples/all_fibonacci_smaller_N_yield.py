def fibonacci(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a + b  # concurrent assignment


N = int(input())
for n in fibonacci(N):
    print(n)
