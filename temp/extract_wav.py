# referece
# https://docs.python.org/3/library/wave.html
# https://blog.csdn.net/vevoly/article/details/85993801
# https://blog.csdn.net/qq_39516859/article/details/79834039

# %%
import wave

# %%
f = wave.open(r"C:/Users/rickyl/Desktop/macOS_startup.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
f.close()

# %%
f = wave.open(r"C:/Users/rickyl/Desktop/macOS_startup.wav", "wb")
f.setsampwidth(1)
f.setframerate(44100)
f.setnchannels(2)
f.close()

# %%
print(nchannels, sampwidth, framerate, nframes)

# %%
print(f.getframerate())

# %%
print(f.getcomptype())

# %%
import struct
# f = open(r"C:/Users/rickyl/Desktop/macOS_startup.wav", "rb")
f = open(r"C:/Users/rickyl/Desktop/macOS_startup.wav", "rb")
info = f.read(44)
f.close()
print(struct.unpack('i', info[24:28]))
# %%
print(info[34:36])

# %%
