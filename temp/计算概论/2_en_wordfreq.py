"""
Date: 2020.11.24
Author: Justin

要点说明：
1、从文件读入英文文本，统计词频
2、设置忽略单词列表
3、用字典计数，统计完成后打印
4、存在的问题是字典无序，无法按数量排序
"""

txt_filename = './data/dream.txt'
ignore_list = ['the','of','to','and','a','be','is','in','as',
               'this','that','from','with','for']

# 从文件读取文本
txt_file = open(txt_filename, 'r')
content = txt_file.read()
txt_file.close()

# 文本预处理：替换特殊字符；全部变小写
content = content.lower()

for char in '\\\'~`!@#$%^&*()-_=+[]{}|;:",./<>?':
    content = content.replace(char, ' ')

# 用split()函数把长字符串切分成单词的列表
# split()函数不带参数时，表示识别换行符、制表符、空格。
word_list = content.split()
print('There are ' + str(len(word_list)) + ' words in this article.')

# 注：这样统计时，单词的各种分词形式和单复数形式会被分开统计
# 如果需要将单词的不同形式合并统计，要将单词都转成原型。可以用nltk库完成

# 声明字典，单词为键，对应的值统计出现的次数
word_dict = {}
for w in word_list:
    if w in word_dict.keys():
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1

# 删除不想统计的词，如冠词、连词等
for w in ignore_list:
    del word_dict[w]
print('Some words are ignored.')
    
# 打印字典中的键值对，即 单词 和 出现次数。
# 注意字典是无序的
print_limit = min(len(word_dict),10) # 最多打印10条
count = 0
print('-'*20)

for key,value in word_dict.items():
    print(key + ': ' + str(value))
    count = count + 1
    if count >= print_limit:
        break

print('-'*20)
print('Total: ' + str(len(word_dict)) + ' items')
print('Printed: ' + str(count) + ' items')
