## Trapezoidal Method

y=1
x=0
n=1000
h = (y - x) / n
def fun(x):
    return x**2

sum = (fun(x) + fun(y))

i = 1
while i < n:
    sum = sum + 2 * fun(x + h * i)
    i += 1
    result= sum * (h / 2)

print("Using Trapezoidal method = ",result)
#random number integration(average or summation)
from random import *

def f(x):
    return x**2
n=1000
sum=0
for i in range(n):
    x=random()

    sum+=f(x)
    integrate=sum
result_rand=integrate/n
print("Using random number generation = ",result_rand)
