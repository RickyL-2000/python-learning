# %%
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import t
from sympy import Function

# %%
def plotSlopeField(tdomain,ydomain,formula,points = []):
    # initialize figure
    fig = plt.figure(num=1)
    # create grid
    T,Y = np.meshgrid(tdomain,ydomain )
    # calculate direction vectors
    U = 1
    V = np.array([[formula.subs({y(t): yval, t: tval}) for tval in tdomain] for yval in ydomain],dtype = 'float')
    N = np.sqrt(U**2+V**2)
    U2, V2 = U/N, V/N
    # make the plot
    plt.quiver( T,Y,U2, V2)
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y$")
    plt.axhline(0,0,1,linewidth = 2, color = 'black')
    plt.axvline(0,0,1,linewidth = 2, color = 'black')
    return fig

# %%
tdomain1 = np.linspace(-3, 3, 30)
ydomain1 = np.linspace(-3, 3, 30)

# %%
y = Function('y')
formula1 = t/(y(t))
formula2 = y(t)/t
formula3 = -y(t)/t

# %%
fg = plotSlopeField(tdomain1, ydomain1, formula3, [])
fg.show()


# %%
