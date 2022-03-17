import matplotlib.pyplot as plt
import numpy as np

def newton_raphson(function, function1, x_initial, iteration, e):

###   -------Only for function  : (x**3-20)------

##  In this code we can give a prompt value for initial guess
## and also number of iterations
#e=10**(-4)
# def function(x):
#      return x**3-20
# def function1(x):
#      return 3*x**2
# x_initial =int(input("Enter Initial Value: "))
# iteration = int(input("Enter number of iteration: "))
# x_old=100
# for val in range(0,iteration):
#     if function(x_initial)-function(x_old)<e:
#          x_initial=x_initial-function(x_initial)/function1(x_initial)
#          print("%.5f" % round(x_initial,5))
#     elif function1(x_initial)==0:
#          print("roots cannot be found")
#     else:
#          print("Exceeded number of iterations")

   x =  x_initial
   for val in range(0,iteration):

        func=function(x)
        if abs(func)< e:
            print("Found solution after", val, "iterations")
            return  x
        Df= function1(x)
        if Df ==0:  # if derivative is zero
            print("No solution, Derivative is zero")
            return  None
        x=x-func/Df

   else:
        print("exceeded maximum iterations")
   return None
### Choices for functions

print("(a): x^(1/3)")
print("(b): x^3-20 ")
print("(c): 1-x**2 ")

## ask for choice of function (choices are (a), (b), (c))

choice =input("Choose function whose root you want to find: ")

##--------------First function----------
if choice== "a":
  #print("(a): x^(1/3)")
  function =lambda x:  x**(1/3)
  function1 = lambda x :(1/3)*x**(-2/3)
  result= newton_raphson(function, function1,1,12,10**(-4))
  print(result)

  ##-------------plotting-------------
  x = np.linspace(0,5,50)
  f= x**(1/3)

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')

  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
#plot the function
  plt.plot(x, f,'g', label = 'f(x)= x^(1/3)')


  plt.xlabel('x') # naming the x axis
  plt.ylabel('f(x)')# naming the y axis

# giving a title to my graph
  plt.legend(loc='upper left')
    #plt.title('f(x)=x^3-20')

  plt.show()

##--------------Second function----------

elif choice=="b":
  #print("(b): x**3-20 ")
  function =lambda x: x**3-20
  function1 = lambda x :3*x**2
  result= newton_raphson(function, function1,2,12,10**(-4))
  print("Root for the function x^3-20 is " +"%.6f" % round(result,6))

  ##-------------plotting-------------
  x = np.linspace(-5,5,50)
  f=x**3-20

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
#plot the function
  plt.plot(x, f,'b', label = 'f(x)=x^3-20')


  plt.xlabel('x') # naming the x axis
  plt.ylabel('f(x)')# naming the y axis

# giving a title to my graph
  plt.legend(loc='upper left')
    #plt.title('f(x)=x^3-20')

  plt.show()

  ##--------------Third function------------
else:
  #print("(c): 1-x**2 ")
  function =lambda x:  1-x**2
  function1 = lambda x :-2*x
  result= newton_raphson(function, function1,0,12,10**(-4))
  print(result)

   ##-------------plotting-------------

  x = np.linspace(-5,5,50)
  f=1-x**2

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
#plot the function
  plt.plot(x, f,'c', label = 'f(x)=1-x**2')


  plt.xlabel('x') # naming the x axis
  plt.ylabel('f(x)')# naming the y axis

# giving a title to my graph
  plt.legend(loc='upper left')
    #plt.title('f(x)=x^3-20')

  plt.show()