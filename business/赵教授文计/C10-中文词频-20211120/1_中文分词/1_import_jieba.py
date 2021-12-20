"""
Date: 2020.12.01
Author: Justin

要点说明：
1、jieba是用于中文分词的第三方库，需要pip install jieba
2、jieba.lcut()函数进行分词的两种模式
"""

import jieba

txt = '北京大学创办于1898年，初名京师大学堂，是中国第一所国立综合性大学。'
word_list = jieba.lcut(txt)  # 精确模式，完整且不重复
print(word_list)

print('-'*20)
word_list = jieba.lcut(txt, cut_all=True) # 全模式，输出所有可能的词，会有冗余
print(word_list)

