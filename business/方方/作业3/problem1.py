def print_scores(scores):
    """打印分数，每行5个数值"""
    lens = len(scores)//5
    lefts = len(scores) % 5 
    for i in range(lens):
        print('%4d %4d %4d %4d %4d' % (scores[i*5], scores[i*5+1], scores[i*5+2], scores[i*5+3], scores[i*5+4]) )
    for i in range(len(scores)-lefts,len(scores)):
        print('%4d ' % scores[i],end='')
    if ( lefts > 0): print() 

import random

# 随机产生了43个位于[50,100]之间的分数值
scores = [random.randint(50,100) for i in range(43)]
print('\n总共%d同学分数如下：' % len(scores))
print_scores(scores)

scores.sort()
print("前10位分数(从高到低)分别为")
print_scores(scores[-1:-11:-1])

print("后10位分数(从低到高)分别为")
print_scores(scores[:10])
