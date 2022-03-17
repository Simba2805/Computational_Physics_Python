print("-----------------LU-Decomposition-------------------")

import numpy as np
'''

###Important note:::: when you change the matrix from another matrix then also change 'c'(which is 'b') vector
#which is defined later, after creating upper triangular matrix.


a=np.array([[20,15,10],
            [-3,-2.249,7],
            [5,1,3]],float)
b=np.array([45,1.751,9],float)
'''
a=np.array([[25,5,1],
            [64,8,1],
            [144,12,1]],float)
b=np.array([106.8,177.2,279.2],float)

n =len(b)
z=np.zeros(n,float)
x= np.zeros(n,float)  ## solution vector
L=np.eye(n,n)  ## creating identity matrix
# print(L)


### Partial Pivoting
for k in range(n-1):
    if abs(a[k,k])<1.0e-10:
        for j in range(k+1,n):
            if abs(a[j,k])>abs(a[k,k]):
                a[[j,k]]=a[[k,j]]
                b[[j,k]]=b[[k,j]]
                break

#Elimination:

            ## creating upper(U) and lower triangular(L) matrices----------->
    for i in range(k+1,n):
        if a[i,k]==0:
            continue

        factor = a[i,k]/a[k,k] ## creating factor so that we can create a upper triangular matrix
        L[i,k]=factor  ## creating lower triangular matrix

        for j in range(k,n):
            a[i,j]= a[i,j]- a[k,j]*factor
        # b[i]=b[k]-b[i]*factor
## upper triangular matrix U
#print("--------------------------------------------")
U=a

print("Upper triangular matrix is U: ")
print(U)

print("--------------------------------------------")
print("Lower Triangular matrix is L: ")
print(L)


c=np.array([106.8,177.2,279.2],float)
print("\n")
## here I am creating the same vector b with
#  different name because we changed above the b vector.
print("--------------------------------------------")

### upper triangular matrix
## Forward Substitution
z[0]=b[0]/L[0,0]  ## or z[0]=b[0] because L[0,0]=1
# print(z)
for i in range(1,n):
    sum_Lz=0
    for m in range(0,i):
        sum_Lz+=L[i,m]*z[m]
        # print(sum_Lz)
    z[i]=(c[i]-sum_Lz)/L[i,i]  ##L[i,i]=1
print("z vector from forward substitution: ")
print("z := ",z)

print("\n")
print("------------------Solution vector from LU-Decomposition--------------------------")

## Back-Substitution on upper triangular matrix to get solution vector
## here z vector will be used as constant Right hand vector
x[n-1]= z[n-1]/U[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_Ux=0
    for j in range(i+1,n):
        sum_Ux+=U[i,j]*x[j]
    x[i]=(z[i]-sum_Ux)/U[i,i]

print("\n")

print("The value of solution vector is: ")
print("x := ", x)


##we can compare this result with Gauss-Elimination method

print("\n")


print("------------------ Comparison with Gauss-Elimination Method-----------------\n")


a=np.array([[25,5,1],
        [64,8,1],
        [144,12,1]],float)
b=np.array([106.8,177,279.2],float)
## length of the vector
n= len(b)
# defining zeros to fill the entries of x
x= np.zeros(n,float)
##

## --------------Partial Pivoting---------------

for k in range(n-1):
    if abs(a[k,k])<1.0e-10:
        for i in range(k+1, n):  ### I have to check here what if i take n instead of (n-1), can we interchange the pivot row with the last row.
            if abs(a[i,k])> abs(a[k,k]):### it doesn't matter whether we take n or n-1in the previous range
                a[[i,k]]=a[[k,i]]
                b[[k,i]]=b[[i,k]]
                break


    # Elimination---->
### note: here I am using different  factor than I used in gauss Elimination method (factor= a[i,k]/a[k,k])
    #for k in range(n-1):
    for i in range(k+1,n):
        if a[i,k]==0:
            continue
        factor= a[i,k]/a[k,k]
        for j in range(k,n):
            a[i,j]= a[i,j]- a[k,j]*factor
        b[i]=b[i]-b[k]*factor
# print(a)
## back-Substitution---->

x[n-1]= b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax=0
    for j in range(i+1,n):
        sum_ax+=a[i,j]*x[j]
    x[i]= (b[i]-sum_ax)/a[i,i]

print("x:= ", x)