import threading
import os
import random

status_list = ["我在睡觉......", "我醒着但我很无聊......", "我在散步......", "我在玩耍......", "我在吃饭......", "我在看医生......"]

if os.path.exists("data.txt"):
    with open("data.txt", "r", encoding="utf-8") as f:
        data = f.read().split()
else:
    # 所有状态随机设置
    data = [random.randint(0, 100), 
            random.randint(0, 100), 
            random.randint(0, 100), 
            random.randint(0, 23)]
    data.append(random.choice(status_list[1:]) if data[3] >= 8 else status_list[0])

cat_happiness = int(data[0])
cat_hungry = int(data[1])
cat_health = int(data[2])
cur_time = int(data[3])
cat_status = data[4]

def clock():
    global cur_time
    global cat_happiness
    global cat_hungry
    global cat_health
    global cat_status
        
    #8点醒0点睡
    if cur_time == 0:
        updates_status("我在睡觉......", print_status=False)
    elif cur_time == 8:
        updates_status("我醒着但我很无聊......", print_status=False)

    if cat_status == "我醒着但我很无聊......":
        cat_hungry += 2
        cat_happiness -= 1
    elif cat_status =="我在睡觉......":
        cat_hungry += 1
    elif cat_status =="我在散步......":
        cat_hungry += 3
        cat_health += 1
    elif cat_status =="我在玩耍......":
        cat_hungry += 3
        cat_happiness += 1
    elif cat_status =="我在吃饭......":
        cat_hungry -= 3
    elif cat_status =="我在看医生......":
        cat_health += 4

    #如果饥饿指数大于80，或低于20（过饱），则每个滴答健康指数减去2
    if cat_hungry > 80 or cat_hungry < 20:
        cat_health -= 2

    #如果幸福指数低于20，则每个滴答健康指数减去2
    if cat_happiness < 20:
        cat_health -= 2

    cat_hungry = max(0, min(100, cat_hungry))
    cat_health = max(0, min(100, cat_health))
    cat_happiness = max(0, min(100, cat_happiness))

    cur_time = (cur_time + 1) % 24

    print_current_status()
        
    # 当时间计数到23时归零，循环输出时间
    global timer
    timer = threading.Timer(5.0, clock)
    timer.start()

def updates_status(new_status, print_status=True):
    global cat_status
    cat_status = new_status
    if print_status:
        print(cat_status, "\n")

# 当你键入“status“命令时，需要你用”*“和”-“字符（共计 50 个）模拟它的状态进度，并给出当前状态指数的具体值。
def print_current_status():
    print("\n当前时间: {}点".format(cur_time))
    print("我当前的状态: {}".format(cat_status))

    print("Happiness:   Sad " + "*"*(cat_happiness//2) + "-"*(50-cat_happiness//2) + " Happy({:03})".format(cat_happiness))
    print("Hungry:     Full " + "*"*(cat_hungry//2) + "-"*(50-cat_hungry//2) + " Hungry({:03})".format(cat_hungry))
    print("Health:     Sick " + "*"*(cat_health//2) + "-"*(50-cat_health//2) + " Healthy({:03})\n".format(cat_health))

def commandWakePet(command):  # 宠物醒着的时候，运行命令
    if command == "walk":
        updates_status("我在散步......")
    elif command == "play":
        updates_status("我在玩耍......")
    elif command == "feed":
        updates_status("我在吃饭......")
    elif command == "seedoctor":
        updates_status("我在看医生......")
    elif command == "letalone":
        updates_status("我醒着但我很无聊......")
    else:
        print("我不懂你在说什么")

def main():
    print("我的名字叫Tommy，一只可爱的猫咪....")
    print("你可以和我一起散步玩耍，你也可以给我好吃的东西，带我去看病，也可以让我发呆....")
    print("Commands:")
    print("1.walk:散步")
    print("2.play:玩耍")
    print("3.feed:喂我")
    print("4.seedoctor:看医生")
    print("5.letalone:让我独自一猫")
    print("6.status:查看我的状态")
    print("7.bye:不想看到我\n")

    clock()

    global cat_happiness
    global cat_hungry
    global cat_health
    global cur_time
    global cat_status

    while True:
        command = input("你想: ")
        if command == "bye":
            with open("data.txt", "w", encoding="utf-8") as f:
                f.write(f"{cat_happiness}\n{cat_hungry}\n{cat_health}\n{cur_time}\n{cat_status}\n")
            print("记得来找我!Bye...")
            break
        elif command == "status":
            print_current_status()
        else:
            if cur_time >= 8:  # 8点到24点
                commandWakePet(command)
            else:  # 0点到8点
                if command == "letalone":
                    updates_status("我在睡觉......")
                elif cat_status != "我在睡觉......":
                    commandWakePet(command)
                else:
                    if input("你确定要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的!（y表示是/其他表示不是）") == 'y':
                        #如果在睡觉状态要带它去活动，幸福指数减去4
                        cat_happiness -= 4
                        cat_happiness = max(0, min(100, cat_happiness))
                        commandWakePet(command)

    timer.cancel()

if __name__ == '__main__':
    main()

