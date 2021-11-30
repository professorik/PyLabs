def c(n):
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


if __name__ == "__main__":
    print(c(int(input('Enter n: '))))
