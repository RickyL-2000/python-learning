"""
描述
微博提供了一种便捷的交流平台。一条微博中，可以提及其它用户。例如Lee发出一条微博为：“期末考试顺利 @Kim @Neo”，则Lee提及了Kim和Neo两位用户。

我们收集了N(1 < N < 10000)条微博，并已将其中的用户名提取出来，用小于等于100的正整数表示。

通过分析这些数据，我们希望发现大家的话题焦点人物，即被提及最多的人（题目保证这样的人有且只有一个），并找出那些提及它的人。

输入
输入共两部分：
第一部分是微博数量N，1 < N < 10000。
第二部分是N条微博，每条微博占一行，表示为：
发送者序号a，提及人数k(0 < = k < = 20)，然后是k个被提及者序号b1,b2...bk；
其中a和b1,b2...bk均为大于0小于等于100的整数。相邻两个整数之间用单个空格分隔。
输出
输出分两行：
第一行是被提及最多的人的序号；
第二行是提及它的人的序号，从小到大输出，相邻两个数之间用单个空格分隔。同一个序号只输出一次。
样例输入
5
1 2 3 4
1 0
90 3 1 2 4
4 2 3 2
2 1 3
样例输出
3
1 2 4
来源
医学部计算概论2011年期末考试（谢佳亮）
"""

# NOTE: wrong

num = int(input())
list_totle0 = []
list_totle=[]
dict={}
max=0
output=[]

for i in range(num):
    list_totle0.append(list(input().split()))

# for i in range(num):
#     list_totle.append([])
#     for j in range(len(list_totle0[i])):
#         if list_totle0[i][j] not in list_totle[i]:
#             list_totle[i].append(list_totle0[i][j])
for i in range(num):
    list_totle.append(list_totle0[i][:2] + list(set(list_totle0[i][2:])))

for i in range(len(list_totle)):
    for j in range(2,len(list_totle[i])):
        if dict.get(list_totle[i][j]) is None:
            dict[list_totle[i][j]]=1
        else:
            dict[list_totle[i][j]]+=1

        if dict[list_totle[i][j]] > max:
            max= dict[list_totle[i][j]]
            freq = list_totle[i][j]

# freq=list(dict.keys())[list(dict.values()).index(max)]

for i in range(num):
    for j in range(2,len(list_totle[i])):
        if list_totle[i][j]==freq :
            output.append(list_totle[i][0])

output_2=set(output)
print(str(freq))
print(' '.join(str(i) for i in sorted(output_2)))
