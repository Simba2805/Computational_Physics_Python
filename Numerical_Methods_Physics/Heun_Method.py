###-------------------- Runge-Kutta 2 Method----------------

import matplotlib.pyplot as plt
import numpy as np
import time
startTime = time.time()
x0 = int(input("x0= Enter the initial value of x (try 0): "))
y0 = int(input("y0= Enter the initial value of y (try 0): "))
t=float(input("t= Enter the value of x at which we want the value of y(try 1.2): "))
h= float(input("h= Enter the value of interval h(0.1 or 0.01 or 0.001): "))
def heun_method(x0,y0,h,t):
    # t = 1.2  ## value at which we want to calculate the differential equation
    # y = y0## initial value of x
    # h = 0.1  # interval

    x = x0
    y=y0
    # h=0.1
    def fun(x, y):
        return x + 2 * y

    x1 = 0
    y1 = 0
    xlist = []  ## creating x-axis data list for Runge-Kutta2
    ylist = [] ## creating y-axis data list for Runge-Kutta2
    lsty = []  # y data points which we get numerically for Euler Method
    lstx = []  # x data points which we get numerically for Euler method

    ## creating list for Runge kutta (Explicit mid Point method)----->
    x2=0
    y2=0
    xlist2=[]
    ylist2=[]

     ## creating list for Ralston Method ----->
    x3=0
    y3=0
    xlist3=[]
    ylist3=[]


    while x < t:
        s1 = fun(x, y)
        s2 = fun(x + h, y + s1 * h)
        x += h
        y += h * (s1 + s2) / 2
        ylist.append(y)

        xlist.append(x)

        # ------------Comparing with Euler Method----------

        y1 += fun(x1, y1) * h
        lsty.append(y1)
        x1 = x1 + h
        lstx.append(x1)

        #------------Comparing with Ralston Method----------

        s6= fun(x3,y3)
        s7= fun(x3+2*h/3,y3+s6*h/3)
        x3+=h
        y3 += h*(s6+3*s7)/4
        xlist3.append(x3)
        ylist3.append(y3)

        ## -----------------explicit Mid-Point Method

        s5=fun(x2,y2)
        y2 += h*fun(x2+h/2,y2+s5*h/2)
        x2 += h
        xlist2.append(x2)
        ylist2.append(y2)
    print("The approximate solution at x= ", x, " using Heun's Method is ", y)
    print("The approximate solution at x= ", x, " using Euler Method is ", y1)

    print("The approximate solution at x= ", x, " using Explicit Mid-Point Method is ", y2)


    print("the approximate solution at x= ",x, " using Ralston Method is ", y3)
    # print("The approximate solution at ", x, " RK-2 Method is ", y, " and using Euler Method is ", y1," using Runge-Kutta Explicit Mid point Method ", y2)
    plt.plot(xlist, ylist, '-r', label="Heun's Method")
    plt.plot(lstx, lsty, 'b', label="Euler Method")
    plt.plot(xlist2,ylist2,label ="RK-4, Mid_point_method")
    plt.plot(xlist3,ylist3,label ="Ralston_method")

 #### ---------------- Analytic plotting ------------------


    xp = np.linspace(0, 1.2, 12)
    f = 0.25 * np.exp(2 * xp) - 0.5 * xp - 0.25
    plt.plot(xp, f, '+c', label="Analytic curve")
    plt.savefig("Runge_Kutta2_Heun_method.png")
    plt.grid()
    plt.legend()
    plt.title("h=0.1,There is just slight difference b/w RK2 and analytic curve")
    plt.show()
endTime=time.time()
totalTime = endTime - startTime

print("Total time taken to execute code is= ", totalTime," s")
heun_method(0,0,0.1,1.2)
