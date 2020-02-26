# %%
import numpy as np
from numpy.linalg import solve

# %%
# this is the equation group of:
#   
a=np.mat([[2,3],[1,3]])#系数矩阵
b=np.mat([5,3]).T    #常数项列矩阵
x=solve(a,b)        #方程组的解
print(x)

# %%