def checkio(data):
    a, b, c, d, e, f = list(map(int, [data[1], data[3], data[7], data[9], data[13], data[15]]))
    x0 = round(((f - d) * (a ** 2 + b ** 2) + (b - f) * (c ** 2 + d ** 2) + (d - b) * (e ** 2 + f ** 2)) / \
               (2 * (d * (e - a) + f * (a - c) + b * (c - e))), 2)
    if x0 == int(x0):
        x0 = int(x0)

    y0 = round(((e - c) * (a ** 2 + b ** 2) + (a - e) * (c ** 2 + d ** 2) + (c - a) * (e ** 2 + f ** 2)) / \
               (2 * (a * (d - f) + c * (f - b) + e * (b - d))), 2)
    if y0 == int(y0):
        y0 = int(y0)
    r = round(((a - x0) ** 2 + (b - y0) ** 2) ** 0.5, 2)
    if r == int(r):
        r = int(r)
    return "(x-{})^2+(y-{})^2={}^2".format(x0, y0, r)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
