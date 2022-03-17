## --------------The motion of Halley’s comet, which has a period of about 76 years-------------------


import numpy as np
import matplotlib.pyplot as plt
m= 200 # reduced mass
n = 20000
k= 39.5
h = 2/(n-1)
h2 = h**2/2

# motion in xy-plane
t = np.linspace(0, 2, n-1)  # time interval
x = np.zeros(n-1)           # distance (x-component)
y = np.zeros(n-1)           # distance (y-component)
r = np.zeros(n-1)
vx = np.zeros(n-1)
vy = np.zeros(n-1)
gx = np.zeros(n-1)
gy = np.zeros(n-1)

# initial positions
x[0] = 1.966843         # r_max = 5.28 × 10^(12) m (aphelion)
y[0] = 0
r[0] = x[0]

# initial velocity
vx[0] = 0
vy[0] = 0.815795        # v_min = 9.13 × 10^2 m/s

# initial accelerations
gx[0] = -k/(r[0]**2)
gy[0] = 0

# Verlet Algorithm for position an velocity
for i in range(n-2):

  x[i+1] = x[i] + h*vx[i] + h2*gx[i]
  y[i+1] = y[i] + h*vy[i] + h2*gy[i]
  r2 = x[i+1]**2 + y[i+1]**2
  r[i+1] = np.sqrt(r2)
  r3 = r2*r[i+1]
  gx[i+1] = -k*x[i+1]/r3
  gy[i+1] = -k*y[i+1]/r3
  vx[i+1] = vx[i] + h*(gx[i+1] + gx[i])/2
  vy[i+1] = vy[i] + h*(gy[i+1] + gy[i])/2

# positions
print('x-component ', x)
print("")
print('y-component', y)
# ---------plotting---------
plt.plot(t, r,'--',color= 'k')
plt.title('The distance between the sun and comet')
plt.xlabel('(time/76) years')
plt.ylabel('r (m/$(a = 2.68 x 10^{12})$)') #semi-major axis of orbit a =
plt.axis([0,2.0, 0, 2.0])
plt.savefig("Halley's Comet.png")
plt.show()