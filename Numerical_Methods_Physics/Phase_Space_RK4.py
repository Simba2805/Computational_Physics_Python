import numpy as np
import matplotlib.pyplot as plt
x0 = float(input('Enter initial position(x0 = 1 ,-1 or 1): '))       # Initial position

v0 = float(input('Enter initial velocity (v0 = 0.1, 0.1 or 10): '))  # Initial Velocity
t1 = 0
tn = 100

h = 0.01

"""
''While using third initial condition set tn = 10 and h = 0.001''
"""
n = (tn-t1)/h
x = np.zeros(int(n))
v = np.zeros(int(n))
# force
force0 = -4 *x0*(x0**2 -1)
force = np.zeros(int(n))
force[0] = force0
x[0] = x0
v[0] = v0
def force(x):
  return -4 * x * (x**2 -1)

for i in range(int(n-1)):
  
  s1 = force(x[i])
  s2 = force(x[i] + h/2)
  s3 = force(x[i] + h/2)
  s4 = force(x[i]+h)
  s = (s1+2*s2+2*s3+s4)/6
  v[i+1] = v[i] + s * h
  x[i+1] = x[i] + v[i] *h 

                                    #--------- plotting----------
plt.figure("Phase space Trajectory RK4 (x0, p0)=(1, 0.1)", figsize =(7,5))
plt.plot(x, v, color = 'blue')

plt.xlabel('position (x)')
plt.ylabel('Velocity (v)')
plt.title("Phase space Trajectory RK4 (x0, p0)=" +"("+str(x0) + ',' + str(v0)+")")
# plt.savefig(f"Phase-space-Trajectory-RK4-{(x0, v0)}.png")
plt.show()

# plt.show(block =False)
# plt.pause(0.0001)
# plt.clf()