import turtle as t
from math import pi, sin, cos, sqrt, acos

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
    serpinsky(xA, yA, C, deep)
    t.hideturtle()
    t.mainloop()


def serpinsky(xA, yA, C, deep):
    if deep < 1:
        return
    drawTriangle(xA + C / 4, yA + C * sqrt(3) / 4, xA + 3 * C / 4, yA + C * sqrt(3) / 4, xA + C / 2, yA, "white")
    serpinsky(xA, yA, C / 2, deep - 1)
    serpinsky(xA + C / 4, yA + C * sqrt(3) / 4, C / 2, deep - 1)
    serpinsky(xA + C / 2, yA, C / 2, deep - 1)


if __name__ == "__main__":
    arrNums = [15, 1, -6, 7, 12, -3, 6, 9]
    t.shape("square")
    t.up()
    t.delay(0)
    for i in range(len(arrNums)):
        a = t.clone()
        a.turtlesize(abs(arrNums[i]), 1)
        a.forward(i*30)
        a.left(90)
        a.forward(10*arrNums[i] - 20)
        a.right(90)
        arrSquares.append(a)
    t.hideturtle()
    sort()
    t.mainloop()
    #serpMain(-400, -300, 800, 6)
