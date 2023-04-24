import numpy as np

if __name__ == "__main__":
    #A = np.array([[1, 3.61, 0], [3.61, 1.22, -1.11], [0, -1.11, 6.7]], np.float64)
    A = np.array([[2, 0, -1], [2, 4, -3], [3, 2, 4]], np.float64)
    Q, R = np.linalg.qr(A)
    print(Q)
    print(R)
    print(Q.dot(R))
    for i in range(500):
        Q, R = np.linalg.qr(A)
        A = R.dot(Q)
    print(A)

'''
[[ 7.03681885e+000  7.94661158e-017  1.33570986e-015]
 [-3.18345813e-099  4.44992314e+000  2.48366567e-015]
 [ 0.00000000e+000 -8.82966366e-119 -2.56674200e+000]]
 Eigenvalues 7.03681885, 4.44992314, -2.56674200
'''