import sys
import copy
import numpy
import fractions


def solve(A, n, x):
    for i in range(n):
        if A[i][i] == 0.0:
            print("Impossible to calculate")
            sys.exit()
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n + 1):
                A[j][k] = A[j][k] - ratio * A[i][k]
    x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]


def calcDiff(A, n, x):
    sum = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += A[i][j] * x[j]
        sum += abs(tmp - A[i][n])
    return sum


if __name__ == "__main__":
    f = open("D:\\PycharmProjects\\graphics\\res.txt", "w", encoding='utf-8')
    for size in range(2, 21):
        a = numpy.zeros((size, size + 1))
        aF = numpy.zeros((size, size + 1), dtype=fractions.Fraction)
        res = numpy.zeros(size)
        resF = numpy.zeros(size, dtype=fractions.Fraction)
        for i in range(size):
            for j in range(size):
                a[i][j] = 1 / (i + j + 1)
                aF[i][j] = fractions.Fraction(1, i + j + 1)
            a[i][size] = 1
            aF[i][size] = fractions.Fraction(1, 1)
        # print(a)
        # print(aF)
        solve(copy.deepcopy(a), size, res)
        solve(copy.deepcopy(aF), size, resF)
        delta = 0
        print("Fractions\t\t\t\tNums")
        for i in range(size):
            print("X%d = " % i, + resF[i], '\t', "X%d = " % i, res[i])
            delta += abs(resF[i] - res[i])
        dif = calcDiff(a, size, res)
        f.write("n = %d delta = %f zero_diff = %s\n" % (size, delta, dif))
        print("delta = %f" % delta, '\t\t', "dif_frac = ", calcDiff(aF, size, resF), '\t\t', "dif_num = ", dif)
    f.write('''Видно, что при увеличении кол-ва переменных разность между актуальным решением и решением, 
полученным численными методами на компьютере со 
стандартными типами данных, становится все больше''')
