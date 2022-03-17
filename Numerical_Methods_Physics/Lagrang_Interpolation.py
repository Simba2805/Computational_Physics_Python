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
nn=80

xd=(x[n-1]-x[0])/nn

listx=[]  # creating an empty list for x values.


for j in range(nn+1):
    xn=x[0]+j*xd
    listx.append(xn)
print(listx)
p = float(input("Enter the value of the data point p= "))

f=0

for i in range(n):
     y1=1  ## important  Do not put y1 before defining the range for i,
     # otherwise while evaluating the multiplication,
     #  y1 will continue with the next iteration for i after finishing with one i
     for j in range(n):
        if i!=j:
          y1=y1*(p-x[j])/(x[i]-x[j])

     f+=y[i]*y1

# print(y1)
print("Value of the polynomial is = ", f)


