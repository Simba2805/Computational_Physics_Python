## ----------------Heat Equation in a 1D Rod--------------
import numpy as np
import matplotlib.pyplot as plt
L=1                         # length of the rod
T=4                         # total time for simulation
k=1
Nx=50                       # number of grid points on the rod
Nt=50                       # NUMBER OF TIME STEPS
dx=L/Nx
dt=T/Nt
alpha=k*dt/dx**2
# print(alpha)
# alpha=1.5
# alpha=0.4

x = np.linspace(0,L,Nx+1)   #points on the rod
t = np.linspace(0,T,Nt+1)   # time steps
u_n=np.zeros((Nx+1, Nt+1))
# u_n[:,0]=20



u_n[:,0]=np.sin(2*np.pi*x)    # Initial condition , sine wave
u_init=np.copy(u_n)
u_n[-1]=0

for i in range(1,Nt):
    # print("Time t =",t[i])
    for j in range(1,Nx):
        u_n[j,i+1]=u_n[j,i]+alpha*(u_n[j+1,i]+u_n[j-1,i]-2*u_n[j,i])
    u_n-=u_n*dt
    plt.figure("Temperature profile", figsize =(5,4))
    plt.plot(x,u_n,color='red',label='Current Temperature profile')
    plt.plot(x,u_init,color='black',label='Initial Temperature profile')
    # plt.plot(0,0,color='red',label='Elapsed time '+str(dt))
    # ax=plt.axes(projection='3d')
    # ax.plot3D(x,u)
    plt.title(" Heat Equation for 1D rod")
    plt.axis([0,L,-1.7,1.7])
    string="Time $t$ = " +str(t[i])+ ' $T_{max}$ = '+str(np.amax(u_n))+ '$^o C$, $T_{min}$ = '+str(np.amin(u_n))+'$^o C$'
    plt.suptitle(string)
    plt.xlabel("Distance(m)",fontsize=10)
    plt.ylabel("Temperature(T)", fontsize=10)

    plt.grid()

    plt.show(block=False)  ## Or  plt.draw()
    plt.pause(0.001)
    plt.clf()
    plt.legend('Temperature at each x')

