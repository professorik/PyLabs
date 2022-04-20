def root(a, r):
    x_p = -a
    x = a
    i = 0
    while abs(x - x_p) > 1e-7:
        x_p = x
        x = ((r - 1) * x + a / (x ** (r - 1))) / r
        i += 1
    print("Method1: a=%d, r = %d, iterations=%d, res=%s" % (a, r, i, x))


def root_2(a, r):
    x = a
    i = 0
    while abs(x ** r - a) > 1e-7:
        x = ((r - 1) * x + a / (x ** (r - 1))) / r
        i += 1
    print("Method2: a=%d, r = %d, iterations=%d, res=%s" % (a, r, i, x))


if __name__ == '__main__':
    for i in range(2, 5):
        for j in range(2, 5):
            root(i, j)
            root_2(i, j)
            print()