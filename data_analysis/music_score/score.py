# %%
import matplotlib.pyplot as plt
import numpy as np


# %%
score = []
with open('D:\\GitHub\\python-learning\\data_analysis\\music_score\\notes2.txt', 'r') as notes:
    for line in notes.readlines():
        str_list = line.split()
        score.append([int(str_list[0]), int(str_list[1]), int(str_list[2])])

# %%
time = []
note = []
for e in score:
    time.append(e[0])
    note.append(e[2])

# %%
plt.plot(time[:len(time)//2], note[:len(note)//2])

plt.xlabel('time')
plt.ylabel('note')

plt.title("Score")

plt.show()
