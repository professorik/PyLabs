import turtle as t
import time
import random


class TurtleArray:
    GAP = 30

    def __init__(self, arr):
        t.showturtle()
        self.arr = arr
        self.tArr = []
        t.shape("square")
        t.up()
        t.delay(0)
        for i in range(len(arr)):
            a = t.clone()
            a.turtlesize(abs(arr[i]) if arr[i] != 0 else 0.5, 1)
            a.forward(i * self.GAP)
            a.left(90)
            a.forward(10 * arr[i] - 20)
            a.right(90)
            self.tArr.append(a)
        t.hideturtle()

    def swap(self, i, j):
        self.tArr[i].color("red")
        self.tArr[j].color("red")
        t.delay(50)
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.tArr[i].forward(self.GAP * (j - i))
        self.tArr[j].backward(self.GAP * (j - i))
        self.tArr[i], self.tArr[j] = self.tArr[j], self.tArr[i]
        self.tArr[i].color("black")
        self.tArr[j].color("black")
        t.delay(0)

    def compare(self, i, j):
        t.delay(0)
        self.tArr[i].color("green")
        self.tArr[j].color("green")
        time.sleep(0.5)
        self.tArr[j].color("black")
        self.tArr[i].color("black")
        return self.arr[i] - self.arr[j]

    def color(self, i, _color):
        self.tArr[i].color(_color)


def bubbleSort(arr):
    temp = TurtleArray(arr)
    arrLen = len(arr)
    for i in range(arrLen - 1):
        fl = True
        for j in range(arrLen - i - 1):
            if temp.compare(j, j + 1) > 0:
                temp.swap(j, j + 1)
                fl = False
        if fl: break


def quickSort(arr):
    temp = TurtleArray(arr)

    def bubble(l, r):
        for i in range(r - l):
            fl = True
            for j in range(r - l - i):
                if temp.compare(j + l, j + l + 1) > 0:
                    temp.swap(j + l, j + l + 1)
                    fl = False
            if fl: break

    def median(l, r):
        m = (l+r)//2
        par = (arr[l] + arr[r] + arr[m]) - max(arr[l], arr[r], arr[m]) - min(arr[l], arr[r], arr[m])
        if par == arr[l]:
            return l
        elif par == arr[r]:
            return r
        else:
            return m

    def qs(left, right):
        if right - left < 3:
            bubble(left, right)
            return
        med = median(left, right)
        temp.swap(med, (left+right)//2)
        v = arr[(left+right)//2]
        a, b = left, right
        while a <= b:
            while arr[a] < v or temp.compare(a, a):
                a = a + 1
            while arr[b] > v or temp.compare(b, b):
                b = b - 1
            if a >= b: break
            temp.swap(a, b)
            a = a + 1
            b = b - 1
        qs(left, b)
        qs(b + 1, right)

    qs(0, len(arr) - 1)


if __name__ == "__main__":
    testArr = []
    for i in range(8):
        testArr.append(random.randint(-15, 15))
    #testArr = [5, 5, 5, 5, 5, 5, 5, 5]
    #testArr = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    #testArr.reverse()
    print(testArr)
    t.up()
    t.delay(0)
    t.goto(-400, -300)
    t.write('Bubble Sort', font=('Arial', 40, 'bold'))
    t.goto(100, -300)
    t.write('Quick Sort', font=('Arial', 40, 'bold'))

    t.goto(-400, 100)
    timer = time.time()
    bubbleSort(testArr.copy())
    t.goto(-400, -400)
    t.write('%.5f' % (time.time() - timer), font=('Arial', 30, 'bold'))

    t.goto(100, 100)
    timer = time.time()
    quickSort(testArr)
    t.goto(100, -400)
    t.write('%.5f' % (time.time() - timer), font=('Arial', 30, 'bold'))

    t.mainloop()
