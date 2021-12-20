"""
Date: 2020.12.01
Author: Justin

要点说明：
1、读入《三国演义》中文小说文本
2、用jieba库分词，用字典统计两字以上的词的出现次数
3、根据用户需求，打印出现次数最多的若干个词
4、上述打印结果同时写入结果文件
"""

import jieba


# 从文件读取文本
txt_filename = './data/三国演义.txt'

#txt_file = open(txt_filename, 'r') # 默认编码是gbk，该文件是utf-8
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()

# 分词
word_list = jieba.lcut(content)
    
# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    if (len(w)) == 1: # 忽略单字
        continue
    
    if w in word_dict.keys(): # 已在字典中的词，将出现次数增加1
        word_dict[w] = word_dict[w] + 1
    else:  # 未在字典中的词，表示是第一次出现，添加进字典，次数记为1
        word_dict[w] = 1

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)

total_num = len(items_list)
print('经统计，共有' + str(total_num) + '个不同的词')

# 了解用户需求：打印排名前列的词的数量
num = input("您想查看前多少词？[10]:")
if not num.isdigit() or num == '':
    num = 10
else:
    num = int(num)

# 打印在屏幕上，同时写入结果文件
result_filename = './output/三国演义-词频.csv'
result_file = open(result_filename, 'w')

result_file.write('词,次数\n')
for i in range(num):
    word, cnt = items_list[i]
    print(str(i+1) + '.' + word + '\t' + str(cnt))
    result_file.write(word + ',' + str(cnt) + '\n')

result_file.close()
print('已写入文件：' + result_filename)
    
    
