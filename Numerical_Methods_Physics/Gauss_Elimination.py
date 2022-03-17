# #from numpy import array, zeros
# from array import *
import numpy as np
#from numpy import fabs

'''
a=np.array([[25,5,1],
        [64,8,1],
        [144,12,1]],float)
b=[106.8,177,279.2]
n= len(b)
x= np.zeros(n,float)

# Elimination
for k in range(n - 1):
    for i in range(k + 1, n):
        if a[i, k] == 0:
            continue
        factor = a[k, k] / a[i, k]
        for j in range(k, n):
            a[i, j] = a[k, j] - a[i, j] * factor
        b[i] = b[k] - b[i] * factor
print(a)

print(b)

# Back-Substitution
x[n - 1] = b[n - 1] / a[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    sum_ax = 0
    for j in range(i + 1, n):
        sum_ax += a[i, j] * x[j]
    x[i] = (b[i] - sum_ax) / a[i, i]

print(x)
'''

### Gauss Elimination Method with Partial Pivoting
##3 defining array
## Coefficient Matrix
'''
a= np.array([[0,7,-1,3,1],
             [0,3,4,1,7],
             [6,2,0,2,-1],
             [2,1,2,0,2],
             [3,4,1,-2,1]],float)
## Constant vector
b = np.array([5,7,2,3,4],float)
'''
'''
a=np.array([[25,5,1],
        [64,8,1],
        [144,12,1]],float)
b=np.array([106.8,177,279.2],float)
'''
a=np.array([[20,15,10],
            [-3,-2.249,7],
            [5,1,3]],float)
b=np.array([45,1.751,9],float)

## length of the vector
n= len(b)
# defining zeros to fill the entries of x
x= np.zeros(n,float)
##

## --------------Partial Pivoting---------------
## if there is zero on the main diagonal the we have to interchange the row with another row which has greater value then zero
for k in range(n-1):
    if abs(a[k,k])<1.0e-10:
        for i in range(k+1, n):  ### I have to check here what if i take n instead of (n-1), can we interchange the pivot row with the last row.
            if abs(a[i,k])> abs(a[k,k]): #we can also write (1.0e-10) instead of a([k,k])### it doesn't matter whether we take n or n-1in the previous range.
                a[[i,k]]=a[[k,i]]
                b[[k,i]]=b[[i,k]]
                break


    # Elimination---->

    #for k in range(n-1):
    for i in range(k+1,n):
        if a[i,k]==0:
            continue
        factor= a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j]= a[k,j]- a[i,j]*factor
        b[i]=b[k]-b[i]*factor
print("the upper triangular matrix ")
U=a
print(np.round(U,1))
## back-Substitution---->

x[n-1]= b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax=0
    for j in range(i+1,n):
        sum_ax+=a[i,j]*x[j]
    x[i]= (b[i]-sum_ax)/a[i,i]

print("The solution vector is: ")
print(np.round(x,1))
