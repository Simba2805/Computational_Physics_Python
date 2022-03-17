                         ## ----------------Heat Equation in a 1D Rod(BTCS)--------------
                          #-----------------Laasonen (BTCS) Scheme-----------------------
                          #------------(BTCS--Backward Time Central space )--------------
from scipy.sparse import diags
import numpy as np
import matplotlib.pyplot as plt


L = 0.04                  # length of the rod
T = 1                     # Total time
dx = 0.0005               # spatial interval( grid interval)
dt = 0.01                 # time interval

x = np.arange(0,L+dx,dx)  # np.arange(start, stop, interval). creating grid points
t = np.arange(0,T+dt, dt) # creating time steps

nx= len(x)                # number of spatial grid points
nt = len(t)               # number of time steps

                          # Diffusion Number
a = 2*10**(-4)
alpha=a*dt/dx**2  # = 0.08

                          # Initial condition

# T=np.zeros(nx,)         # We are taking everywhere at t=0, temperature T=0, And while we take this BC,
                          #take T[0] =10, T[-1]=4 and set axis plt.axis([0,L,0,12])


T = np.sin(2*np.pi*x/L)
T_init=np.copy(T)
                          # Boundary condition

T[0] = 0                  # Temperature at left boundary all the time
T[-1] =0                  # Temperature at right boundary all the time

                          # Creating sparse matrix (Coefficient Matrix)
A = diags([-alpha, 1+2* alpha, -alpha], [-1, 0, 1], shape =(nx-2, nx-2)).toarray()
                          # toarray() returns values in array(Matrix) form.
                          #[-1,0,1] represents [lower diagonal from main diagonal, main diagonal, just upper diagonal]
                          # This uses scipy package

for j in range(nt):       # up to last time step
                          # print("Time t =",t[j],'ms')

    Tn=T                  # copy
    B = Tn[1:-1]          # create matrix of known on the RHS of the equation. [1,-1] means first and last elements are removed(sliced)
    B[0] +=alpha*T[0]     # topmost entry of the RHS vector
    B[-1]+= alpha*T[-1]   # Bottommost entry of the RHS vector
    T[1:-1]=np.linalg.solve(A,B)  #Solution of linear equations(np.linalg.aolve(Coefficient_Matrix, constant_vector_RHS))


                          # -----------------------Plotting------------------------

    plt.figure("Temperature profile", figsize =(5,4))
    plt.clf()
    plt.plot(x,T,color ='yellow')
    plt.plot(x,T_init,'k')# plotting initial temperature profile
    # plt.title( "Temperature Profile (BTCS) of 1D Rod", fontname="Times New Roman Bold")
    plt.xlabel("Grid points (x)", fontsize=10,fontweight='bold')
    plt.ylabel("Temperature (T $^0C$)  ",fontsize =10,fontweight='bold')

    plt.axis([0, L, -1.4,1.4])
    string="Temperature Profile (BTCS Scheme) of 1D Rod" + "\nTime t = " +str(t[j])+"ms"
    plt.suptitle(string,fontweight='bold',style = 'italic' )
    plt.grid()
    plt.show(block=False)  ## Or  plt.draw()
    plt.pause(0.0001)
plt.savefig("Temperature Profile (BTCS) of 1D Rod")
plt.legend()

