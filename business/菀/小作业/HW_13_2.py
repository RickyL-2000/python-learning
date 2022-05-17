"""
HW13_2. Kelly教练的田径队里有4位U10选手, 他们每次跑600m所花的时间被Kelly教练分别记录在4个文本文件中: james.txt, sarah.txt, julie.txt和mikey.txt. 这些时间的记录方式并不一致, 有"分:秒", "分.秒", "分-秒"三种方式. Kelly教练需要获得每位选手跑得最快的3个不同时间, 请编程实现.
"""
# %%
import re

def max_speed(fname):
    with open(fname, 'r') as f:
        text = f.read().strip().split(',')
    name = text[0]
    times = []
    for record in text[2:]:
        time = re.sub(r"[:-]", ".", record)
        times.append(time)
    times.sort()
    out = [times[0]]
    for i in range(1, len(times)):
        if times[i] == out[-1]:
            continue
        if len(out) == 3:
            break
        out.append(times[i])

    print(f"{name}'s fastest times are:", out)

if __name__ == '__main__':
    for f_name in ["james.txt", "julie.txt", "mikey.txt", "sarah.txt"]:
        max_speed(f_name)
