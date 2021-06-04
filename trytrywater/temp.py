# %%
freq = []
dura = []

with open('monkeyisland.sh', 'r') as file:
    data = file.read().split()
# print(data)
for i in range(len(data)):
    if data[i] == '-f':
        freq.append(round(float(data[i+1])))
    if data[i] == '-l':
        dura.append(round(float(data[i+1])))

# %%
print(len(freq) == len(dura))
print(len(freq))

# %%
