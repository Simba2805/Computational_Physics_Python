import matplotlib.pyplot as plt
N = 1000
m= 1
t = 1
t_f = 10
# first initial conditions
x0 = 1
x_f = 10
h =(x_f -x0)/N
p0 = 0.10
p_f = 1
h1 = (p_f-p0)/N

# 2nd Initial conditions
N1 = 1000
t1 = 1
t1_f = 10
x1 = -1
x1_f = 10
h_1 =(x1_f -x1)/N1
p1 = 0.10
p1_f = 1
h1_1 = (p1_f-p1)/N1

# 3rd initial conditions
N2= 1000
m= 1
t2 = 1
t2_f = 10

x2 = 1
x2_f = 10
h_2 =(x2_f -x2)/N2
p2 = 10
p2_f = 100
h2_1 = (p2_f-p2)/N2


def dxdt(p,t):
  return p/m

def dpdt(x,t):
  return -4*x*(x**2-1)

# first trajectory
x_list =[]
p_list =[]

while t< t_f:
  x0 += dxdt(p0, t)*h
  p0 += dpdt(x0, t)*h1
  x_list.append(x0)
  p_list.append(p0)
  t += h

# 2nd Trajectory
x_list1 =[]
p_list1 =[]

while t1< t1_f:
  x1 += dxdt(p1, t)*h_1
  p1 += dpdt(x1, t)*h1_1
  x_list1.append(x1)
  p_list1.append(p1)
  t1 += h

# 3rd trajectory
x_list2 =[]
p_list2 =[]

while t2< t2_f:
  x2 += dxdt(p2, t)*h_2
  p2 += dpdt(x2, t)*h2_1
  x_list2.append(x2)
  p_list2.append(p2)
  t2 += h




plt.plot(x_list, p_list,'r' )
plt.plot( x_list1, p_list1, 'b')
plt.plot(x_list2, p_list2,'g')
plt.savefig("Phase-trajectory.png")
plt.xlabel('x')
plt.ylabel('p')
plt.title("Phase Space Trajectory Using Euler Method")
plt.show()