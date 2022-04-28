"""
3.作业3： 生成包括N(=1000)个0-100之间的随机分数，统计其中各个分数出现的次数，按照出现次数的从高到低的顺序（不包括出现次数为0的分数）打印出来。
首先采用每行：分数 次数格式输出
其次每行： 次数：分数1、分数2.... 的格式输出
"""

import random

N = 1000
# 第11行是第12-14行的快速写法，可以只需要一行。但是12-14行是基础
# scores = [random.randint(0, 100) for _ in range(N)]
scores = []
for i in range(N):
    scores.append(random.randint(0, 100))   # 随机生成 [0, 100] 之间的整数
# 建立两个字典 cnt1, cnt2
# 其中 cnt1: {score, cnt}; cnt2: {cnt, [score]}
# cnt1 记录每个score出现了cnt次；
# cnt2 记录出现了cnt次的score的一个list
cnt1, cnt2 = {}, {}
for score in scores:                # 遍历生成的N的scores
    if score in cnt1:               # 如果当前score已经存在cnt1字典中
        cnt1[score] += 1            # 就让当前计数+1
    else:
        cnt1[score] = 1             # 否则初始化为1，只出现了1次
# 对字典进行排序
# cnt1.item() 返回一个list,其中的元素为每个(key, value)对
# lambda x: x[1]指的是对此list进行排序的时候，以x[1]，也就是value位置进行标准排序
# 在这个情况下，就是对(score, cnt)中的cnt部分进行排序，就是对次数进行排序
# reverse=True 所以是降序
cnt1 = sorted(cnt1.items(), key=lambda x: x[1], reverse=True)
# 输出，同时建一个新的字典
for item in cnt1:
    # 按照格式输出第一部分，item的内容是(score, cnt)
    print(item[0], item[1]) 
    # 构建字典 cnt2
    if item[1] in cnt2:                     # 如果当前次数item[1]，即cnt，已经存在cnt2字典中
        cnt2[item[1]].append(str(item[0]))  # 则让该次数对应的list，append一个当前的score，即item[0]
    else:                                   
        cnt2[item[1]] = [str(item[0])]      # 否则初始化一个list，内容是item[0]，即当前的score
# 对字典cnt2进行排序，排序规则参考(key, value)中的key，即cnt2中的cnt，即次数
cnt2 = sorted(cnt2.items(), key=lambda x: x[0], reverse=True)
for item in cnt2:
    # 输出，并把每个cnt对应的score的list用join()连接起来，连接符号是"、"
    print(f"{item[0]}：{'、'.join(item[1])}")

