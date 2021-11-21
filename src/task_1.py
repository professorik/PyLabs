def pr0(arr):
    return max(arr) - min(arr)


def pr1(arr):
    return sum(arr[:3])


def pr2(arr):
    return [max(arr[0], arr[-1])] * len(arr)


def pr3(arr):
    if len(arr) == 1:
        return 0
    return (sum(arr) - min(arr) - max(arr)) / (len(arr) - 2)


def pr4(arr):
    return [x ** 3 for x in arr]


def pr5(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


def pr6(arr):
    return len(pr5(arr))


def pr7(arr):
    return 2 in arr or 3 in arr


def pr8_0(arr):
    arr[0] = ';' + str(arr[0])
    arr[-1] = str(arr[-1]) + ';'
    return ';2;2;' in ';'.join(map(str, arr))


def pr8_1(arr):
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] and arr[i] == 2:
            return True
    return False


def pr9(arr):
    return sum([x for x in arr if x != 13])


def pr10(arr):
    return [x for x in arr if not isinstance(x, list)]


def magic(elem):
    # it's possible without string
    elem = str(elem)
    if elem[0] == '1' and elem[-1] == '2':
        return 0
    elif elem[0] == '1':
        return int(elem[:elem.rfind('1') + 1])
    return int(elem)


def pr11(arr):
    return sum(map(magic, arr))


def pr11_new_interpret(arr):
    s = -1
    last = -1
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            last = i
            if s == -1:
                s = i
        elif arr[i] == 2 and s != -1:
            del (arr[s:i+1])
            i -= (i+1-s)
            s = -1
        i += 1
    if last != -1:
        del (arr[last+1:])
    return sum(arr)


if __name__ == '__main__':
    #all lengths are greater than zero
    print(pr0([9, 2, -3, 6, 0]))
    print(pr1([9, 2, -3, 6, 0]))
    print(pr2([9, 2, -3, 6, 0]))
    print(pr3([9, 2, -3, 6, 0]))
    print(pr4([9, 2, -3, 6, 0]))
    print(pr5([9, 2, -3, 6, 0]))
    print(pr6([9, 2, -3, 6, 0]))
    print(pr7([9, 2, -3, 6, 0]))
    print(pr8_0([9, 2, -3, 6, 0, 2, 2]))
    print(pr8_1([9, 2, 2, 2, -3, 6, 0]))
    print(pr9([9, 13, 13, -1]))
    print(pr10([9, 13, [1, 2, 3, 4], -1, [23, 4, 4, [1, 2, 3]], 2]))
    print(pr11([9, 131, 12342, 1232145]))
    print(pr11_new_interpret([2, 1, 3, 4, 5, 2, 3, 1, 9, 2, 9, 1, 8, 765]))
