import threading
import numpy # Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
import time

pConData = numpy.load('pData.npy')
pConSta = numpy.load('pSta.npy')
#numpy.load()函数从具有npy扩展名(.npy)的磁盘文件返回输入数组。
tick = pConData[3]
# exec_count = 0
judgeStop = False
#上面这部分不懂，不用numpy能否实现？

def rangeStatus(num):  # 各指数的值在 0～100之间
    if num > 100:
        num = 100
        pass
    elif num < 0:
        num = 0
        pass
    return num
    pass
#这一部分是各种状态的数值？

#以下是一种计时器的实现
def Clock():  # 模拟24h的时钟
    global tick
    global judgeStop
    # print("当前时刻：{}点".format(exec_count))

#8点醒0点睡
    if tick == 0:
        p.sleep()
        pass
    elif tick == 8:
        p.wake()
        pass

#在醒着，什么事都不做的情况下，每个滴答，饥饿指数增加 2，幸福指数减少 1
#在睡着状态，每个滴答，饥饿指数增加1
#在陪它散步状态，每个滴答，饥饿指数增加3，健康指数增加1
#在陪它玩耍状态，每个滴答，饥饿指数增加3，幸福指数增加1
#在喂食状态，每个滴答，饥饿指数减少3
#如果带它去看医生，每个滴答，健康指数增加4
    
    if p.status == "我醒着但我很无聊......":
        p.Hunger += 2
        p.Happiness -= 1
        pass
    elif p.status =="我在睡觉......":
        p.Hunger += 1
        pass
    elif p.status =="我在散步......":
        p.Hunger += 3
        p.Health += 1
        pass
    elif p.status =="我在玩耍......":
        p.Hunger += 3
        p.Happiness += 1
        pass
    elif p.status =="我在吃饭......":
        p.Hunger -= 3
        pass
    elif p.status =="我在看医生......":
        p.Health += 4
        pass

#如果在睡觉状态要带它去活动，幸福指数减去4
    if tick < 8 and p.status != "我再睡觉......":
        p.Happiness -= 4
        pass

#如果饥饿指数大于80，或低于20（过饱），则每个滴答健康指数减去2
    if p.Hunger > 80 or p.Hunger < 20:
        p.Health -= 2
        pass

#如果幸福指数低于20，则每个滴答健康指数减去2
    if p.Happiness < 20:
        p.Health -= 2
        pass

  # 改变值之后判断是否超过范围
    p.Hungry = rangeStatus(p.Hungry)
    p.Health = rangeStatus(p.Health)
    p.Happiness = rangeStatus(p.Happiness)
#不太明白

    tick += 1 #计数加一
#不太明白
        
# 当时间计数到23时归零，循环输出时间
    if judgeStop == False:
        if tick < 24:
            threading.Timer(5, Clock).start()
            pass
        else:
            tick = 0
            threading.Timer(1, Clock).start()
            pass
        pass
    pass
#如果用老师给的timer，如何实现？

#按照进度表输出参数
def printInfo(a):
    for i in range(1,(int)(a/2)+1):
        print("*",end="")
        pass
    for i in range((int)(a/2)+1,50):
        print("-",end="")
        pass
    pass

#以下语句如果不用class如何实现？
class Pet:

    def __init__(self, Happiness, Hungry, Health, status):  # 初始化参数

        self.name = "Tommy"
        self.Happiness = Happiness
        self.Hunger = Hunger
        self.Health = Health
        self.status = status
        pass

    def sleep(self):
        self.status = "我在睡觉..."
        # print(self.status)
        pass

    def wake(self):
        self.status = "我醒着但我很无聊..."
        # print(self.status)
        pass

    def walk(self):
        self.status = "我在散步..."
        #print(self.status)
        pass

    def play(self):
        self.status = "我在玩耍..."
        #print(self.status)
        pass

    def feed(self):
        self.status = "我在吃饭..."
        #print(self.status)
        pass

    def seeDoctor(self):
        self.status = "我在看医生..."
        #print(self.status)
        pass

# 当你键入“status“命令时，需要你用”*“和”-“字符（共计 50 个）模拟它的状态进度度，并给出当前状态指数的具体值。
 def cur_status(self):
        print("\n当前时间：", end="")
        print("{}点".format(tick))
        print("我当前的状态:", end="")
        print(self.status)
        print("Happiness:   Sad", end="")
        printInfo(self.Happiness)
        print("Happy({})".format(self.Happiness))

        print("Hunger:      Full", end="")
        printInfo(self.Hungry)
        print("Hungry({})".format(self.Hunger))

        print("Health:      Sick", end="")
        printInfo(self.Health)
        print("Healthy({})\n".format(self.Health))
        pass
    pass

# 加载参数

# p = Pet(0, 0, 0 ,"")

p = Pet(pConData[0], pConData[1], pConData[2], pConSta[0])

def commandWakePet(Command):  # 宠物醒着的时候，运行命令
    if Command == "walk":
        p.walk()
        pass
    elif Command == "play":
        p.play()
        pass
    elif Command == "feed":
        p.feed()
        pass
    elif Command == "see doctor":
        p.seeDoctor()
        pass
    elif Command == "letalone":
        p.wake()
        print(p.status)
        pass
    else:
        print("我不懂你在说什么")

def commandSleepPet(Command):  # 宠物睡着的时候，先确定是否叫醒，再运行命令
    if Command == "letalone":
        p.sleep()
        print(p.status)
        pass
    else:
        ans = input("你确定要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是/其他表示不是）")
        if ans == 'y':
            if Command == "walk":
                p.walk()
                pass
            elif Command == "play":
                p.play()
                pass
            elif Command == "feed":
                p.feed()
                pass
            elif Command == "see doctor":
                p.seeDoctor()
                pass
            else:
                print("我不懂你在说什么")
                pass
            pass 

def mainF():
    global judgeStop
    while True:
        a = input("你想做什么")
        if a == "bye":
            # 存储参数
            # 当你键入“bye”暂时关闭程序，你需要将 Tommy 的状态保存到文件（包括
            # 当前时刻，当前所处的状态，睡觉、散步等，各个状态指数），以便重新开始
            # 程序时，可以接着上次的状态开始你的游戏
            pData = [p.Happiness, p.Hungry, p.Health, exec_count]
            pSta = [p.status]
            numpy.save('pData.npy', pData)
            numpy.save('pSta.npy', pSta)
            print("记得来找我!Bye...")
            judgeStop = True
            break
        elif a == "status":
            p.cur_status()
            pass
        else:
            if exec_count >= 8:  # 8点到24点
                orderWakePet(a)
                pass
            else:  # 0点到8点
                orderSleepPet(a)
                pass
        pass

def VirtualPet():
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
    t1 = threading.Thread(target=Clock)
    t2 = threading.Thread(target=mainF)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pass
#\n不懂，t1往下不懂

if __name__ == '__main__':
    VirtualPet()
    pass

