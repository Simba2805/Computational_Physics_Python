import numpy as np
import matplotlib.pyplot as plt
# from numpy import zeros

t0 = 0
tn = 100
h = 0.01
square_h = h**2/2
n = (tn - t0)/h

# first initial condition
x0 = -1.0
v0 = 0.1
f0 = -4 *x0*(x0**2 -1)

x = np.zeros(int(n))
v = np.zeros(int(n))
f = np.zeros(int(n))

x[0] = x0
v[0] = v0
f[0] = f0

# second initial condition
x01 = 1.0
v01 = 0.1
f01 = -4 *x01*(x01**2 -1)

x1 = np.zeros(int(n))
v1 = np.zeros(int(n))
f1 = np.zeros(int(n))

x1[0] = x01
v1[0] = v01
f1[0] = f01

# for loop for first initial conditions
for i in range(int(n-1)):
  # Velocity Verlet algorithm
  x[i+1] = x[i] + h * v[i] + square_h * f[i]
  f[i+1] = -4 * x[i] * (x[i]**2 -1)
  v[i+1] = v[i] + h * (f[i+1] + f[i])/2

# for loop for second initial conditions
for i in range(int(n-1)):
  x1[i+1] = x1[i] + h * v1[i] + square_h * f1[i]
  f1[i+1] = -4 * x1[i] * (x1[i]**2 -1)
  v1[i+1] = v1[i] + h * (f1[i+1] + f1[i])/2


# --------------plotting--------------
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10.5, 5.5)
fig.suptitle('Phase trajectory using Verlet Algorithm')


ax[0].plot(x, v, 'k')
ax[0].set(xlabel = 'x', ylabel='velocity (v)')
ax[0].set_title("(x0, p0)=" +"("+str(x0) + ',' + str(v0)+")")


ax[1].plot(x1, v1, 'b')
ax[1].set(xlabel = 'x')
ax[1].set_title(" (x0, p0)=" +"("+str(x01) + ',' + str(v01)+")")


# plt.savefig('Phase-Space-Velocity-Verlet.png')
plt.show()