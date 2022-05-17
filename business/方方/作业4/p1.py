def check(a, b):
    cnt_a = {}
    cnt_b = {}
    for c in a:
        if c in cnt_a:
            cnt_a[c] += 1
        else:
            cnt_a[c] = 1
    for c in b:
        if c in cnt_b:
            cnt_b[c] += 1
        else:
            cnt_b[c] = 1
    if len(cnt_a) != len(cnt_b):
        return False
    for c in cnt_a:
        if c not in cnt_b:
            return False
        if cnt_a[c] != cnt_b[c]:
            return False
    return True

s = input("请输入两个单词，以空格分隔: ")
a, b = s.strip().split()

if check(a, b):
    print(f"单词{a}与单词{b}是相似词！")
else:
    print(f"单词{a}与单词{b}不是相似词！")
