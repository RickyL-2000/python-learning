# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
lat = np.array(np.linspace(1, 11, 9))
lon = np.array(np.linspace(1, 11, 9))

# %%
m = 9
n = 9
ver = hriz = []
for i in range(0, m):
    ver.append([])
    hriz.append([])
    for j in range(0, n):
        ver[i].append((-1*lon[j])/(lon[j]*lon[j] + lat[i]*lat[i]))
        hriz[i].append(lat[i]/(lon[j]*lon[j] + lat[i]*lat[i]))
    
# ver = (-1*lon)/(lon*lon + lat*lat)
# hriz = lat/(lon*lon + lat*lat)

# %%
plt.quiver(lon, lat, ver, hriz, color='deepskyblue', width=0.005, scale=30)
plt.show()

# %%
