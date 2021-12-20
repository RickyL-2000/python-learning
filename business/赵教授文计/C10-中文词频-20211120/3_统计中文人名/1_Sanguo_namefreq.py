"""
Date: 2020.12.01
Author: Justin

要点说明：
1、读入《三国演义》中文小说文本，用jieba库分词
2、用字典统计两字以上的词的出现次数
3、删除不是人名的词
4、对指代同一人物的人名进行合并
5、根据用户需求，打印出现次数最多的若干个人物名字和出现次数
6、上述打印结果同时写入结果文件
"""

import jieba

txt_filename = './data/三国演义.txt'

# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
print('文件读取完成')

## 经过初次统计，会看到：玄德曰 孔明曰。需要考虑是否计数。
## 考虑到曹操出现的次数与孔明和玄德相当，因此用自定义字典加上“操曰”
## 可以看到 操曰 玄德曰 孔明曰 数量相当。
## 因此可以都统计，也可以都不统计
# jieba.add_word('操曰')  
# jieba.del_word('操曰')

# 分词
word_list = jieba.lcut(content)
print('分词完成')

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    if len(w) == 1: # 忽略单字
        continue
    # 对指代同一人物的名词进行合并
    if w == '孔明':
        w = '诸葛亮'
        # “丞相”出现很多，究竟指代谁，值得深入分析，这里未作处理
    elif w == '玄德' or w == '刘玄德':
        w = '刘备'
    elif w == '云长' or w == '关公':
        w = '关羽'
    elif w == '后主':
        w = '刘禅'
    else:
        pass # pass表示“什么都不做”，常用于为尚未完成的代码占位置

    
    # 已在字典中的词，将出现次数增加1；否则，添加进字典，次数记为1
    if w in word_dict.keys():
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1
        
print('词频统计完成')

# 删除不想统计的词
ignore_list =  ['将军','却说','二人','不可','荆州','不能','如此',
               '商议','如何','主公','军士','左右','军马','次日',
               '引兵','大喜','天下','东吴','于是','今日','不敢',
               '魏兵','陛下','人马','都督','一人','不知','汉中',
               '众将','只见','蜀兵']

for w in ignore_list:
    del word_dict[w]

print('删除停用词完成')

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)

# 计算并打印不同的词的总数
total_num = len(items_list)
print('='*20)
#print('经统计，共有' + str(total_num) + '个不同的词')
print('经统计，共有{}个不同的词'.format(total_num))

# 了解用户需求：打印排名前列的词的数量
num = input('您想查看前多少个人物？[10]:')
if not num.isdigit() or num == '':
    num = 10
else:
    num = int(num)

if num > total_num:
    num = total_num
    
# 把结果打印在屏幕上，同时把统计结果存入文件
result_filename = './output/三国演义-人物词频.csv'
result_file = open(result_filename, 'w')   

result_file.write('人物,出现次数\n')
for i in range(num):
    word, cnt = items_list[i]
    #print(str(i+1) + '. ' + word + '\t' + str(cnt))
    print('{}.{}\t{}'.format(i+1,word,cnt))
    #result_file.write(word + ',' + str(cnt) + '\n')
    result_file.write('{},{}\n'.format(word,cnt))

result_file.close()

print('已写入文件：' + result_filename)
