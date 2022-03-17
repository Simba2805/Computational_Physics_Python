import matplotlib.pyplot as plt
import numpy as np
#
x_0 = int(input("Enter the initial value of x (try 0): "))
y_0 = int(input("Enter the initial value of y (try 0): "))
t=float(input("Enter the value of x at which we want the value of y(try 1.2): "))
h= float(input("Enter the value of interval h(0.1 or 0.01 or 0.001): "))
def euler_method(x_0, y_0, h, t):  ## t is final point where we want the value of function
 x=x_0
 y=y_0
 def fun(x,y):
     return x+2*y                                                   # return 3*np.exp(-x)-0.4*y
                                                        #   #return (x + y + x * y)



## make lists to store values
 lsty=[]  # y data points which we get numerically
 lstx=[]  # x data points which we get numerically
 while x < t:  # here t is final point
   y+=fun(x,y)*h
   lsty.append(y)
   x=x+h
   lstx.append(x)

 print("Approximate solution at x = ", int(x), " is ", "%.6f"% y)
 print("The number of iterations are n = ",int((x-x_0)/h+1))
   # print(list[y], end=" ")
 # print (lstx)
 # print (lsty)

 ## --------------Plotting------------------------
 ## ----------Numerical plot----------------------

 ## for interval h=0.1-->
 if h==0.1:
  # plt.subplot(1,3,1)
  plt.plot(lstx,lsty,'-r',label ="Numerical curve")
  ##---------- functional plot---------------------
  xp= np.linspace(0,1.2,12)
  f=0.25*np.exp(2*xp) - 0.5*xp-0.25

  plt.plot(xp,f, 'c', label="Functional curve")
  plt.savefig("Euler_Method_h_0.1.png")
  plt.grid()
  plt.legend()
  plt.title("h=0.1")
  plt.show()


 ### for interval h=0.01--->
 elif h==0.01:
  # plt.subplot(1,3,2)
  plt.plot(lstx,lsty,'-r',label ="Numerical curve")
  xp= np.linspace(0,1.2,121)
  f=0.25*np.exp(2*xp) - 0.5*xp-0.25
  plt.plot(xp,f, 'c', label="Functional curve")
  plt.savefig("Euler_Method_h_0.01.png")
  plt.grid()
  plt.legend()
  plt.title("h=0.01")
  plt.show()



 # for interval h=0.001--->
 elif h==0.001:
  # plt.subplot(1,3,3)
  plt.plot(lstx,lsty,'-r',label ="Numerical Euler method curve")
  xp= np.linspace(0,1.2,1201)
  f=0.25*np.exp(2*xp) - 0.5*xp-0.25
  plt.plot(xp,f, 'c', label="Functional curve")
  plt.title("h=0.001")
  plt.savefig("Euler_Method_h_0.001.png")
  plt.grid()
  plt.legend()
  plt.show()

euler_method(x_0,y_0,h,t)
#euler_method(0,1,0.025,.1)

##----------plotting -------------

def f(x):
    return 0.25*np.exp(2*x) - 0.5*x-0.25
print ("The exact value is ", f(1.2))


#x= np.linspace(0,1.2,121)
# f=0.25*np.exp(2*x) - 0.5*x-0.25
# plt.plot(x,f,lstx,lsty)
# plt.xlabel('x')  # naming the x axis
# plt.ylabel('f(x)')  # naming the y axis
# plt.show()
