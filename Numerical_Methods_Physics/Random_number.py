from random import *
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
n =int(input("Enter the total number of points inside the square or cube "))
pi_true=np.pi


def pi_2D(n):
    inpoint1=0
    for i in range(n):
        x=random()
        y= random()
        if sqrt(x*x+y*y)<=1:
            inpoint1+=1

        pi_2D=4*inpoint1/n

    return pi_2D
    # print("number of points inside the sphere are ",inpoint1)
def pi_3D(n):
    inpoint2=0
    for j in range(n):
        x=random()
        y= random()
        z=random()
        if sqrt(x*x+y*y+z*z)<=1:
            inpoint2+=1

        pi_3D=6*inpoint2/n

    return pi_3D
    # print("num+ber of points inside the circle are ",inpoint2)

# print("The difference between actual value and obtained value ",error1)
print("The value of pi from 2D circle is= ",pi_2D(n))
print("-----------------------------------------------------")


# print("The difference between actual value and obtained value ",error2)
print("The value of pi from 3D sphere is= ",pi_3D(n))

list_n=[]
list_err2D=[]
list_err3D=[]

for k in range(7):
    n=pow(10,k)
    err2D=abs(pi_true-pi_2D(n))
    err3D=abs(pi_true-pi_3D(n))
    list_n.append(n)
    list_err2D.append(err2D)
    list_err3D.append(err3D)




plt.plot(list_n,list_err2D,marker="o",label="Variation")
plt.plot(list_n,list_err3D,marker="o",label="Variation")
plt.title(" Deviation from the true value of pi ")
plt.xlabel("n")
plt.ylabel("Error")
plt.legend()
plt.show()
'''
x=range(n)
plt.title("plot between error and points inside the square")
plt.plot(x,listy1)
plt.plot(x,listy2)
plt.xlabel("n")
plt.ylabel("error")
plt.show()
'''