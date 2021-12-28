# %%
import threading
# import numpy # Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
import time

# pConData = numpy.load('pData.npy')
# pConSta = numpy.load('pSta.npy')
# #numpy.load()函数从具有npy扩展名(.npy)的磁盘文件返回输入数组。
# tick = pConData[3]

try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
        content = content.split()
except:
    content = [30, 20, 20, 0, "我醒着但我很无聊......"]


judgeStop = False
#上面这部分不懂，不用numpy能否实现？

pet_name = "Tommy"
pet_Happiness = int(content[0])
pet_Hunger = int(content[1])
pet_Health = int(content[2])
pet_status = content[4]

tick = int(content[3])

timer = None

def rangeStatus(num):  # 各指数的值在 0～100之间
    if num > 100:
        num = 100
    elif num < 0:
        num = 0
    return num
#这一部分是各种状态的数值？

#以下是一种计时器的实现
def Clock():  # 模拟24h的时钟
    global tick
    global judgeStop
    global pet_name
    global pet_Happiness
    global pet_Hunger
    global pet_Health
    global pet_status
    # print("当前时刻：{}点".format(exec_count))
    
#这部分也不太懂 以上是老师提供的timer
        
#8点醒0点睡
    if tick == 0:
        pet_sleep()
    elif tick == 8:
        pet_wake()

#在醒着，什么事都不做的情况下，每个滴答，饥饿指数增加 2，幸福指数减少 1
#在睡着状态，每个滴答，饥饿指数增加1
#在陪它散步状态，每个滴答，饥饿指数增加3，健康指数增加1
#在陪它玩耍状态，每个滴答，饥饿指数增加3，幸福指数增加1
#在喂食状态，每个滴答，饥饿指数减少3
#如果带它去看医生，每个滴答，健康指数增加4

    if pet_status == "我醒着但我很无聊......":
        pet_Hunger += 2
        pet_Happiness -= 1
    elif pet_status =="我在睡觉......":
        pet_Hunger += 1
    elif pet_status =="我在散步......":
        pet_Hunger += 3
        pet_Health += 1
    elif pet_status =="我在玩耍......":
        pet_Hunger += 3
        pet_Happiness += 1
    elif pet_status =="我在吃饭......":
        pet_Hunger -= 3
    elif pet_status =="我在看医生......":
        pet_Health += 4

#如果在睡觉状态要带它去活动，幸福指数减去4
    # if tick < 8 and pet_status != "我在睡觉......":
    #     pet_Happiness -= 4


#如果饥饿指数大于80，或低于20（过饱），则每个滴答健康指数减去2
    if pet_Hunger > 80 or pet_Hunger < 20:
        pet_Health -= 2

#如果幸福指数低于20，则每个滴答健康指数减去2
    if pet_Happiness < 20:
        pet_Health -= 2

  # 改变值之后判断是否超过范围
    pet_Hunger = rangeStatus(pet_Hunger)
    pet_Health = rangeStatus(pet_Health)
    pet_Happiness = rangeStatus(pet_Happiness)
#不太明白

    tick += 1 #计数加一
    tick %= 24
#不太明白
        
# 当时间计数到23时归零，循环输出时间
    if judgeStop == False:
        global timer
        timer = threading.Timer(5, Clock)
        timer.start()
#如果用老师给的timer，如何实现？

#按照进度表输出参数
def printInfo(a):
    for i in range(1,(int)(a/2)+1):
        print("*",end="")
    for i in range((int)(a/2)+1,50):
        print("-",end="")

#以下语句如果不用class如何实现？
def pet_sleep():
    global pet_status
    pet_status = "我在睡觉......"
    print(pet_status, "\n")

def pet_wake():
    global pet_status
    pet_status = "我醒着但我很无聊......"
    print(pet_status, "\n")

def pet_walk():
    global pet_status
    pet_status = "我在散步......"
    print(pet_status, "\n")

def pet_play():
    global pet_status
    pet_status = "我在玩耍......"
    print(pet_status, "\n")

