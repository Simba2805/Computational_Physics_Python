import matplotlib.pyplot as plt
import numpy as np
# In this code we can give a prompt value for initial guess
# and also number of iterations
# def forward_diff(x,y):
#
# e=10**(-4)
# a=x
# b=y
#
#  def func(x):
#     return x**3-20
# funa=func(a)
# funb=func(b)
# # print(func(a))
# # print(func(b))
# if abs((b-a)/b)>e:
#     b= b-(funa*(b-a))/(funb-funa)
# return b
#print(forward_diff(0,1))
def newton_rapshon2(fun, p, q, n, e):
    a = p
    b = q
    #i=0
    #while i<n:
    for val in range(0, n):
        funca = fun(a)
        funcb = fun(b)
        if abs(funca) < e:  #                abs((b-a)/b)<e:
            print("Found solution after", val, "iterations")
            return a
        a = a - (funca * (b - a)) / (funcb - funca)
    else:
        print("exceeded maximum iterations")
    return None


fun = lambda x: x ** 3 - 20

result = newton_rapshon2(fun, 2, 3, 20, 10 ** (-4))
print("The value of the root is:", "%.5f" % result)

x = np.linspace(-5, 5, 50)
f = x ** 3 - 20

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#plot the function
plt.plot(x, f, 'g', label='f(x)=x^3-20')

plt.xlabel('x')  # naming the x axis
plt.ylabel('f(x)')  # naming the y axis

# giving a title to my graph
plt.legend(loc='upper left')
#plt.title('f(x)=x^3-20')
plt.savefig("Newton_raphson2.png")
plt.show()

