import threading
import time
import random

# config
TICK_TACK = 5
WAKE_UP = 8
FALL_ASLEEP = 24

Commands = ["walk", "play", "feed", "seedoctor", "letalone", "status", "bye", "disturb"]
States = ["walk", "play", "feed", "seedoctor", "letalone", "sleep", "waiting_for_disturb"]

# globals
clock = 0

class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        global clock
        while True:
            time.sleep(TICK_TACK)
            clock = (clock + 1) % 24

class CatTommy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        # the clock
        global clock
        self.internal_clock = clock
        # states
        self.state = "letalone"
        # value
        self.hunger_value = int(random.randint(1, 100))
        self.happy_value = int(random.randint(1, 100))
        self.health_value = int(random.randint(1, 100))
        
    def run(self):
        global clock
        while True:
            if self.internal_clock != clock:
                self.internal_clock = clock

                if self.state == "letalone":
                    self.hunger_value += 2
                    self.happy_value -= 1
                elif self.state == "sleep" or self.state == "waiting_for_disturb":
                    self.hunger_value += 1
                elif self.state == "walk":
                    self.hunger_value += 3
                    self.health_value += 1
                elif self.state == "play":
                    self.hunger_value += 3
                    self.health_value += 1
                elif self.state == "feed":
                    self.hunger_value -= 3
                elif self.state == "seedoctor":
                    self.health_value += 4

                # value check
                self.__value_check()

                # normalize
                self.hunger_value = max(0, min(100, self.hunger_value))
                self.happy_value = max(0, min(100, self.happy_value))
                self.health_value = max(0, min(100, self.health_value))
                
    def __value_check(self):
        if self.hunger_value > 80 or self.hunger_value < 20:
            self.health_value -= 2
        if self.happy_value < 20:
            self.health_value -= 1

    def update_state(self, new_state):
        if self.state == new_state:
            return
        if self.state == "sleep" and new_state in ["walk", "play", "feed", "seedoctor"]:
            self.state = "waiting_for_disturb"
            self.handle_disturb_waiting(new_state)
            return
        if self.state == "sleep" and new_state == "letalone":
            self.print_state()
            return
        if new_state in ["walk", "play", "feed", "seedoctor", "letalone"]:
            self.state = new_state
            self.print_state()
        elif new_state == "sleep":
            self.state = new_state  # no printing

    def handle_disturb_waiting(self, new_state):
        confirm = input("你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！(y表示是/其他表示不是):")
        if confirm != "y":
            self.state = "sleep"
            return
        if self.state == "sleep":
            self.state = new_state
            self.happy_value -= 4
            self.__value_check()
            self.print_state(cur_time=False, cur_values=False)
        else:
            # NOTE: 如果它睡着了，你打扰它，但是你过了很久，等它醒了再坚持带它去活动，则不会扣happy值
            self.state = new_state
            self.print_state()

    def print_state(self, cur_time=True, cur_state=True, cur_values=True):
        if cur_time:
            print(f"当前时间: {clock}点")
        if cur_state:
            print("我当前的状态:", end="")
            if self.state == "walk":
                print("我在散步.....")
            elif self.state == "play":
                print("我在玩耍.....")
            elif self.state == "feed":
                print("我在吃饭.....")
            elif self.state == "seedoctor":
                print("我在看医生.....")
            elif self.state == "letalone":
                print("我醒着但很无聊.....")
            elif self.state == "sleep":
                print("我在睡觉.....")
        if cur_values:
            print(f"Happiness:  Sad {'*'*int(self.happy_value/2) + '_'*int(50-self.happy_value//2)} Happy({self.happy_value:03})")
            print(f"Hungry:    Full {'*'*int(self.happy_value/2) + '_'*int(50-self.happy_value//2)} Hungry({self.happy_value:03})")
            print(f"Health:    Sick {'*'*int(self.happy_value/2) + '_'*int(50-self.happy_value//2)} Healthy({self.happy_value:03})")
        
    def process_input(self, command):
        return
        

    def load_checkpoints(self):
        pass

    def save_checkpoints(self):
        pass

if __name__ == '__main__':
    timer = Timer()
    timer.daemon = True
    timer.start()
    # timer.join()

    while True:
        key = input("input:")
        print("-"*20)
        if key == "status":
            print("cnt:", cnt)
            print("value:", timer.value)
        elif key == "q":
            break
        elif key.isdigit():
            timer.value = key
            print("cnt:", cnt)
            print("value:", timer.value)
        print("-"*20)


    timer.join()
