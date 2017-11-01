def checkio(data):
    # x1, y1, x2, y2, x3, y3
    a, b, c, d, e, f = list(map(int, [data[1], data[3], data[7], data[9], data[13], data[15]]))
    # this formulas are derived from the equality of the squares of the radii
    x0 = ((f - d) * (a ** 2 + b ** 2) + (b - f) * (c ** 2 + d ** 2) + (d - b) * (e ** 2 + f ** 2)) / \
         (2 * (d * (e - a) + f * (a - c) + b * (c - e)))

    y0 = ((e - c) * (a ** 2 + b ** 2) + (a - e) * (c ** 2 + d ** 2) + (c - a) * (e ** 2 + f ** 2)) / \
         (2 * (a * (d - f) + c * (f - b) + e * (b - d)))

    r = round(((a - x0) ** 2 + (b - y0) ** 2) ** 0.5, 2)
    if r == int(r):
        r = int(r)

    x0 = round(x0, 2)
    if x0 == int(x0):
        x0 = int(x0)

    y0 = round(y0, 2)
    if y0 == int(y0):
        y0 = int(y0)

    return "(x-{})^2+(y-{})^2={}^2".format(x0, y0, r)
