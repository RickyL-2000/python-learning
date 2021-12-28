import threading
import os
import random

# 保存各状态和状态对应的消息
status_dict = {
    "sleep": "我在睡觉...",
    "awake": "我醒着但我很无聊......",
    "walk": "我在散步......",
    "play": "我在玩耍......",
    "feed": "我在吃饭......",
    "seedoctor": "我在看医生......"
}

# 保存宠物的三个指标，随机初始化
cat_values = {
    "happiness": random.randint(0, 100),
    "hungry": random.randint(0, 100),
    "health": random.randint(0, 100),
}

cur_time = random.randint(0, 23)
cur_status = "sleep" if cur_time < 8 else "awake"

# 如果本地存在缓存文件，则从文件中恢复数据
if os.path.exists("cat.txt"):
    with open("cat.txt", "r") as f:
        values = f.read().split()
        cat_values["happiness"] = int(values[0])
        cat_values["hungry"] = int(values[1])
        cat_values["health"] = int(values[2])
        cur_status = values[3]
        cur_time = int(values[4]) - 1   # 从上一个时刻开始

# 更新状态并打印消息
def update_status(new_status):
    global cur_status
    cur_status = new_status
    print(status_dict[cur_status], "\n")

# 打印消息和进度条
def print_status():
    print(f"\n当前时间: {cur_time}点")
    print(f"我当前的状态: {status_dict[cur_status]}")

    print("Happiness:   Sad ", end="")
    print("*"*(cat_values["happiness"]//2) + "-"*(50-cat_values["happiness"]//2), end="")
    print(f" Happy({cat_values['happiness']:03})")

    print("Hungry:     Full ", end="")
    print("*"*(cat_values["hungry"]//2) + "-"*(50-cat_values["hungry"]//2), end="")
    print(f" Hungry({cat_values['hungry']:03})")

    print("Health:     Sick ", end="")
    print("*"*(cat_values["health"]//2) + "-"*(50-cat_values["health"]//2), end="")
    print(f" Healthy({cat_values['health']:03})\n")

# 处理命令并更新状态
def process_command(command):
    # 默认这时候宠物是醒着的
    if command in ["walk", "play", "feed", "seedoctor"]:
        update_status(command)
    elif command == "letalone":
        update_status("awake")
    else:
        print("我不懂你在说什么\n")

# func_timer函数，后台计时并更新宠物指标
def func_timer():        
    global cur_time
    global cur_status
    global timer

    # 时间从0到23循环
    cur_time = (cur_time + 1) % 24

    #8点醒0点睡
    if cur_time == 0:
        cur_status = "sleep"
        print(f"\n\n{status_dict[cur_status]}\n\n你想: ", end="")
    elif cur_time == 8:
        cur_status = "awake"
        print(f"\n\n{status_dict[cur_status]}\n\n你想: ", end="")

    # 基础指标更新
    if cur_status == "awake":
        cat_values["hungry"] += 2
        cat_values["happiness"] -= 1
    elif cur_status =="sleep":
        cat_values["hungry"] += 1
    elif cur_status =="walk":
        cat_values["hungry"] += 3
        cat_values["health"] += 1
    elif cur_status =="play":
        cat_values["hungry"] += 3
        cat_values["happiness"] += 1
    elif cur_status =="feed":
        cat_values["hungry"] -= 3
    elif cur_status =="seedoctor":
        cat_values["health"] += 4

    #如果幸福指数低于20，则每个滴答健康指数减去2
    if cat_values["happiness"] < 20:
        cat_values["health"] -= 2

    #如果饥饿指数大于80，或低于20（过饱），则每个滴答健康指数减去2
    if cat_values["hungry"] > 80 or cat_values["hungry"] < 20:
        cat_values["health"] -= 2

    cat_values["hungry"] = min(100, max(0, cat_values["hungry"]))
    cat_values["health"] = min(100, max(0, cat_values["health"]))
    cat_values["happiness"] = min(100, max(0, cat_values["happiness"]))
    
    timer = threading.Timer(5.0, func_timer)
    timer.start()

# 主函数，运行主要逻辑
def main():
    msg = "我的名字叫Tommy，一只可爱的猫咪....\n" \
          "你可以和我一起散步玩耍，你也可以给我好吃的东西，带我去看病，也可以让我发呆....\n" \
          "Commands:\n" \
          "1.walk:散步\n" \
          "2.play:玩耍\n" \
          "3.feed:喂我\n" \
          "4.seedoctor:看医生\n" \
          "5.letalone:让我独自一猫\n" \
          "6.status:查看我的状态\n" \
          "7.bye:不想看到我\n"

    print(msg)
    func_timer()
    print_status()

    while True:
        command = input("你想: ")
        if command == "status":
            print_status()
        elif command == "bye":
            with open("cat.txt", "w") as f:
                f.write(f"{cat_values['happiness']}\n")
                f.write(f"{cat_values['hungry']}\n")
                f.write(f"{cat_values['health']}\n")
                f.write(f"{cur_status}\n")
                f.write(f"{cur_time}\n")
            print("记得来找我!Bye...")
            break
        else:
            if cur_time >= 8:
                process_command(command)
            else:
                # 此时cat在睡觉
                # 需要考虑letalone的两个子状态
                if command == "letalone":
                    update_status("sleep")
                elif cur_status != "sleep":
                    process_command(command)
                else:
                    # 先吵醒，再进行命令
                    if input("你确定要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是/其他表示不是）") == "y":
                        cat_values["happiness"] -= 4
                        cat_values["happiness"] = min(100, max(0, cat_values["happiness"]))
                        process_command(command)

    timer.cancel()

main()
