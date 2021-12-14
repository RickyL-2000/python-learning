"""
描述
小王很喜欢百京大学的长款羽绒服，但只能通过团购的形式找商家定做，因此她将想买羽绒服的同学都拉到了一个微信群里，大家在群里疯狂刷屏说出了自己想要的尺码和件数，但格式并不统一：

（1）码数后面跟相应的件数，例如：S要1件，M要2件

（2）出现“各”这个字，例如：M和L各要1件

（3）上述两种情况同时出现，例如：S和M各要1件，L要2件

由于消息数量特别多，小王没法手动处理，想请教你能不能使用计算机程序帮她计算出各个尺码的具体件数。

输入
输入若干行，每行都是一句话，以“end”作为结束。

注意：
（1）码数只有S，M，L三种，但有的同学可能打的是小写字母。
（2）大家都是用阿拉伯数字来表达件数，而不是中文的“一二三”。
（3）由于不存在买了十多件衣服的土豪，所以这些句子里的件数只会是1到9这9个数字之一。
（4）大家发消息实在是太随意了，上述只是样例，不能代表所有情况。句子之间不一定有逗号隔开，而且尺码和数字之间可能有多种多样的表达方式（例如：S码1件，S要1件，S码*1……）
输出
三个数字，用空格隔开，分别代表S，M，L三种尺码各自的件数。

样例输入
S 1件，M 2件
m和l各1
S/M各要1件，L要2件
end
样例输出
2 4 3

样例输入
S 1件，M 2件
m和l各1
S/M各要1件，L要2件
L要3件，S/M各要2件
end
样例输出
4 6 6
"""

msgs = []
while True:
    msg = input()
    if msg == "end":
        break
    msgs.append(msg.upper())

def find_num(s):
    for i, c in enumerate(s):
        if c.isdigit():
            return i, int(c)
    return -1, 0

# S_num, M_num, L_num = 0, 0, 0
output_num = [0, 0, 0]  # S_num, M_num, L_num
for msg in msgs:
    idx_list = (
        (0, msg.find("S")), # (index in output_num, index in the input string)
        (1, msg.find("M")),
        (2, msg.find("L"))
    )
    idx_list = sorted(idx_list, key=lambda x: x[1])
    # 排序后变成(X, Y, Z)
    each_idx = msg.find("各")
    if each_idx >= 0:
        # 有"各"
        if idx_list[1][1] < each_idx < idx_list[2][1]:
            # 此为 "X Y 各要x, Z 要 y" 情况
            # 需要在"各"和Z之间找到x
            _, each_num = find_num(msg[each_idx: idx_list[2][1]])
            output_num[idx_list[0][0]] += each_num
            output_num[idx_list[1][0]] += each_num
            _, temp_num = find_num(msg[idx_list[2][1]:])
            output_num[idx_list[2][0]] += temp_num
        elif idx_list[2][1] < each_idx:
            # 此时分为这么几种情况：
            # 1. "Y Z 各要x" (X不在string中，即idx==-1)
            # 2. "X Y Z 各要x"
            # 3. "X 要x, Y Z 各要y"
            if idx_list[0][1] == -1:
                # case 1
                _, each_num = find_num(msg[each_idx:])
                output_num[idx_list[1][0]] += each_num
                output_num[idx_list[2][0]] += each_num
            else:
                # 寻找 X 和 Y 之间是否有数字
                temp_idx, temp_num = find_num(msg[idx_list[0][1]: idx_list[1][1]])
                _, each_num = find_num(msg[each_idx:])
                if temp_idx == -1:
                    # 没有数字，即 case 2
                    output_num[idx_list[0][0]] += each_num
                    output_num[idx_list[1][0]] += each_num
                    output_num[idx_list[2][0]] += each_num
                else:
                    # case 3
                    output_num[idx_list[0][0]] += temp_num
                    output_num[idx_list[1][0]] += each_num
                    output_num[idx_list[2][0]] += each_num
    else:
        # 没有"各"
        if idx_list[0][1] > -1:
            _, num = find_num(msg[idx_list[0][1]: idx_list[1][1]])
            output_num[idx_list[0][0]] += num
        if idx_list[1][1] > -1:
            _, num = find_num(msg[idx_list[1][1]: idx_list[2][1]])
            output_num[idx_list[1][0]] += num
        if idx_list[2][1] > -1:
            _, num = find_num(msg[idx_list[2][1]:])
            output_num[idx_list[2][0]] += num

print(f"{output_num[0]} {output_num[1]} {output_num[2]}")
