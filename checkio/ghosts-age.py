def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def checkio(opacity):
    ages = [10000]
    fibs = []
    for n in fibonacci(5000):
        fibs.append(n)

    while len(ages) < 5000:
        age = len(ages)
        if age in fibs:
            ages.append(ages[-1] - age)
        else:
            ages.append(ages[-1] + 1)
    return ages.index(opacity)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
