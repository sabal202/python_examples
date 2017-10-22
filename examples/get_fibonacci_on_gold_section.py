# this code returns Nth Fibonacci number
def fib(n):
    sqrt5 = 5 ** 0.5
    phi = (sqrt5 + 1) / 2
    return int(phi ** n / sqrt5 + 0.5)


