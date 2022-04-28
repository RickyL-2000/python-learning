import random

number = random.randint(0, 9)

while True:
    guess = input("输入数字: ")
    if not guess.isdigit() or len(guess) > 1:
        continue
    guess = int(guess)
    if guess > number:
        print("太大")
        continue
    elif guess < number:
        print("太小")
        continue
    else:
        print("恭喜你！你猜中了！")
        break
