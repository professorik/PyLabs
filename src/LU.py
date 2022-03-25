def solve(A):
    n = len(A)
    U = [[0] * n for _i in range(n)]
    L = [[0] * n for _i in range(n)]
    for i in range(n):
        L[i][i] = 1
    for i in range(n):
        U[i][i] = A[i][i] - sum([L[i][k] * U[k][i] for k in range(i)])
        for j in range(i + 1, n):
            U[i][j] = A[i][j] - sum([L[i][k] * U[k][j] for k in range(i)])
            L[j][i] = (A[j][i] - sum([L[j][k] * U[k][i] for k in range(i)])) / U[i][i]
    return U, L


def multiple(A, B):
    n, m, l = len(A), len(B[0]), len(B)
    assert l == len(A[0])
    C = [[0] * n for _i in range(m)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                C[i][j] += A[i][k] * B[k][j]
    return C


def print_matrix(A, message=""):
    if len(message) > 0:
        print(message)
    s = [[str(e) for e in row] for row in A]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table), "\n")


def test(A):
    global test_case_id
    test_case_id += 1
    print("Test Case #%d" % test_case_id)
    U, L = solve(A)
    print_matrix(A, "Input:")
    print_matrix(L, "Matrix L:")
    print_matrix(U, "Matrix U:")
    assert multiple(L, U) == A
    print_matrix(multiple(L, U), "Check. Similar to input")
    print("-" * 30)


if __name__ == '__main__':
    test_case_id = 0
    test([[10, -7, 0], [-3, 6, 2], [5, -1, 5]])
    test([[-3, 2, 5, -4], [3, 2, -7, 1], [-3, -18, 18, 12], [-3, 10, 1, -13]])
