import threading
import os
import random

# 所有可能的状态
all_status = {
    "walk": "我在散步......",
    "play": "我在玩耍......",
    "feed": "我在吃饭......",
    "see doctor": "我在看医生......",
    "sleep": "我在睡觉...",
    "idle": "我醒着但我很无聊......"
}

if os.path.exists("cat.csv"):
    # 从文件中回复状态
    with open("cat.csv", "r") as f:
        data = f.read().split()
        cat_happiness = int(data[0])
        cat_hunger = int(data[1])
        cat_health = int(data[2])
        cat_status = data[3]
        cat_time = int(data[4])
else:
    # 随机初始化
    cat_happiness = random.randint(0, 100)
    cat_hunger = random.randint(0, 100)
    cat_health = random.randint(0, 100)
    cat_time = random.randint(0, 23)
    if cat_time < 8:
        cat_status = "sleep"
    else:
        cat_status = "idle"

# 让所有值都在0和100之间
def check_value(value):
    return min(100, max(0, value))

# 修改自func_timer函数
def clock():        
    global cat_time
    global cat_status
    global timer

    global cat_happiness
    global cat_hunger
    global cat_health

    #8点醒0点睡。多print一次使得界面看上去更加友好
    if cat_time == 0:
        cat_status = "sleep"
        print(f"\n\n{all_status[cat_status]}\n\n你想: ", end="")
    elif cat_time == 8:
        cat_status = "idle"
        print(f"\n\n{all_status[cat_status]}\n\n你想: ", end="")

    # 基础指标更新
    if cat_status == "idle":
        cat_hunger += 2
        cat_happiness -= 1
    elif cat_status =="sleep":
        cat_hunger += 1
    elif cat_status =="walk":
        cat_hunger += 3
        cat_health += 1
    elif cat_status =="play":
        cat_hunger += 3
        cat_happiness += 1
    elif cat_status =="feed":
        cat_hunger -= 3
    elif cat_status =="see doctor":
        cat_health += 4

    if cat_hunger > 80 or cat_hunger < 20:
        cat_health -= 2

    if cat_happiness < 20:
        cat_health -= 2

    cat_hunger = check_value(cat_hunger)
    cat_health = check_value(cat_health)
    cat_happiness = check_value(cat_happiness)

    # 时间从0到23循环
    cat_time = cat_time + 1
    if cat_time > 23:
        cat_time = 0
    
    timer = threading.Timer(5.0, clock)
    timer.start()

# 处理命令，转移各个状态
def command_cat(command):
    global cat_status
    if command == "walk":
        cat_status = "walk"
        print(all_status["walk"] + "\n")
    elif command == "play":
        cat_status = "play"
        print(all_status["play"] + "\n")
    elif command == "feed":
        cat_status = "feed"
        print(all_status["feed"] + "\n")
    elif command == "see doctor":
        cat_status = "see doctor"
        print(all_status["see doctor"] + "\n")
    elif command == "letalone":
        # 假如此时是醒着的
        cat_status = "idle"
        print(all_status["idle"] + "\n")
    else:
        print("我不懂你在说什么\n")

# 进度条
def progress_bar(value):
    return "*"*(value//2) + "-"*(50-value//2)

def command_status():
    print(f"\n当前时间: {cat_time}点\n我当前的状态: {all_status[cat_status]}")

    print("Happiness:   Sad " + progress_bar(cat_happiness) + f" Happy({cat_happiness:03})")
    print("Hungry:     Full " + progress_bar(cat_hunger) + f" Hungry({cat_hunger:03})")
    print("Health:     Sick " + progress_bar(cat_health) + f" Healthy({cat_health:03})")
    print()

if __name__ == '__main__':
    print("我的名字叫Tommy，一只可爱的猫咪....")
    print("你可以和我一起散步玩耍，你也可以给我好吃的东西，带我去看病，也可以让我发呆....")
    print("Commands:")
    print("1.walk:散步")
    print("2.play:玩耍")
    print("3.feed:喂我")
    print("4.see doctor:看医生")
    print("5.letalone:让我独自一猫")
    print("6.status:查看我的状态")
    print("7.bye:不想看到我\n")

    command_status()
    clock()

    while True:
        command = input("你想: ")
        if command == "status":
            command_status()
        elif command == "bye":
            with open("cat.csv", "w") as f:
                f.write(str(cat_happiness) + "\n")
                f.write(str(cat_hunger) + "\n")
                f.write(str(cat_health) + "\n")
                f.write(str(cat_status) + "\n")
                f.write(str(cat_time) + "\n")
            print("记得来找我!Bye...")
            timer.cancel()
            break
        else:
            if cat_time < 8:
                # 此时tommy在睡觉
                if command == "letalone":
                    # 此时，无论如何tommy都应该睡回去
                    cat_status = "sleep"
                    print(all_status["sleep"] + "\n")
                elif cat_status != "sleep":
                    # 如果没有睡(已经被叫醒)那就继续做事
                    command_cat(command)
                else:
                    # 需要先吵醒
                    msg = input("你确定要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是/其他表示不是）")
                    if msg == "y":
                        cat_happiness -= 4
                        cat_happiness = check_value(cat_happiness)
                        command_cat(command)
                    else:
                        print()
            else:
                command_cat(command)

