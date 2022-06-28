# -*- coding: utf-8 -*-
import numpy as np


def cgs(A):
    m, n = A.shape
    Q = np.copy(A)
    R = np.zeros([n, n], dtype='float64')

    for i in range(n):
        R[:i, i] = A[:, i].T.dot(Q[:, :i])
        Q[:, [i]] = A[:, [i]] - Q[:, :i].dot(R[:i, [i]])

        R[i, i] = np.linalg.norm(Q[:, i])
        if np.abs(R[i, i]) < 1e-15:
            Q[:, i] = np.zeros(m, dtype='float64')
            R[i, i] = 0.
        else:
            Q[:, i] /= R[i, i]
    return Q, R


def mgs(A):
    m, n = A.shape
    Q = np.copy(A)
    R = np.zeros([n, n], dtype='float64')

    for i in range(n):
        R[i, i] = np.linalg.norm(Q[:, i])
        if np.abs(R[i, i]) < 1e-15:
            Q[:, i] = np.zeros(m, dtype='float64')
            R[i, i] = 0.
        else:
            Q[:, i] /= R[i, i]

        R[[i], i + 1:] = Q[:, [i]].T.dot(Q[:, i + 1:])
        Q[:, i + 1:] -= Q[:, [i]].dot(R[[i], i + 1:])
    return Q, R


if __name__ == "__main__":
    g = [[2., 0., -1.],
         [2., 4., -3.],
         [3., 2.,  4.]]
    A = np.asmatrix(g)
    print(cgs(A))
    print(mgs(A))