def ex0():
    a = 0
    while a < 10:
        a = a + 1
    print(a)


def ex1():
    print(int(input('Input x: ')) // 2)


def ex2():
    s = input('Input string: ')
    for i in range(len(s)):
        if s[i] == '1':
            print('Yes', end=' ')


def ex3():
    s = input('Input string: ')
    for i in s:
        if i == '1':
            print('Yes', end=' ')


def ex4():
    s = input('Input string: ')
    print('Yes ' * s.count('1'))


def ex5():
    print(input('Input string: ')[::-1])


def summa(a, b):
    return a if a == b else a + b


def pr0(a, b):
    return a + b if a != b else (a + b) * 2


def pr1(a):
    return abs(a - 20) if a < 20 else 2 * abs(a - 20)
    # return 20 - a if a < 20 else 2 * (a - 20)


def pr2(a, b):
    return a == 10 or b == 10 or a + b == 10


def pr3(a):
    return abs(a - 100) <= 10 or abs(a - 200) <= 10


def pr4(a, b):
    return a * b < 0


def pr5(a, b, fl):
    return (fl and a * b < 0) or (not fl and a > 0 and b > 0)


def pr6(s):
    return s.count('0') > 0


def pr7(s):
    return s[-1] + s[1:-1] + s[0]


def pr8(s, n):
    return s[n:] + s[:n]


def pr9(s):
    if s.startswith('not'):
        return s
    return 'not' + s


def pr10(s, n):
    return s[:n] + s[(n + 1):]


def pr11(s):
    return 3 * s[:3] + s[3:]


def pr12(s1, s2):
    n = min(len(s1), len(s2))
    i = n // 2
    while 0 < i < n:
        if s1[:i] != s2[:i]:
            n = i
            i = i // 2
        elif i < n - 1:
            i = (i + n) // 2
        elif s1[:n] == s2[:n]:
            i = n
        else:
            n = i
    return i


if __name__ == '__main__':
    print(pr12(input('Input str1: '), input('Input str2: ')))
    # print(pr11(input('Input str: ')))
    # print(pr10(input('Input str: '),int(input('Input n: '))))
    # print(pr9(input('Input str: ')))
    # print(pr8(input('Input str: '),int(input('Input n: '))))
    # print(pr7(input('Input str: ')))
    # print(pr6(input('Input str: ')))
    # print(pr0(1,2))
    # print(pr0(2,2))
    # print(pr1(21))
    # print(pr1(-3))
    # print(pr2(10,0))
    # print(pr2(9,1))
    # print(pr2(7,2))
    # print(pr3(99))
    # print(pr3(150))
    # print(pr4(1,-1))
    # print(pr4(1,2))
    # print(pr4(-1,-2))
    # print(pr5(2,3,True))
    # print(pr5(-2,3,True))
    # print(pr5(2,3,False))
    # print(pr5(2,-3,False))
