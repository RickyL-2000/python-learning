"""
Date: 2020.12.01
Author: Justin

要点说明：
1、用jieba.pseg在分词时标注词性
2、显示所有的分词，用字典记录下人名和词性
注：jieba的常见词性代号
a，形容词；c，连词；n，名词；nr，人名；ns，地名；v，动词
"""

import jieba.posseg as pseg

content = '念刘备、关羽、张飞，虽然异姓，既结为兄弟，\
……不求同年同月同日生，只愿同年同月同日死。'

#import jieba
#jieba.load_userdict('./data/userdict_pseg.txt')

words =pseg.cut(content)
#pseg.cut()函数返回的是一个“生成器”，用于生成列表
#用for循环可以从“生成器”中提取列表元素，但不能提前知道列表的长度
print(words) # 这条语句无法打印出列表的内容

name_dict = {}

i = 0
for w in words:
    i = i + 1
    print(i, w.word, w.flag)
    if 'nr' in w.flag:  # nr代表人名
        name_dict[w.word] = w.flag

print('-'*20)

for name,flag in name_dict.items():
    print(name, flag)