def pet_feed():
    global pet_status
    pet_status = "我在吃饭......"
    print(pet_status, "\n")

def pet_seeDoctor():
    global pet_status
    pet_status = "我在看医生......"
    print(pet_status, "\n")

# 当你键入“status“命令时，需要你用”*“和”-“字符（共计 50 个）模拟它的状态进度度，并给出当前状态指数的具体值。
def pet_cur_status():
    print("\n当前时间：", end="")
    print("{}点".format(tick))
    print("我当前的状态:", end="")
    print(pet_status)

    print("Happiness:   Sad", end="")
    printInfo(pet_Happiness)
    print("Happy({:0>3})".format(pet_Happiness))

    print("Hunger:      Full", end="")
    printInfo(pet_Hunger)
    print("Hungry({:0>3})".format(pet_Hunger))

    print("Health:      Sick", end="")
    printInfo(pet_Health)
    print("Healthy({:0>3})\n".format(pet_Health))

def commandWakePet(Command):  # 宠物醒着的时候，运行命令
    if Command == "walk":
        pet_walk()
    elif Command == "play":
        pet_play()
    elif Command == "feed":
        pet_feed()
    elif Command == "seedoctor":
        pet_seeDoctor()
    elif Command == "letalone":
        pet_wake()
        print(pet_status)
    else:
        print("我不懂你在说什么")

def commandSleepPet(Command):  # 宠物睡着的时候，先确定是否叫醒，再运行命令
    if Command == "letalone":
        pet_sleep()
        # print(pet_status)
    else:
        ans = input("你确定要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是/其他表示不是）")
        if ans == 'y':
            global pet_Happiness
            pet_Happiness -= 4
            pet_Happiness = rangeStatus(pet_Happiness)
            if Command == "walk":
                pet_walk()
            elif Command == "play":
                pet_play()
            elif Command == "feed":
                pet_feed()
            elif Command == "seedoctor":
                pet_seeDoctor()
            else:
                print("我不懂你在说什么") 

def mainF():
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

    # t1 = threading.Thread(target=Clock)
    # t1.start()
    Clock()

    global judgeStop
    while True:
        a = input("你想: ")
        if a == "bye":
            # 存储参数
            # 当你键入“bye”暂时关闭程序，你需要将 Tommy 的状态保存到文件（包括
            # 当前时刻，当前所处的状态，睡觉、散步等，各个状态指数），以便重新开始
            # 程序时，可以接着上次的状态开始你的游戏
            # pData = [pet_Happiness, pet_Hunger, pet_Health, tick]
            # pSta = [pet_status]
            # numpy.save('pData.npy', pData)
            # numpy.save('pSta.npy', pSta)

            with open("data.txt", "w", encoding="utf-8") as f:
                f.write("{}\n{}\n{}\n{}\n{}\n".format(pet_Happiness, pet_Hunger, pet_Health, tick, pet_status))

            print("记得来找我!Bye...")
            judgeStop = True
            break
        elif a == "status":
            pet_cur_status()
        else:
            # FIXME: 这或许不是一个好选择，因为叫醒后再letalone是可以睡回去的
            if tick >= 8 or (tick < 8 and pet_status != "我在睡觉......"):  # 8点到24点
                commandWakePet(a)
            else:  # 0点到8点
                commandSleepPet(a)

    # t1.join()
    timer.cancel()


# def VirtualPet():
#     print("我的名字叫Tommy，一只可爱的猫咪....")
#     print("你可以和我一起散步玩耍，你也可以给我好吃的东西，带我去看病，也可以让我发呆....")
#     print("Commands:")
#     print("1.walk:散步")
#     print("2.play:玩耍")
#     print("3.feed:喂我")
#     print("4.see doctor:看医生")
#     print("5.letalone:让我独自一猫")
#     print("6.status:查看我的状态")
#     print("7.bye:不想看到我\n")
#     t1 = threading.Thread(target=Clock)
#     t2 = threading.Thread(target=mainF)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# #\n不懂，t1往下不懂

if __name__ == '__main__':
    # VirtualPet()
    mainF()

