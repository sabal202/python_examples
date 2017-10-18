def func(a, b, c):
    if a * b == c:
        print("Yes")
        print("{} {} {}".format(a, b, c))
        return
    if c * b == a:
        print("Yes")
        print("{} {} {}".format(c, b, a))
        return
    if a * c == b:
        print("Yes")
        print("{} {} {}".format(a, c, b))
        return
    print("No")


a, b, c = map(int, input().split())
func(a, b, c)
