import matplotlib.pyplot as plt
import numpy as np


def Bisection(func, x, y, n):
    ## func= function,
    ## x,y = teo guess points
    ## n= number of iterations


    if func(x) * func(y) >= 0:
        print("Wrong Input")
        return
    a = x  ### First point
    b = y  ## second point
    for N in range(0, n):
        z = (a + b) / 2
        if func(a) * func(z) < 0:  ### condition where root is available
            b = z
            # a=a
        else:  # func(z)*func(b)<0:
            #b=b
            a = z
            # elif func(z)==0:
            #      print("Found exact solution, root= ", z)
            #     #return z
            # else:
            #     print("Bisection Method fails")
            #     #return None
    print("Found exact solution, root is = " + str(z))


## ---------Functions of which we want to find the roots--------
print("(a): x^3-20 ")
print("(b): (2*x-1)*(x-3) ")


## -----------choice for the function--------------
choice = input("Enter the choice for function (a) or (b): ")


### finding roots

# -----------First function--------------

if choice == "a":
    func = lambda x: x ** 3 - 20
    x = int(input("Enter Upper limit(try 3): "))  ##give 3
    y = int(input("Enter Lower Limit (try 2): "))  ## give 2
    result = Bisection(func, x, y, 25)
    print(result)

    ##---------------Plotting--------


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

    plt.show()


#------------Next Function---------
else:
    func = lambda x: (2 * x - 1) * (x - 3)
    x = float(input("Enter Upper limit (try 0): "))  ##give 0
    y = float(input("Enter Lower Limit (try 0.9): "))  ## give 0.9
    result = Bisection(func, x, y, 25)
    print(result)  ## Exact answer is 0.5


    ###------------Plotting-------------


    x = np.linspace(-5, 5, 50)
    f = (2 * x - 1) * (x - 3)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    #plot the function
    plt.plot(x, f, 'c', label='f(x)=(2x-1)(x-3)')

    plt.xlabel('x')  # naming the x axis
    plt.ylabel('f(x)')  # naming the y axis

    # giving a title to my graph
    plt.legend(loc='upper left')
    #plt.title('f(x)=x^3-20')

    plt.show()
