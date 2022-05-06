s = input("请输入两个单词，以空格分隔")
a, b = s.strip().split()
if len(a) == len(b):
    print(f"单词{a}与单词{b}是相似词！")
else:
    print(f"单词{a}与单词{b}不是相似词！")
