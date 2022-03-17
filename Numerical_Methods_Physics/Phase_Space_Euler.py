import numpy as np
import matplotlib.pyplot as plt


x0 = float(input('Enter initial position(x0 = 1 ,-1 or 1): '))       # Initial position

v0 = float(input('Enter initial velocity (v0 = 0.1, 0.1 or 10): '))  # Initial Velocity
t1 = 0
tn = 100

h = 0.01                                                             # time interval

n = (tn-t1)/h                                                        # number of steps

                                                                     # initialization for position and velocity
x = np.zeros(int(n))
v = np.zeros(int(n))

force0 = -4 *x0*(x0**2 -1)                                           # Initial force
force = np.zeros(int(n))
force[0] = force0
x[0] = x0
v[0] = v0
for i in range(int(n-1)):
  force[i] = -4 * x[i] * (x[i]**2 -1)                                # updating values
  v[i+1] = v[i] + force[i] * h
  x[i+1] = x[i] + v[i] * h

                                    #--------- plotting----------
plt.figure("Phase space Trajectory (x0, p0)=(1, 0.1)", figsize =(7,5))
plt.plot(x, v, color = 'black')

plt.xlabel('position (x)')
plt.ylabel('Velocity (v)')
plt.title("Phase space Trajectory (x0, p0)=" +"("+str(x0) + ',' + str(v0)+")")
# plt.savefig(f"Phase-space-Trajectory-{(x0, v0)}.png")
plt.show()

# plt.show(block =False)
# plt.pause(0.0001)
# plt.clf()