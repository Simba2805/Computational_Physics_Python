
import numpy as np

n= int(input("Number of points(order) (Enter between 1 to 6): "))
xi= int(input("Initial value of integration: "))
xf= int(input("Upper limit of integration: " ))
def guass_Quadrature(xi,xf,n):



    def f1(z):
        return 5 * z * np.exp(-2 * z)


    # def f2(z):
    #    return z ** 6 - 7 * z ^ 3


    def f3(z):
        return (xf-xi)/2*(f1((xf+xi)/2+z*(xf-xi)/2))

    y=0
    if n==1:
        w=[2]
        x=[0]

    elif n==2:
        w=[1.0000000000000000,1.0000000000000000]
        x=[-0.5773502691896257,0.5773502691896257]
        # for i in range(0,2):
        #    y+=w[i]*f1(x[i])
        # print(y)
    elif n==3:
        w=[0.8888888888888888,0.5555555555555556,0.5555555555555556]
        x=[0.0000000000000000,-0.7745966692414834,0.7745966692414834]
        # for i in range(0,3):
        #    y+=w[i]*f1(x[i])
        # print(y)

    elif n==4:
        w=[0.6521451548625461,0.6521451548625461,0.3478548451374538,0.3478548451374538]
        x=[-0.3399810435848563,0.3399810435848563,-0.8611363115940526,0.8611363115940526]
        # for i in range(0,4):
        #    y+=w[i]*f1(x[i])
        # print(y)

    elif n==5:
        w=[0.5688888888888889,0.4786286704993665,0.4786286704993665,0.2369268850561891,0.2369268850561891]
        x=[0.0000000000000000,-0.5384693101056831,0.5384693101056831,-0.9061798459386640,0.9061798459386640]
        # for i in range(0,5):
        #    y+=w[i]*f1(x[i])
        # print(y)

    elif n==6:
        w=[0.3607615730481386,0.3607615730481386,0.4679139345726910,0.4679139345726910,0.1713244923791704,0.1713244923791704]
        x=[0.6612093864662645,0.6612093864662645,0.2386191860831969,-0.2386191860831969,0.9324695142031521,-0.9324695142031521]
        # for i in range(0,6):
        #    y+=w[i]*f1(x[i])
        # print(y)


    else:
        print("invalid number of input")


    y=0
    if xi==-1 and xf ==1:
        for i in range(0,n):
            y+=(w[i]*f1(x[i]))
        print("The value of integration is: ",y)
    else:
        for i in range(0,n):
            y+=w[i]*f3(x[i])
        print("The value of integration is: ",y)


print(guass_Quadrature(xi,xf,n))
