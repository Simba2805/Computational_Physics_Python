import matplotlib.pyplot as plt

import numpy as np

x = float(input("Enter the value of initial point(try 0.1): "))
y = float(input("Enter the value of final point(try 1.3): "))
n = int(input("number of intervals: "))


def simpson_third(x, y, n):
    h = (y - x) / n

    def fun(x):
        return 5 * x * np.exp(-2 * x)

    i = 0
    sum = 0
    #sum=fun(x)+fun(y)
    while i <= n:
        if i == 0:
            sum = sum + fun(x)
        elif i == n:
            sum = sum + fun(y)
        elif i % 2 == 0:
            sum = sum + 2 * fun(x + h * i)
        else:
            sum += 4 * fun(x + h * i)
        i += 1
    return (h / 3) * sum



from scipy.integrate import quad


def integrate(p):
    return 5 * p * np.exp(-2 * p)


exact_value = quad(integrate, 0.1, 1.3)
print(" The true value of integration is ", "%.5f" % exact_value[0])
result_38 = simpson_third(x, y, n)



print(" The value of integration is ", "%.5f" % result_38)


abs_err = ( result_38 - exact_value[0])

print(" error is: ",abs_err)


x = np.linspace(-5, 7, 40)
fun = 5 * x * (np.exp(-2 * x))
plt.plot(x, fun, 'g', label="5x exp(-2*x), range -5:5:40")
plt.xlabel("x")
plt.ylabel("Y")
plt.grid()
plt.title("f(x)= 5x exp(-2x)")
plt.savefig("Trapezoidal.png")
plt.show()
