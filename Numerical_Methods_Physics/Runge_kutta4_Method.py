## Runge-Kutta-4 Method

import matplotlib.pyplot as plt
import numpy as np

x0 = int(input("x0 = Enter the initial value of x (try 0): "))
y0 = int(input("y0 = Enter the initial value of y (try 0): "))
t=float(input("t = Enter the value of x at which we want the value of y(try 1.2): "))
h= float(input("h = Enter the value of interval h(0.1 or 0.01 or 0.001): "))
def runge_kutta4(x0,y0,h,t):
    x=x0
    y=y0

    def fun(x,y):
        return x+2*y

    ## creating list for runge kutta-2 (Heun's Method)------>
    xlist=[]
    ylist=[]

    ## creating list for Euler Method ----->
    x1=0
    y1=0
    lsty=[]  # y data points which we get numerically
    lstx=[]  # x data points which we get numerically

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


    while x<t:
        s1= fun(x,y)
        s2 = fun(x+h/2,y+s1*h/2)
        s3 = fun(x+h/2,y+s2*h/2)
        s4 = fun(x+h,y+s3*h)
        s=(s1+2*s2+2*s3+s4)/6
        y += h*s
        ylist.append(y)
        x+=h
        xlist.append(x)

        ## -----------------explicit Mid-Point Method

        s5=fun(x2,y2)
        y2 += h*fun(x2+h/2,y2+s5*h/2)
        x2 += h
        xlist2.append(x2)
        ylist2.append(y2)

        #------------Comparing with Ralston Method----------

        s6= fun(x3,y3)
        s7= fun(x3+2*h/3,y3+s6*h/3)
        x3+=h
        y3 += h*(s6+3*s7)/4
        xlist3.append(x3)
        ylist3.append(y3)

        #------------Comparing with Euler Method----------

        y1+=fun(x1,y1)*h
        lsty.append(y1)
        x1=x1+h
        lstx.append(x1)


    print("The approximate solution at x= ", x, " using RK-2 Method is ", y)
    print("The approximate solution at x= ", x, " using Euler Method is ", y1)

    print("The approximate solution at x= ", x, " using Explicit Mid-Point Method is ", y2)


    print("the approximate solution at x= ",x, " using Ralston Method is ", y3)
    plt.plot(xlist,ylist,'r',label ="RK-4")
    plt.plot(xlist2,ylist2,label ="RK-4, Mid_point_method")
    plt.plot(xlist3,ylist3,label ="Ralston_method")
    plt.plot(lstx,lsty,'b',label ="Euler Method")

    ### -------------Analytic curve--------------

    xp = np.linspace(0, 1.2, 12)
    f = 0.25 * np.exp(2 * xp) - 0.5 * xp - 0.25
    plt.plot(xp, f, '*c', label="Analytic curve")
    plt.savefig("Runge_Kutta4.png")
    # plt.title("RK$ curve almost exactly coincides with functional curve")
    plt.grid()
    plt.legend()
    plt.title("h=0.1, RK4 and Mid_point curve curve almost exactly coincides with Analytic curve")
    plt.show()
runge_kutta4(x0,y0,h,t)