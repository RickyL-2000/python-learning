"""
HW14_1. 编写一个按照固定句子结构造句的程序: 输入整数n, 输出n个句子.
固定的句子结构 The adj noun verb . 
举例 The crazed elephant danced a jig . 
说明 固定部分 形容词(adj) 名词(noun) 动词短语(verb) 固定部分 
要求：
1) 用户输入创建的句子数目，如果输入的不是整数，提示用户重新输入. 要求: 使用try…except…结构.
2) 从adj.txt  下载 adj.txt , noun.txt  下载 noun.txt , verb.txt  下载 verb.txt 三个文件读入可供选择的形容词、名词和动词短语, 构成一个speechPartsDict字典.
3) 从字典speechPartsDict中随机选择相应词性的单词来替换对应部分的内容, 其它字符原样输出. 即, 从字典中随机选择"adj", "noun", "verb"相对应的某个单词创建句子, "The"和"."原样输出.
"""
# %%
import random

if __name__ == '__main__':
    speechPartsDict = {}
    with open("adj.txt") as f:
        speechPartsDict["adj"] = f.read().strip().split(',')
    with open("noun.txt") as f:
        speechPartsDict["noun"] = f.read().strip().split(',')
    with open("verb.txt") as f:
        speechPartsDict["verb"] = f.read().strip().split(',')
    
    while True:
        try:
            n = int(input("请输入需要创建的句子数目(正整数): ").strip())
            if n <= 0:
                raise Exception
        except:
            print("输入有误，重新输入...")
            continue
        for i in range(1, n+1):
            out = ["The", 
                    random.choice(speechPartsDict["adj"]), 
                    random.choice(speechPartsDict["noun"]), 
                    random.choice(speechPartsDict["verb"])]
            out = " ".join(out) + "."
            print(f"{i}. {out}")
        break

