import random as r

# g - graph, a - start vertex
def calculate(g, a, _deep):
    n = len(g)
    nums = [0]*n
    deep = _deep
    while deep > 0:
        deep -= 1
        nums[a] += 1
        k = r.random()
        tmpSum = 0
        for i in range(n):
            tmpSum += g[a][i]
            if tmpSum >= k:
                a = i
                break
    for i in range(n):
        nums[i] /= _deep
    return nums
    

def build_graph(g):
    n = len(g)
    p = []
    for i in range(n):
        p.append([0]*n)
        k = sum(g[i])
        if k != 0:
            x = (1 - 0.15*n)/k
        else:
            x = -1
        for j in range(n):
            if x != -1:
                p[i][j] = g[i][j] * x + 0.15
            else:
                p[i][j] = 1/n 
    return p        


if __name__ == "__main__":
    g = [[0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0], 
        ]
    p = build_graph(g)
    #print(p)
    for i in range(len(p)):
        print(calculate(p, i, 10000))
