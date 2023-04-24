import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(polar=True)
ax.spines['polar'].set_visible(True)

#plt.xticks([])
plt.yticks([])

plt.xlim([0, 2 * np.pi])
plt.ylim([0, 4])


def f(t, x):
    return x[0] * (x[0] - 1) * ((x[0] - 2)**2) * (3 - x[0]), 1


N = 500
T = 30
t = np.linspace(0, T, N)

x0 = [0.8, np.pi / 4]
res = solve_ivp(f, [0, T], x0, dense_output=True)
s = res.sol(t)
ax.plot(s[1], s[0], color='cyan')
ax.plot(x0[1], x0[0], 'go')

x0 = [1.3, np.pi / 2]
res = solve_ivp(f, [0, T], x0, dense_output=True)
s = res.sol(t)
ax.plot(s[1], s[0], color='orange')
ax.plot(x0[1], x0[0], 'go')

x0 = [2.3, np.pi / 4]
res = solve_ivp(f, [0, T], x0, dense_output=True)
s = res.sol(t)
ax.plot(s[1], s[0], color='yellow')
ax.plot(x0[1], x0[0], 'go')

x0 = [3.5, np.pi / 10]
res = solve_ivp(f, [0, T], x0, dense_output=True)
s = res.sol(t)
ax.plot(s[1], s[0], color='purple')
ax.plot(x0[1], x0[0], 'go')

ax.plot(np.linspace(0, 2 * np.pi, N), np.ones(N), color='red')
ax.plot(np.linspace(0, 2 * np.pi, N), np.ones(N) * 2, color='green')
ax.plot(np.linspace(0, 2 * np.pi, N), np.ones(N) * 3, color='blue')

#plt.tight_layout()
plt.show()
