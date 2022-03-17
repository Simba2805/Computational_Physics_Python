import numpy as np
import time

##------------ exact value of the integration -----------


### _--------------Simpson's 3/8 rule -----------------
startTime = time.time()
x = float(input("Enter the value of initial point(try 0.1): "))
y = float(input("Enter the value of final point(try 1.3): "))
n = int(input("number of intervals: "))


def simpson_third(x, y, n):
    h = (y - x) / n

    def fun(x):
        return 5 * x * np.exp(-2 * x)

    i = 0
    sum = 0
    # sum=fun(x)+fun(y)
    while i <= n:
        if i == 0:
            sum = sum + fun(x)
        elif i == n:
            sum = sum + fun(y)
        elif i % 3 == 0:
            sum = sum + 2 * fun(x + h * i)
        else:
            sum += 3 * fun(x + h * i)
        i += 1
    #print("Number of iterations: ", n)
    return (3 * h / 8) * sum


from scipy.integrate import quad


def integrate(p):
    return 5 * p * np.exp(-2 * p)


exact_value = quad(integrate, 0.1, 1.3)
print(" The true value of integration is ", "%.5f" %exact_value[0])

simpson = simpson_third(x, y, n)
# abs_error = (result-exact_value)
#
# while n>np.log((y-x)/abs_error)/np.log(2)-1:
# print(n)
print(" The value of integration is ", "%.5f" % simpson)
abs_err = ( simpson - exact_value[0])
# print(" Error is: " , "%.5f"% abs_err)
print(" error is: ",abs_err)
# print(abs_error)
endTime = time.time()
totalTime = endTime - startTime

print("Total time taken to execute code is= ", totalTime)