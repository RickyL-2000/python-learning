import random
print("作业5：统计分数出现次数")
scores = []
for i in range(1000):
    scores.append(random.randint(0, 100))
counter = {}
for score in scores:
    if score in counter:
        counter[score] += 1
    else:
        counter[score] = 1
counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
for item in counter:
    print(item[0], item[1])
number = -1     
for item in counter:
    if number != item[1]:
        if number != -1:
            print()     # 去掉两段之间的空行
        number = item[1]
        print("次数", number, ":", item[0], end='')
    else:
        print(",", item[0], end='')
