"""
描述
一年一度的趣味游戏大赛又开幕了。今年的主办方只为所有的参赛选手准备了一道题目，如下：
    
    给定10个整数的序列，要求对其重新排序。排序要求:
    1.奇数在前，偶数在后；
    2.奇数按从大到小排序；
    3.偶数按从小到大排序。

当选手做出这道题目，即可得到丰厚的奖励。你准备好拿奖了吗？

输入
输入一行，包含10个整数，彼此以一个空格分开，每个整数的范围是大于等于0，小于等于100。
输出
按照要求排序后输出一行，包含排序后的10个整数，数与数之间以一个空格分开。
样例输入
4 7 3 13 11 12 0 47 34 98
样例输出
47 13 11 7 3 0 4 12 34 98
"""

list1=input().split()
listodd=[]
listeven=[]
for i in list1:
    if int(i)%2==1:
        listodd.append(int(i))
    if int(i)%2==0:
        listeven.append(int(i))
listodd.sort(reverse=True)
listeven.sort()
a=' '.join(str(i) for i in listodd)+' '+' '.join(str(j) for j in listeven)
print(a)
