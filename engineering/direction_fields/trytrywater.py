# %%
import matplotlib.pyplot as plt

# %%
tx0 = 0.1
ty0 = 0.2
tx1 = 0.3
ty1 = 0.5

# %%
plt.annotate('',xy=(tx0,ty0),xytext=(tx1,ty1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))

# %%