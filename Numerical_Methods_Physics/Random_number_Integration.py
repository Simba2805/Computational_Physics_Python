from random import *
# from random import randint
import numpy as np

sum=0
n=1000
for i in range(n):
    x=random()
    y=-np.log(1-x*(np.exp(2)-1)/np.exp(2))
    z=(np.exp(-y**2)*(np.exp(2)-1))/((np.exp(-y)*np.exp(2)))
    sum+=z
    R=sum/n
print(R)

