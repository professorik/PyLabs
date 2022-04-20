def queens(n):
    res = [0]
    col = [True]*n
    md = [True]*(2*n-1)
    sd = [True]*(2*n-1)
    
    def f(i):
        for j in range(n):
            if sd[i+j] and md[i-j+n-1] and col[j]:
                col[j] = False
                md[i-j+n-1] = False
                sd[i+j] = False
                if i < n - 1:
                    #print(col, md, sd)
                    f(i + 1)
                else:
                    res[0] += 1
                col[j] = True
                md[i-j+n-1] = True
                sd[i+j] = True

    f(0)
    return res


def knights(n):
    row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
    col = [1, 2, 2, 1, -1, -2, -2, -1, 1]
    res = [0]

    def isValid(x, y):
        return 0 <= x < n and 0 <= y < n

    def printPath(arr):
        for r in arr:
            print(r)
        print()

    def knightTour(visited, x, y, pos):
        visited[x][y] = pos
        if pos >= n * n:
            #printPath(visited) #comment this to not print 1728 boards
            #exit(0) #comment this to not find only 1 config
            visited[x][y] = 0
            res[0] += 1
            return
        for k in range(8):
            newX = x + row[k]
            newY = y + col[k]
            if isValid(newX, newY) and visited[newX][newY] == 0:
                knightTour(visited, newX, newY, pos + 1)
        visited[x][y] = 0


    for i in range(n//2):
        for j in range(n % 2 + n//2):
            knightTour([[0]*n for y in range(n)], i, j, 1)
    res[0] *= 4
    if n % 2 == 1:
        knightTour([[0]*n for y in range(n)], n//2, n//2, 1)
    return res[0]


if __name__ == "__main__":
    #print(queens(8))
    print(knights(5))