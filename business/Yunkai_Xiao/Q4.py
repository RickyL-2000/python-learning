# -*- encoding:utf-8 -*-
# 习题四
import random
import time
A=['C','D','H','S']
B=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
pokers=[]
n=1
for i in A:
    for j in B:
        pokers.append((n,(i+j)))
        n=n+1
random.shuffle(pokers)
def xipai(x):
    for i in x:
        pokers.remove(i)
    return pokers
def fapai(y):
    for i in y:
        print(i[1],' ',end="")
def paixu(z):
    for i in z:
        print(i[1],' ',end="")
time.sleep(3)
a=random.sample(pokers,13) 
pokers=xipai(a)   
fapai(a)
a.sort()
time.sleep(3)
print("\n13张扑克牌（无大小王牌）")