import turtle as t
import random as r
import copy
from math import pi, sin, cos, sqrt, acos


#--------------------SORT--------------------
arrNums = []
arrSquares = []


def swap(i):
    arrSquares[i].color("red")
    arrSquares[i + 1].color("red")
    t.delay(100)
    arrNums[i], arrNums[i + 1] = arrNums[i + 1], arrNums[i]
    arrSquares[i].forward(30)
    arrSquares[i + 1].backward(30)
    arrSquares[i], arrSquares[i + 1] = arrSquares[i + 1], arrSquares[i]
    arrSquares[i].color("black")
    arrSquares[i + 1].color("black")
    t.delay(0)


def sort():
    for i in range(len(arrNums)):
        for j in range(len(arrNums) - 1):
            if arrNums[j] > arrNums[j + 1]:
                swap(j)

#--------------------SORT--------------------

def drawTriangle(xA, yA, xB, yB, xC, yC, color):
    t.color(color)
    t.up()
    t.goto(xA, yA)
    t.begin_fill()
    t.down()
    t.goto(xB, yB)
    t.goto(xC, yC)
    t.up()
    t.end_fill()


def serpMain(xA, yA, C, deep):
    t.delay(0)
    drawTriangle(xA, yA, xA + C, yA, xA + C / 2, yA + C * sqrt(3) / 2, "black")
    Sierpinski(xA, yA, C, deep)
    t.hideturtle()

def Sierpinski(xA, yA, C, deep):
    if deep < 1:
        return
    drawTriangle(xA + C / 4, yA + C * sqrt(3) / 4, xA + 3 * C / 4, yA + C * sqrt(3) / 4, xA + C / 2, yA, "white")
    Sierpinski(xA, yA, C / 2, deep - 1)
    Sierpinski(xA + C / 4, yA + C * sqrt(3) / 4, C / 2, deep - 1)
    Sierpinski(xA + C / 2, yA, C / 2, deep - 1)

def SierpinskiRand():
    C = 800
    xA = -400
    yA = -300
    lx = -400
    ly = -300
    for i in range(5000):
        t.goto(lx, ly)
        t.dot(5, "green")
        a = r.random()
        if 3*a < 1:
            lx = (lx + xA)/2
            ly = (ly + yA)/2
        elif 3*a < 2:
            lx = (lx + C + xA)/2
            ly = (ly + yA)/2
        else:
            lx = (lx + xA + C/2)/2
            ly = (ly + yA + sqrt(3)*C/2)/2


def fern():
    x = 0
    y = 0
    for i in range(5000):
        t.goto(65 * x, 37 * y - 252)
        t.dot(5, "green")
        a = r.random()
        if a < 0.01:
            x, y = 0.00 * x + 0.00 * y, 0.00 * x + 0.16 * y + 0.00
        elif a < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
        elif a < 0.93:
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.60
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

#--------------------GAME IN LIFE--------------------
life = []
screen = t.Screen()
N = 25
field = t.Turtle()


def startGame():
    t.setup(1000, 1000)
    t.hideturtle()
    t.speed(0)
    t.tracer(0, 0)
    field.up()
    field.hideturtle()
    field.speed(0)
    field.color('green')
    for i in range(N):
        row = []
        for j in range(N):
            if r.randint(0, 7) == 0:
                row.append(1)
            else:
                row.append(0)
        life.append(row)
    updateStage()


def drawSquare(x, y, size):
    field.up()
    field.goto(x, y)
    field.down()
    field.seth(0)
    field.begin_fill()
    for i in range(4):
        field.fd(size)
        field.left(90)
    field.end_fill()


def drawStage():
    global life
    for i in range(N):
        for j in range(N):
            if life[i][j] == 1:
                lx = 800 / N * i - 400
                ly = 800 / N * j - 400
                drawSquare(lx + 1, ly + 1, 800 / N - 2)


def neighbors(x, y):
    res = 0
    for i in range(max(x - 1, 0), min(x + 1, N - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, N - 1) + 1):
            res += life[i][j]
    return res - life[x][y]


def updateStage():
    global life
    newLife = copy.deepcopy(life)
    for i in range(N):
        for j in range(N):
            k = neighbors(i, j)
            if k < 2 or k > 3:
                newLife[i][j] = 0
            elif k == 3:
                newLife[i][j] = 1
    life = copy.deepcopy(newLife)
    field.clear()
    drawStage()
    screen.update()
    screen.ontimer(updateStage, 300)

#--------------------GAME IN LIFE--------------------

if __name__ == "__main__":
    startGame()

    #t.up()
    #t.delay(0)
    #t.tracer(0, 0) #faster
    #SierpinskiRand()
    #fern()

    #arrNums = [15, 1, -6, 7, 12, -3, 6, 9]
    #t.shape("square")
    #t.up()
    #t.delay(0)
    #for i in range(len(arrNums)):
    #    a = t.clone()
    #    a.turtlesize(abs(arrNums[i]), 1)
    #    a.forward(i * 30)
    #    a.left(90)
    #    a.forward(10 * arrNums[i] - 20)
    #    a.right(90)
    #    arrSquares.append(a)
    #t.hideturtle()
    #sort()

    #serpMain(-400, -300, 800, 6)
    t.mainloop()
