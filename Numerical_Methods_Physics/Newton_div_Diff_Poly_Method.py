
import matplotlib.pyplot as plt
'''
import numpy as np
x=np.array([10,15,20,22.5,30],float)
y=np.array([227.04,362.78,517.35,602.97,901.67],float)

# plt.plot(x,y)
# plt.show()

x1=[-1,0,1,2]
y1=[3,-4,5,6]
plt.plot(x1,y1)
plt.show()
x2=[1,2,3,4,5,6,7]
y2=[-1.5,-1,0.5,0.25,1,1.65,2.5]
plt.plot(x2,y2)
# plt.show()
plt.show()
'''

'''
n=len(x)
# p=np.zeros([n,5])
p=np.zeros([n,n+1])
# p[:,0]=y

nk=60
xi=0
xf=30

xdiff=(xf-xi)/nk


for i in range(n):
     # for i in range(n):
        p[i,0]=x[i]
        p[i,1]=y[i]
# print(p)
'''
'''

## If you want to use this piece of code for creating the table for NDDP
##then use 1 instead of 2 while defining k and also remove  p[i,0]=x[i] above.
# print(p)
for l in range(n):
    for k in range(2,n-l):
        p[l,k]=(p[l+1,k-1]-p[l,k-1])/(x[l+1]-x[l])
'''
'''
for i in range(2,n+1): #column
  for j in range(n+1-i):# defines row
    p[j,i]=(p[j+1,i-1]-p[j,i-1])/(x[j+i-1]-x[j])

'''
'''
b=p[0][1:n+1]
m=len(b)
l=len(x)
# x_new=x[0:n+1]
def product(l,value,x):

    prod=1
    for k in range(l):
        prod= prod*(value-x[k])

        return prod


def fun(value):

    f =b[0]

    for i in range(1,m):

        f+=b[i]*(value-x[i-1])
        return f
# print("Newton divided difference tree table is ")
np.set_printoptions(suppress=True)
# print(p)
  ## b contains all the differences b0,b1,b2,b3(these are unknown coefficients)
print("The coefficients' vector is ")
print(b)

print(product(4,20,x))


# print(b)
# value=float(input("Enter the value of data point "))



# func= fun(value)
# print("The value of the function at ", value, " is", fun(20))
print(y)
print(fun(20))

'''
## Newton Divided Difference Polynomial Interpolation Method

import numpy as np
a = input("Enter the choice of array(input a or b or c): ")
if a=='a':
  x=np.array([10,15,20,22.5,30],float)
  y=np.array([227.04,362.78,517.35,602.97,901.67],float)
elif a=='b':
  x=np.array([-1,0,1,2],float)
  y=np.array([3,-4,5,6],float)
elif a=='c':
  x=np.array([1,2,2.5,3,4,4.5,5],float)
  y=np.array([-1.5,-1,0.5,0.25,1,4.5,5],float)
else:
  print("Array Doesn't exist!")

n=len(x)

p=np.zeros([n,n+1])#creating a Tree table (n x n+1 array)
value =float(input("Enter the point at which you want to calculate the value of the polynomial: "))
# first two columns of the table are filled with x and y data points
for i in range(n):

        p[i,0]=x[i]
        p[i,1]=y[i]

## algorithm for tree table from column 2 two n+1
for i in range(2,n+1): #column
  for j in range(n+1-i):# defines row
    p[j,i]=(p[j+1,i-1]-p[j,i-1])/(x[j+i-1]-x[j])#Tree Table
np.set_printoptions(suppress=True)## this suppress the scientific symbol(e) and returns values in normal digits
print("Newton Divided Difference Tree Table")
print(p)

# print(p) ## can check the complete Tree table here for NDDP
print("----------------------------------")
print("Coefficients of the polynomial are: ")
b=p[0][1:]#This vector contains the unknown coefficients in the polynomial which are the top elements of each column.
print("Coefficient vector= ",b)
print("Data points: ")
print("x= ",x)
print("------------------------------------")
lst=[] # list where we will append the values of prouct terms

t=1
for i in range(len(x)):
    t*=(value-x[i]) ##(x-x0), (x-x0)(x-x1), (x-x0)(x-x1)(x-x2) etc..
    lst.append(t)
print("The list of product elements: ",lst)
## creating a general function

f=b[0]
for k in range(1,len(b)):
  f+=b[k]*lst[k-1] ## important**[k-1]** not k because in list we use one step earlier element.
  # For example for b1 we have to use (x-x0), for b2, we use (x-x0)(x-x1) for b3 we use (x-x0)(x-x1)(x2)
print("\nThe value of polynomial at ",value," of data set ",a,"is: ","%.2f"%f)


'''
def polynomial(value):

    coef=b[0]

    for k in range(len(b)):
        coef+=b[k-1]*(value-x[k-1])
    return coef
print(polynomial(value))


'''

def polynomial(value):
    n=len(x)
    coef=b[n-1]
    for i in range(n-1,-1,-1):
        coef=coef*(value-x[i])+b[i]
    return coef

print(polynomial((5)))

##---------Plotting-----------
from shapely.geometry import LineString
# x=np.array([10,15,20,22.5,30],float)
x_axis=np.linspace(max(x), min(x),100)
y_axis=polynomial(x_axis)
# plt.subplot()
plt.plot(x_axis,y_axis, 'k',label="Interpolation")
plt.title("Newton's Divided Difference Polynomial Interpolation")
plt.plot(x,y,'c', label="Given Data-set")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc='best')

##this is for marking the points of intersection
first_line = LineString(np.column_stack((x_axis, y_axis)))
second_line = LineString(np.column_stack((x, y)))
intersection = first_line.intersection(second_line)
plt.plot(*LineString(intersection).xy, 'o')

plt.show()
'''
## Another method of creating the tree table
import numpy as np
x=np.array([10,15,20,22.5,30],float)
y=np.array([227.04,362.78,517.35,602.97,901.67],float)
n=len(x)

p=np.zeros([n,n])
p[:,0]=y

np.set_printoptions(suppress=True)
# print(p)

for i in range(1,n):
  for j in range(n-i):
    p[j,i]=(p[j+1,i-1]-p[j,i-1])/(x[j+i]-x[j])
print(p)
'''