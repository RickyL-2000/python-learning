# %%
import mido
import re

# %%
mid = mido.MidiFile(r"ID - Nyan Cat.mid")

# %%
''' print meta info and sample '''
for msg in mid.tracks[0]:
    print(msg)

# %%
msg_list = []
for msg in mid.tracks[1]:
    msg_list.append(str(msg))

for i in range(10):
    print(msg_list[i])

# %%
''' begin parse '''
tempo = 428571 # how much μs in one beat
time2duration = lambda x: int(x / 48 * tempo / 1000)
pitch2freq = lambda x: int(440 * 2**((x - 69) / 12))

freq = []
duration = []
i = 1
while i < len(msg_list) - 1:
    if not (msg_list[i][:7] == "note_on" and msg_list[i+1][:8] == "note_off"):
        i += 1
        continue

    on_time = int(re.search(r'time=([0-9]+)', msg_list[i]).group(1))
    off_time = int(re.search(r'time=([0-9]+)', msg_list[i+1]).group(1))

    if on_time > 0:     # a duration for silence
        freq.append(0)
        duration.append(time2duration(on_time))

    note = int(re.search(r'note=([0-9]+)', msg_list[i]).group(1))
    freq.append(pitch2freq(note))
    duration.append(time2duration(off_time))

    i += 2


# %%
temp = "note_off channel=0 note=75 velocity=80 time=48"
print(re.search(r'note=([0-9]+)', temp).group(1))

# %%
for i in range(820, 980):
    print(msg_list[i])

# %%
print(freq)
print(duration)
# %%
print(len(freq))
print(len(duration))

# %%
''' second try (every pitch with same duration) '''
''' begin parse '''
tempo = 428571 # how much μs in one beat
time2duration = lambda x: int(x / 48 * tempo / 1000)
pitch2freq = lambda x: int(440 * 2**((x - 69) / 12))
dur = 214

freq = []
duration = []
i = 1
while i < len(msg_list) - 1:
    if not (msg_list[i][:7] == "note_on" and msg_list[i+1][:8] == "note_off"):
        i += 1
        continue

    on_time = int(re.search(r'time=([0-9]+)', msg_list[i]).group(1))
    off_time = int(re.search(r'time=([0-9]+)', msg_list[i+1]).group(1))

    if on_time > 0:     # a duration for silence
        freq.append(0)
        duration.append(time2duration(on_time))

    note = int(re.search(r'note=([0-9]+)', msg_list[i]).group(1))

    if (time2duration(off_time) > dur):
        freq.append(pitch2freq(note))
        duration.append(dur)
        freq.append(0)
        duration.append(time2duration(off_time) - dur)
    else:
        freq.append(pitch2freq(note))
        duration.append(time2duration(off_time))

    i += 2
