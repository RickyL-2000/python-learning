import threading
import time

cnt = 0

class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.index = 0
    
    def run(self):
        global cnt
        while True:
            cnt += 1
            time.sleep(1)
    
    def subblock(self):
        input("thread is subblocked! input anything: ")
        print("cnt:", cnt)
        print("index:", self.index)

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
            print("index:", timer.index)
        elif key == "q":
            break
        elif key.isdigit():
            timer.index = key
            print("cnt:", cnt)
            print("index:", timer.index)
        elif key == "block":
            input("thread is blocked! input anything: ")
            print("cnt:", cnt)
            print("index:", timer.index)
        elif key == "subblock":
            timer.subblock()
        print("-"*20)


    timer.join()
