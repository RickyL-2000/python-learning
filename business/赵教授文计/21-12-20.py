"""
描述
统计单词出现次数并排序输出

输入
最多60,000个单词，每个一行。单词由小写字母构成，不超过30个字符。
输出
按单词出现次数从高到低输出所有单词。次数相同的，按照词典序从小到大排。
样例输入
about
send
about
me
样例输出
2 about
1 me
1 send
"""

list1 = []
list3 = []
list4=[]
listout = []
# import sys
# for a in sys.stdin:
#     list1.append(a)

list1 = ["about", "send", "about", "me"]
    
list2 = list(set(list1))
list2.sort()

for i in range(len(list2)):
    list3.append(list1.count(list2[i]))

for i in range(len(list2)):
    list4.append((list3[i],list2[i]))

list4.sort(key=lambda x: (-x[0], x[1]))

for i in range(len(list2)):
    listout.append(str(list4[i][0])+' '+str(list4[i][1]))

print('\n'.join(str(i) for i in listout))
