import string
import time
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]

usercolor = ""
compcolor = ""

def init_board():  # 初始化棋盘
    board = []
    for x in range(n):
        board.append(['.']*n)
    a = int(n/2 - 1)
    b = int(n/2)
    board[a][a], board[b][b] = "O", "O"
    board[a][b], board[b][a] = "X", "X"
    return board


def print_board(board):
    cn = string.ascii_lowercase[:n]
    print(' ', ' '.join(cn))
    for i in range(n):
        print(cn[i], ' '.join(board[i]))


def isonboard(x, y):  # 是否边界
    return 0 <= x <= n-1 and 0 <= y <= n-1


def check_legal_move(board, color, row, col):
    # 落棋是否合法
    othercolor = "X" if color == "O" else "O"
    if board[row][col] != ".":
        return False        
    for dx, dy in direction:    #遍历下棋初始位置的八个方向
        x, y = row, col
        visit_other = False
        while True:
            x, y = x + dx, y + dy
            if isonboard(x, y) and board[x][y] != ".":   # 查看是否在棋盘内，以及是否是空格
                if board[x][y] == othercolor:
                    visit_other = True
                    continue    #遇到对手的棋子，继续在该方向上移动一个单位
                if board[x][y] == color:
                    # 当while循环中移动到自己棋子时，说明初始位置有效
                    if visit_other:
                        return True
                    break
            else:
                break
    return False


def human_move(board, color):  # 玩家下棋
    humpos = input('Enter move for %s (RowCol):' % (color))
    row = int(ord(humpos[0]) - 97)
    col = int(ord(humpos[1]) - 97)
    if check_legal_move(board, color, row, col) is False:  # 输入位置无效
        gameover(board, color, row, col)
        raise
    if get_valid_moves(board, color) == []:
        gameover(board, color, row, col)
        # print('%s player has no valid move.' % (color))
        return False
    else:
        return row, col


def make_move(board, color, row, col):
    flip_pos = check_legal_move(board, color, row, col)
    if flip_pos == False:
        return False
    board[row][col] = color
    othercolor = "X" if color == "O" else "O"
    poses = []
    for dx, dy in direction:
        pos = []
        visit_other = False
        x, y = row, col
        while True:
            x, y = x + dx, y + dy
            if isonboard(x, y) and board[x][y] != ".":
                if board[x][y] == othercolor:
                    visit_other = True
                    pos.append((x, y))
                    continue
                if board[x][y] == color:
                    if visit_other:
                        poses.append(pos)
                    break
            else:
                break
    for pos in poses:
        for x, y in pos:
            board[x][y] = color
    return True


def get_valid_moves(board, color):
    ret = []
    for row in range(n):
        for col in range(n):
            if check_legal_move(board, color, row, col):
                ret.append((row, col))
    return ret


def score_board(board):
    blackscore = whitescore = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'X':
                blackscore += 1
            if board[x][y] == 'O':
                whitescore += 1
    return {'X': blackscore, 'O': whitescore}


def copy_board(board):
    new_board = init_board()
    for x in range(n):
        for y in range(n):
            new_board[x][y] = board[x][y]
    return new_board


def isoncorner(x, y):  # 最优位置——角落
    return(x == 0 and y == 0) or (x == 0 and y == n-1) or (x == n-1 and y == 0) or (x == n-1 and y == n-1)


def position_score(board, row, col, color):
    other_color = "X" if color == "O" else "O"
    dup_board = copy_board(board)
    before = [a for line in board for a in line]
    make_move(dup_board, color, row, col)
    after = [a for line in dup_board for a in line]
    score = before.count(other_color) - after.count(other_color)
    return score


def computer_move(board, color):  # position score
    valid_moves = get_valid_moves(board, color)  # 电脑下的棋必须在有效位置
    if valid_moves:
        max_score = 0
        max_r, max_c = -1, -1
        for row, col in valid_moves:
            score = position_score(board, row, col, color)
            if score > max_score:
                max_score = score
                max_r, max_c = row, col
        return max_r, max_c
    else:
        print('%c player has no valid move.' % color)
        return None


