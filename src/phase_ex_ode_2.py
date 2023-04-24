# Рівняння ван дер Поля як швидко-повільна система. Анімація
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 1
m = 1
v0 = 0.5
F0 = 1


def F(x):
    return np.vectorize(lambda arg: F0 if arg < v0 else -F0)(x)


def f(t, x):
    x1, x2 = x
    y1 = x2
    y2 = (-k * x1 + F(x2)) / m
    return y1, y2


fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.set_xlim([-0.5, 2.5])
ax.set_ylim([-1.5, 1.5])
plt.suptitle('k=' + str(k) + ',m=' + str(m) + ',F0=' + str(F0) + ',v0=' + str(v0))
x0 = [2, 1.3]
dt = 0.05
T = 14.4
t = np.arange(0, T, dt)

res = solve_ivp(f, [0, T], x0, dense_output=True)
x = res.sol(t)
ax.plot(x[0], x[1])
ax.grid()

x1 = np.linspace(-0.5, 2.5, 31)
x2 = np.linspace(-1.5, 1.5, 31)
xx1, xx2 = np.meshgrid(x1, x2)
ff1, ff2 = f(0, [xx1, xx2])
ax.quiver(xx1, xx2, ff1, ff2)

z = ax.scatter([], [], c='red')


def animate(i):
    z.set_offsets(x[:, i])
    return z,


anim = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)
plt.show()
#anim.save('D:/PycharmProjects/graphics/src/anim.gif')
