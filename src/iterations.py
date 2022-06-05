import numpy as np
import scipy.linalg as sclin


def prepareForGS(A, b, n):
    LD = np.tril(A)
    LDI = sclin.solve_triangular(LD, np.identity(n), lower=True)
    U = A - LD
    C = - LDI.dot(U)
    d = LDI.dot(b)
    return C, d


def prepareForJacoby(A, b, n):
    D = np.diag(A)
    DI = np.diag(1 / D)
    I = np.identity(n)
    C = I - DI.dot(A)
    d = DI.dot(b)
    return C, d


def solveJacoby(A, b, eps=0.05):
    n = A.shape[0]
    C, d = prepareForJacoby(A, b, n)
    x = np.zeros((n,))
    y = d
    i = 0
    while np.linalg.norm(x - y, np.inf) > eps:
        x = y
        y = C.dot(x) + d
        i += 1
    return y, i


def solveGaussSeidel(A, b, eps=0.05):
    n = A.shape[0]
    C, d = prepareForGS(A, b, n)
    x = np.zeros((n,))
    y = d
    i = 0
    while np.linalg.norm(x - y, np.inf) > eps:
        x = y
        y = np.dot(C, x) + d
        i += 1
    return y, i


def loss(A, b, x):
    return np.linalg.norm(A.dot(x) - b, np.inf)


def resultLoss(x, x0):
    return np.linalg.norm(x - x0, np.inf)


if __name__ == "__main__":
    A = np.matrix([[5, 1, 1], [2, 6, 1], [2, 2, 7]])
    b = np.matrix([10, 17, 27]).transpose()
    res = np.matrix([1, 2, 3]).transpose()
    delta = 0.005
    x, i = solveJacoby(A, b, delta)
    #9 times
    print("For %s loss - iterated %d times. Actual loss %s" % (loss(A, b, x), i, resultLoss(res, x)))
    x, i = solveGaussSeidel(A, b, delta)
    #3 times
    print("For %s loss - iterated %d times. Actual loss %s" % (loss(A, b, x), i, resultLoss(res, x)))