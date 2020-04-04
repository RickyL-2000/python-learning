# %%
import numpy as np

A = np.array([[2,0,0,1],
              [0,2,-1,-1],
              [0,1,2,-1],
              [1,-1,0,0]])
b = np.array([2,0,-2,-1])
x = np.linalg.solve(A, b)
print(x)

# %%
A = np.array([
    [2,2,-1],
    [0,-1,3],
    [1,-1,0]
])
b = np.array([2,0,-1])
x = np.linalg.solve(A, b)
print(x)

# %%
A = np.array([[4,-1],[-1,3]])
b = np.array([2,-2])
x = np.linalg.solve(A,b)
print(x)

# %%
