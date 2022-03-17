print("-----Gauss-Jordan Elimination-----")

## in this method we transform our nxn matrix to a identity matrix and then don't need to do back substitution

import numpy as np

a=np.array([[1,3,2],
            [2,7,7],
            [2,5,2]],float)
b=np.array([2,-1,7],float)
# a= np.array([[1,3,-2,4],
#              [2,6,0,5],
#              [4,11,8,0],
#              [1,3,2,1]],float)
# b=np.array([7,5,7,-2],float)
n= len(b)

## if there is zero or negligible element on the main diagonal, then code for interchanging the rows
for k in range(n):
    if abs(a[k,k])<1.0e-10:
        for i in range(k+1,n):
            if abs(a[i,k])>abs(a[k,k]): # We can also write abs(a[k,k])=1.0e-10 because we are looking for non zero element on the main diagonal
                a[[k,i]]=a[[i,k]] ## changeing rows of matrix
                b[i,k]=b[k,i]## changeing elements in the RHS constant vector
                ##Or
                # for j in range(k,n):
                #     a[k,j],a[i,j]=a[i,j],a[k,j]
                # b[k],b[i]=b[i],b[k]

                break

    for l in range(n):
        a[k,:]=a[k,:]/a[k,k]
    b[k]=b[k]/a[k,k]

    # #Or
    # for k in range(n):
    #     pivot= a[k,k]
        # for l in range(n):
        #     a[k,l]=a[k,l]/pivot
        # b[k]=b[k]/pivot

    for i in range(n):
        # b[k],b[i]=b[i],b[k]
        if i==k or a[i,k]==0: ##we skip that row if there is zero and also i==k element(diagonal element) because we have already set that to 1.
            continue

        factor =a[i,k] ## we have to predefine the factor, because in every iteration it changes.(although sometimes it doesn't matter)
        b[i] -= b[k]*factor ## we can define this vector also after the j loop.
        for j in range(k,n):
            a[i,j]-= factor * a[k,j]



print("Transformed Identity matrix: ")
print(a)

print("The solution vector is: ")
print(b)