# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
t = np.arange(1024)
signal = np.sin(t) + np.sin(2*t) + np.sin(8*t)

freq = np.fft.fftfreq(t.shape[-1])
sp = np.fft.fft(signal)

# %%
plt.plot(freq, sp.real**2)
plt.show()

# %%
plt.plot(freq, sp.imag)
plt.show()
