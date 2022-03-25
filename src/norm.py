from math import sqrt


def norm1(var):
    if isinstance(var[0], int):
        return sum(map(abs, var))
    _sum = [0] * len(var[0])
    for i in range(len(var)):
        for j in range(len(var[0])):
            _sum[j] += abs(var[i][j])
    return max(_sum)


def norm2(var):
    if isinstance(var[0], int):
        return sqrt(sum(map(lambda x: x * x, var)))
    _sum = [0] * len(var[0])
    for i in range(len(var)):
        for j in range(len(var[0])):
            _sum[j] += abs(var[i][j])
    return max(_sum)


def normInf(var):
    if isinstance(var[0], int):
        return max(map(abs, var))
    return max([sum(map(abs, i)) for i in var])


def task_1():
    vec = [4, 5, -6]
    n1 = (norm1(vec), "x1")
    n2 = (norm2(vec), "x2")
    ninf = (normInf(vec), "xInf")
    print(n1, n2, ninf)
    print("Minimum: ", min(n1, n2, ninf))
    print("Maximum: ", max(n1, n2, ninf))
    print("x2 <= x1 <= sqrt(n)*x2: ", n2[0] <= n1[0] <= n2[0] * sqrt(len(vec)))
    print("xInf <= x2 <= sqrt(n)*xInf: ", ninf[0] <= n2[0] <= ninf[0] * sqrt(len(vec)))
    print("xInf <= x1 <= n*xInf: ", ninf[0] <= n1[0] <= ninf[0] * len(vec))


def task_2():
    print(norm1([[5, -6], [-7, 8]]))
    print(normInf([[5, -6], [-7, 8]]))


if __name__ == '__main__':
    task_1()
    task_2()