def gameover(board, color, x, y):
    othercolor = usercolor if color == compcolor else compcolor
    blacks = score_board(board)['X']  # 分别计算棋盘上黑白颜色个数
    whites = score_board(board)['O']

    if get_valid_moves(board, color) == []:  # 无有效位置下棋
        if get_valid_moves(board, othercolor) == []:  # 双方都无有效位置可以下棋
            print('Both players have no valid move!')
            if score_board(board)['X'] > score_board(board)['O']:
                print('X : 0 = %d : %d  X player wins!\nGame over.' %
                      (blacks, whites))
            if score_board(board)['X'] < score_board(board)['O']:
                print('X : 0 = %d : %d  O player wins!\nGame over.' %
                      (blacks, whites))
            if score_board(board)['X'] == score_board(board)['O']:
                print('X : 0 = %d : %d  Draw!\nGame over.' % (blacks, whites))
            return False
        else:
            print('%s player has no valid move.' % (color))
            if score_board(board)['X'] > score_board(board)['O']:
                print('X : 0 = %d : %d  X player wins!\nGame over.' %
                      (blacks, whites))
            if score_board(board)['X'] < score_board(board)['O']:
                print('X : 0 = %d : %d  O player wins!\nGame over.' %
                      (blacks, whites))
            if score_board(board)['X'] == score_board(board)['O']:
                print('X:0=%d:%d.Draw!\nGame over.' % (blacks, whites))
            return True
    return False

def check_board(board):
    b = [color for line in board for color in line]
    if set(b) == {'.', 'X', 'O'}:  # 棋盘未满且双方棋子都有
        if get_valid_moves(board, 'X') or get_valid_moves(board, 'O'):  # 双方均有棋可下
            return True
        else:  # 双方均无棋可下
            print('Both players have no valid move.')
            return False
    else:
        return False

def save(board, x, y, duration):  # 人下棋info
    ti = time.strftime("%Y%m%d %H:%M:%S")
    if compcolor == "X":
        Xuser = 'computer'
        Ouser = 'player'
    else:
        Xuser = 'player'
        Ouser = 'computer'
    Xscore = str(score_board(board)['X'])
    Oscore = str(score_board(board)['O'])
    if check_legal_move(board, usercolor, x, y):
        result = 'Human gave up.'
    else:
        result = Xscore+'to'+Oscore
    size = '%d*%d' % (n, n)
    total = '%s\t%d\t%s\t%s\t%s\t%s\n' % (
        ti, int(duration), size, Xuser, Ouser, result)
    with open('reversi.csv', 'a+') as handler:
        handler.write(total)


def main():
    global n
    global usercolor
    global compcolor
    try:
        n=int(input('Enter the board dimension:'))
        if n < 4 or n > 26 or n % 2 != 0:
            raise
        compcolor = input('Computer plays(X/O):')
        if compcolor not in "XO":
            raise
    except Exception:
        print("程序初始化不合法，请重试！")
        return
    mainboard = init_board()
    print_board(mainboard)
    
    if compcolor == "X":
        turn = 'computer'
        usercolor = "O"
    if compcolor == "O":
        turn = 'player'
        usercolor = "X"

    t_start = time.time()
    while True:
        if not check_board(mainboard):
            gameover(mainboard, usercolor if turn == 'player' else compcolor, 0, 0)
            break
        
        if turn == 'player':  # 人下
            try:
                move = human_move(mainboard, usercolor)  # 下棋,无效位置则False
                valids = get_valid_moves(mainboard, usercolor)
                if move in valids:  # 有效落子，翻转对方棋子，并打印新的棋盘，转为电脑下棋
                    make_move(mainboard, usercolor, move[0], move[1])
                    print_board(mainboard)
                else:
                    print('%s player has no valid move.' % (usercolor))
                    continue
                turn = 'computer'
            except Exception:
                print('Invalid move!\n%s player wins!\nGame over.' % (compcolor))
                break

        if turn == 'computer':  # 电脑下
            if get_valid_moves(mainboard, compcolor) == []:  # 若电脑无有效位置下棋，continue
                # gameover(mainboard, compcolor, x, y)
                print('%s player has no valid move.' % (compcolor))
                # continue
            else:  # 电脑有位置可下，则翻转对方棋子，告知落子位置，打印新的棋盘
                x, y = computer_move(mainboard, compcolor)
                make_move(mainboard, compcolor, x, y)
                print('Computer places %s at %s%s' %
                      (compcolor, chr(x+97), chr(y+97)))
                print_board(mainboard)

            # if get_valid_moves(mainboard, usercolor) == []:  # 电脑下完棋后，如果玩家没有有效下棋位置，gameover
            #     gameover(mainboard, usercolor, x, y)
            #     break
            # else:
            turn = 'player'

    t_end = time.time()
    save(mainboard, x, y, t_end-t_start)


main()
