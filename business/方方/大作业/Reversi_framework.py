import string
import time

board = []  # 棋盘
n = 0       # 棋盘的行数/列数，棋盘大小=n*n
# 方向偏移量
direction = ((-1, -1), (-1, 0), (-1, 1),  # NW, N, NE
             (0, -1), (0, 1),             # W, E
             (1, -1), (1, 0), (1, 1))     # SW, S, SE


def main():
    start = time.time()
    global n
    compcolor = ''
    
    try:
        n = int(input('Enter the board dimension: '))
        if n < 4 or n > 26 or n%2 != 0:
            raise

        compcolor = input('Computer plays (X/O) : ')
        if compcolor != 'X' and compcolor != 'O':
            raise
    except Exception:
        print('程序初始化不合法，请重试！')
        return

    init_board()
    if compcolor == 'O':
        usercolor = 'X'
        turn = 'human'
    else:
        usercolor = 'O'
        turn = 'computer'

    print_board()

    invalid = False  # 初始状态: 用户没有落子在非法位置
    while check_board():   # 游戏尚未结束
        if turn == 'human':    # 轮到用户下棋
            isValid = human_move(usercolor)
            if not isValid:
                invalid = True  # 用户落子在非法位置
                break
            turn = 'computer'
        else:
            computer_move(compcolor)
            turn = 'human'

    end = time.time()
    gameover(start, end, invalid, compcolor)


def init_board():
    for i in range(n):
        line = []
        for j in range(n):
            line.append('.')
        board.append(line)
    center = n//2-1
    board[center][center] = 'O'
    board[center+1][center+1] = 'O'
    board[center][center+1] = 'X'
    board[center+1][center] = 'X'


def print_board():
    cn = string.ascii_lowercase[:n]
    print(' ', ' '.join(cn))
    for i in range(n):
        print(cn[i], ' '.join(board[i]))


def ch2i(ch):
    return ord(ch) - ord('a')


def i2ch(i):
    return chr(i + ord('a'))


# 检查某个特定位置(row, col)是否在棋盘内
def position_in_bounds(row, col):
    return 0 <= row < n and 0 <= col < n


# 判断游戏是否结束
def check_board():
    '''判断游戏是否结束。如果结束，则返回False，否则返回True'''
    b = [color for line in board for color in line]
    if set(b) == {'.', 'X', 'O'}:  # 棋盘未满且双方棋子都有
        if get_all_moves('X') or get_all_moves('O'):  # 双方均有棋可下
            return True
        else:  # 双方均无棋可下
            print('Both players have no valid move.')
            return False
    else:
        return False



# 检查颜色为color的棋子落子(row, col)是否有效
def check_legal_move(row, col, color):
    ''' 检查颜色为color的棋子落子(row, col)是否有效。
        输入：落子的位置，行row, 列col，以及颜色color
        输出：如果有效，则返回True，否则返回False。 '''
    # ====== Begin =======







    # ====== End =======


# 获得颜色为color的棋子在棋盘上所有的合法落子位置
def get_all_moves(color):
    avail = []
    for row in range(n):
        for col in range(n):
            if check_legal_move(row, col, color):
                avail.append((row, col))
    return avail


# 翻转(row, col)8个方向上符合条件的棋子
def flip(row, col, color):
    '''在(row, col)位置的棋格落子color颜色棋子后，翻转8个方向上的对手棋子
        该函数不需要返回值
    '''
    # ====== Begin =======







    # ====== End =======


# 用户下棋
def human_move(color):
    avail = get_all_moves(color)
    if avail:
        pos = input('Enter move for %c (RowCol): ' % color)
        row, col = map(ch2i, pos)
        if check_legal_move(row, col, color):
            board[row][col] = color     # 下棋
            flip(row, col, color)       # 翻棋
            print_board()               # 输出棋盘
            return True
        else:
            print('Invalid move.')  # 落子在非法位置, 游戏结束
            return False
    else:
        print('%c player has no valid move.' % color)  # 没有可落子位置, 本轮弃权
        return True


# 计算(row, col)位置的得分
def position_score(row, col, color):
    ''' 为计算机棋手计算(row, col)位置落子颜色为color的棋子，得分是多少。计算规则参见“计算机选择落子位置的策略”。
        输入：落子的位置，行row, 列col，以及颜色color
        输出：返回整型分值score '''
    score = 0
    # ====== Begin =======





    # ====== End =======            
    return score


# 计算机下棋
def computer_move(color):
    avail = get_all_moves(color)
    if avail:
        maxScore = 0
        maxRow, maxCol = -1, -1
        for (row, col) in avail:
            score = position_score(row, col, color)
            if score > maxScore:
                maxScore = score
                maxRow, maxCol = row, col
        board[maxRow][maxCol] = color
        flip(maxRow, maxCol, color)
        print('Computer places %c at %c%c.' % (color, i2ch(maxRow), i2ch(maxCol)))
        print_board()
    else:
        print('%c player has no valid move.' % color)  # 没有可落子位置, 本轮弃权


# 统计双方得分并输出游戏结果, 将相关信息写入日志文件
def gameover(start, end, invalid, compcolor):
    print('Game over.')
    if invalid:
        print('%c player wins.' % compcolor)
    else:
        blackNum, whiteNum = 0, 0
        for line in board:
            blackNum += line.count('X')
            whiteNum += line.count('O')

        print('X : O = %d : %d' % (blackNum, whiteNum))
        if blackNum == whiteNum:
            print('Draw!')
        elif blackNum > whiteNum:
            print('X player wins.')
        else:
            print('O player wins.')

    Bplayer = 'computer' if compcolor == 'X' else 'human'
    Wplayer = 'computer' if compcolor == 'O' else 'human'
    with open('reversi.csv', 'a+') as handler:
        handler.write("{},{},{}*{},{},{},".format(time.strftime('%Y%m%d %H:%M:%S'),
                                                  int(end-start), n, n,
                                                  Bplayer, Wplayer))
        if invalid:
            handler.write('Human gave up.\n')
        else:
            handler.write('%d to %d\n' % (blackNum, whiteNum))


if __name__ == '__main__':
    main()
