def basicPerm(n):
    x = list(range(1, n + 1))


    def p(t):
        if t == n - 1:
            print(x)
            return
        for j in range(t, n):
            x[j], x[t] = x[t], x[j]
            p(t+1)
            x[j], x[t] = x[t], x[j]

    p(0)


def permutations(n):
    arr = [[0], [1]]


    def printArr(arr):
        for a in arr:
            print(a)


    def p():
        if len(arr[0]) == n:
           return
        for i in range(len(arr)):
            arr.append(arr[i].copy())
        for i in range(len(arr)//2):
            arr[i].append(0)
            arr[len(arr)//2 + i].append(1)
        p()

    p()
    printArr(arr)


if __name__ == "__main__":
    #basicPerm(3)
    permutations(3)
