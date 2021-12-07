"""
Date: 2020.11.24
Author: Justin

要点说明：
对英文文本，统计词频
用字典计数，统计完成后打印
"""

content = '''She sells seashells on the seashore.
The seashells she sells are seashells, she is sure.'''

# 文本预处理1：全部变小写
content = content.lower()

# 文本预处理2：用空格替换特殊字符
# 注意转义的字符：\\表示反斜线,\'表示单引号
# 类似I'm这样的情况会被分割成I m，可能造成少量误差
for char in '\\\'~`!@#$%^&*()-_=+[]{}|;:",./<>?':
    content = content.replace(char, ' ')

# 用split()函数把长字符串切分成单词的列表
# split()函数不带参数时，表示识别换行符、制表符、空格
word_list = content.split()
print('There are ' + str(len(word_list)) + ' words.')
# for word in word_list:
#     print(word)

# 声明字典，单词为键，对应的值统计出现的次数
word_dict = {}
for w in word_list:
    if w in word_dict.keys():
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1

# 去掉不想统计的词
ignore_list = ['is', 'are']
for w in ignore_list:
    del word_dict[w]

# 打印字典中的键值对，即 单词 和 出现次数。注意字典是无序的
for key,value in word_dict.items():
    print(key + ': ' + str(value))
