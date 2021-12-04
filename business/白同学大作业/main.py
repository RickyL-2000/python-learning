import threading
import time
import random

"""
Problems:
1. 当猫醒来的时候，需要自动触发输出一条信息表示它醒了吗？
"""

# constants
TICK_TACK = 5
WAKE_UP = 8
FALL_ASLEEP = 24
EXIT = -2

Commands = ["walk", "play", "feed", "seedoctor", "letalone", "status", "bye"]
States = ["walk", "play", "feed", "seedoctor", "letalone", "sleep", "waiting_for_disturb"]

class CatTommy():
    def __init__(self):
        # timer
        self.clock = 8
        self.t_begin = time.time()
        self.t_end = time.time()
        # states
        self.state = "letalone"
        # value
        self.hunger_value = int(random.randint(1, 100))
        self.happy_value = int(random.randint(1, 100))
        self.health_value = int(random.randint(1, 100))
    
    def run(self):
        print("Initial message")
        self.update_clock()
        self.print_state()
        while True:
            command = input("你想: ")
            res = self.process_input(command)
            if res == -1 or res == 0:
                continue
            elif res == EXIT:
                # exit the program
                self.save_checkpoints()
                print("记得来找我！Bye...")
                break
            else:
                self.update_state(res)
    
    def update_state(self, new_state, verbose=True):
        if self.state == new_state:
            return
        if self.state == "sleep" and new_state in ["walk", "play", "feed", "seedoctor"]:
            self.state = "waiting_for_disturb"
            self.handle_disturb_waiting(new_state)
            return
        if self.state == "sleep" and new_state == "letalone":
            if verbose: self.print_state()
            return
        if new_state in ["walk", "play", "feed", "seedoctor", "letalone"]:
            self.state = new_state
            if verbose: self.print_state()
        elif new_state == "sleep":
            self.state = new_state  # no printing
        else:
            print(f"Something went wrong. Illegal state name: {new_state}")

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

    def update_clock(self):
        self.t_end = time.time()
        time_passed = int(self.t_end - self.t_begin) // TICK_TACK
        self.clock = (self._clock + int(self.t_end - self.t_begin) // TICK_TACK) % 24
        self.t_begin = time.time()
        return time_passed

    def print_state(self, cur_time=True, cur_state=True, cur_values=True):
        if cur_time:
            print(f"当前时间: {self.clock}点")
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
        if command not in Commands:
            print("我不懂你在说什么")
            return -1
        if command in ["walk", "play", "feed", "seedoctor", "letalone"]:
            return command
        if command == "status":
            time_passed = self.update_clock()
            self.update_values(time_passed)
            self.print_state()
            return 0
        if command == "bye":
            # close the program
            return EXIT

    def update_values(self, time_passed):
        for t in range(time_passed):
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

    def load_checkpoints(self):
        pass

    def save_checkpoints(self):
        pass

if __name__ == '__main__':
    
    t_begin = time.time()

    while True:
        key = input("please input anything:")
        t_end = time.time()
        print(f"time has passed {t_end - t_begin}")
        t_begin = time.time()
        if key == "q":
            break
