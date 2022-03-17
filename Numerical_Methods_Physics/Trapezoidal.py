# import math

import matplotlib.pyplot as plt
import numpy as np

# def Trapezoidal( x,y,n):
#
# a=x
# b=y
# h=(b-a)/n
#
#  def fun(x):
#      return (1 / (1 + x * x))
#  sum = (fun(a)+fun(b))
#
#  i=1
#  while i<n:
#     sum =sum +2*fun(a+h*i)
#     i+=1
#  return sum*(h/2)
# #fun = lambda x: (1 / (1 + x * x))
# result =Trapezoidal( 0,1,6)
# print(result)
'''
def Trapezoidal(fun, x,y,n):

 a=x
 b=y
 h=(b-a)/n

 # def fun(x):
 #     return (1 / (1 + x * x))
 sum = (fun(a)+fun(b))

 i=1
 while i<n:
    sum =sum +2*fun(a+h*i)
    i+=1
 return sum*(h/2)
fun = lambda x: (1 / (1 + x * x))
result =Trapezoidal(fun, 0,1,6)
print(result)


'''
x = float(input("Enter the value of initial point(try 0.1): "))
y = float(input("Enter the value of final point(try 1.3): "))
n = int(input("number of intervals: "))


def Trapezoidal(x, y, n):
    h = (y - x) / n

    def fun(x):
        return 5 * x * np.exp(-2 * x)

    sum = (fun(x) + fun(y))

    i = 1
    while i < n:
        sum = sum + 2 * fun(x + h * i)
        i += 1
    return sum * (h / 2)

    #fun = lambda x: (1 / (1 + x * x))


result = Trapezoidal(x, y, n)
print("The root is: ", " %.5f" % result)  ###--------------Plotting----------------


x = np.linspace(-5, 7, 40)
fun = 5 * x * (np.exp(-2 * x))
plt.plot(x, fun, 'g', label="5x exp(-2*x), range -5:5:40")
plt.xlabel("x")
plt.ylabel("Y")
plt.grid()
plt.title("f(x)= 5x exp(-2x)")
plt.savefig("Trapezoidal.png")
plt.show()



