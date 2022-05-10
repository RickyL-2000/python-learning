import random
import time

LINEPERIMAGE = 9  #Every LINEPERIMAGE is a perfect picture of hangman

# We intentionally add LINES below: it's too long
LINES = ''' ______
|  |
|  
| 
|  
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| 
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| /  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| / \ 
|_____
|     |____
|__________|

'''

WIN_MESSAGE = "YOU WIN!"
LOSE_MESSAGE = "YOU LOSE!"

def get_hangman(mistakes=6):
    '''
    print hangman : from 0 (hang) to 6 (hanged)
    '''

    lines = LINES.split('\n')
    start = mistakes * LINEPERIMAGE
    return lines[start: start+ LINEPERIMAGE]

def print_board(hangman, word_display, gameover=""):
    length = max(len(LOSE_MESSAGE), len(word_display)) * 2 - 1 + 4
    for i, l in enumerate(hangman):
        line = " "*length + l
        if i == 5:
            if gameover:
                start = int((length - (len(gameover)*2-1)) // 2)
                end = start + int(len(gameover)*2-1)
                line = line[:start] + " ".join(gameover) + line[end:]
            else:
                start = int((length - (len(word_display)*2-1)) // 2)
                end = start + int(len(word_display)*2-1)
                line = line[:start] + " ".join(word_display) + line[end:]
        print(line)

def main():
    shutdown = False
    # keep playing (replaying)
    while not shutdown:
        with open("words.txt") as f:
            words = f.read().strip().split()
        # random.seed(int(t_start))
        word = random.choice(words)
        word_display = "_"*len(word)
        guess_seq = ""
        mistakes = 0
        gameover = ""

        # game start
        t_start = time.time()
        print("HANGMAN...Game on!")
        print_board(get_hangman(mistakes), word_display, gameover)
        while True:
            char = input("Guess a letter:").strip()
            if len(char) > 1 or (not char.isalpha()):
                print("Invalid input. Please try again.")
                continue
            guess_seq += char
            if char in word and char not in word_display:
                idx = -1
                while True:
                    idx = word.find(char, idx+1)
                    if idx == -1:
                        break
                    word_display = word_display[:idx] + char + word_display[idx+1:]
            else:
                mistakes += 1

            if mistakes == 6:
                gameover = LOSE_MESSAGE
            elif word == word_display:
                gameover = WIN_MESSAGE
            
            print(f"mistakes: {mistakes}")
            print_board(get_hangman(mistakes), word_display, gameover)
            if gameover:
                t_end = time.time()
                print(f"The secret word is {word}, you guess via sequence {guess_seq}. And {gameover}")
                # save
                with open('reversi.csv', 'a+') as f:
                    f.write(f"{time.strftime('%Y%m%d')},{t_end - t_start:.02f},{word},{guess_seq}\n")
                # replay or not
                while True:
                    key = input("Continue game(C/c: continue, Q/q: quit)? ").strip()
                    if not (key in "YyCcQq" and len(key) == 1):
                        continue
                    break
                if key in "Qq":
                    print("Bye...Game over!!!")
                    shutdown = True
                break
                
if __name__ == '__main__':
    main()