'''
Description of my code------>

What happens in RHS of Matrix Equation  is :

A is matrix of dimension 79x79 because boundaries are omitted.(Actually there are 81 steps including boundaries)
B is matrix of dimension 79x1.
initial value is at j=0, where temperature is initial Condition(here, T=0).

Basically we have this kind of matrix equations:

                [ T(1,j+1) ]        [ T(1,j) + alpha * T(0,j) ]
                [ T(2,j+1) ]        [        T(2,j)           ]
                [ T(3,j+1) ]        [        T(3,j)           ]
       [A]   x  [ T(4,j+1) ]   =    [        T(4,j)           ]
                    .                           .
                    .                           .
                    .                           .
                [T(i-1,j+1)]        [ T(i-1,j)+ alpha * T(i,j)]

Here,
T(x_step,t_step)
A is the sparse (tri-diagonal)  matrix which we created.
The dimension of the matrix is (nx-2) x (nx-2).(since, Boundaries are omitted)
Boundaries(T(0,j) and T(i,j)) are not included in this matrix. Although they are present
in the topmost and the bottommost entries of the RHS vector.(This is because of BTCS scheme.)
Here Boundaries are left (T(0,j)=10) and right(T(i,j)=0) side of the rod, the values of which are known.
i is the last x_step.

B[0] =B[0] + alpha*T[0]:

T[0] is T(0,0) left Boundary.
B[0] (the one which is in RHS, is in first iteration) = T(1,0), which is initial condition,
because initially(at j = 0 ) every grid point is at initial('known') temperature(here initial condition T(i,0) =0).
This is how our topmost entry of RHS in first iteration is ( T(1,0) + alpha * T(0,0) ) which is known (0+ alpha* 10).

B[-1]= B[-1] + alpha*T[-1]:

T[-1] = T(i,j) Right Boundary.
B[-1] (the one which is present in LHS) = T(i-1,j), which is the temperature at the grid point present one point
before the RHS boundary point(second last grid point).
B[-1](the one which is in LHS) is bottommost entry of the column, which is also known for the first iteration(j=0),
because  B[-1] + alpha*T[-1] = T(i-1,j) + alpha * T(i,j) = T(i-1,0) + alpha * T(i,0) = which is (0 + alpha * 4) here.
Again to remind, this is because in first iteration everywhere, the temperature is known(initial value).

All the entries in between the top and bottom of the column, are initial temperatures at every grid point
(which is T=0 here).

Thus for the first iteration we have got RHS column, which can be represented as

                                           [ T(1,0) +alpha*T(0,0) ]
                                           [          0           ]
                                           [          0           ]
                                                      .
                                                      .
                                                      .
                                           [ T(i-1,0)+alpha*T(i,0)]


Now we can calculate the matrix solution ( linear equations ),
as A is known and the RHS column us also known. Using these for the first iteration ( j=0 ), we can calculate
the LHS unknown column entries, using the last line of code of the for loop ( T[1:-1]=np.linalg.solve(A,B) ).
From the first iteration we find the column, which is basically symbolically depicted as

                                                 [  T(1,1) ]
                                                 [  T(2,1) ]
                                                 [  T(3,1) ]
                                                     .
                                                     .
                                                     .
                                                 [ T(i-1,1)]

We see that the first, second, etc entries of this column will be used for the calculation of RHS column in
the second iteration. For example, the first entry of RHS column in the second iteration is
             T(1,1) + alpha * T(0,1) = T(1,1) + alpha * T(0,0).
(because of the right boundary, where always T = fixed)
second entry is T(2,1) which is already same as LHS so no need of manipulation is required.
Thus at every time step whole temperature profile (at each grid point) can be calculated.


# ------------Plotting--------------
# ------Laasonen Scheme----------------
plt.figure(figsize=(6,3))
plt.plot([0,2],[1,1],'k')
plt.plot([1,1],[0,1],'k')
plt.plot([0,1,2,1],[1,1,1,0],'ko',markersize=10)
plt.text(1.1,0.1,'T[n,j]')
plt.text(0.1,1.1,'T[n+1,j-1]')
plt.text(1.1,1.1,'T[n+1,j]')
plt.text(2.1,1.1,'T[n+1,j+1]')
plt.xlabel('space')
plt.ylabel('time')
plt.axis('equal')
plt.yticks([0.0,1.0],[])
plt.xticks([0.0,1.0],[])
plt.title('Laasonen scheme',fontsize=12)
plt.axis([-0.5,2.5,-0.5,1.5])
plt.show()

'''
