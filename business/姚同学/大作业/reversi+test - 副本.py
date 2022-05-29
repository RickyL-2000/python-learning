import string
import time
black='X'
white='O'
empty='.'
direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def init_board():#初始化棋盘
    board=[]
    for x in range(n):
        board.append(['.']*n)
    a=int(n/2-1)
    b=int(n/2)
    board[a][a],board[b][b]="O","O"
    board[a][b],board[b][a]="X","X"
    return board

def print_board(board):
    cn=string.ascii_lowercase[:n]
    print(' ', ' '.join(cn))
    for i in range(n):
        print(cn[i],' '.join(board[i]))

def isonboard(x, y):    # 查看边界条件
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
    return False

def human_move(board, usercolor):#玩家下棋
    valid_moves = get_all_moves(board, usercolor)
    if valid_moves:
        pos = input('Enter move for %s (RowCol): ' %(usercolor))
        row = int(ord(pos[0]) - 'a')
        col = int(ord(pos[1]) - 'a')
        if check_legal_move(board, usercolor, row, col):
            return row, col
        else:
            print('Invalid move.')
            return None
    else:
        print('%c player has no valid move.' % usercolor)  # 没有可落子位置, 本轮弃权
        return None

def makemove(board, color, initx, inity):
    flip_pos=check_legal_move(board,color,initx,inity)
    if flip_pos==False:
        return False
    board[initx][inity]=color
    for x,y in flip_pos:
        board[x][y]=color
    return True

def get_all_moves(board, color):
    ret = []
    for row in range(n):
        for col in range(n):
            if check_legal_move(board, color, row, col):
                ret.append([row, col])
    return ret

def bestposition(board):
    initscore=0
    for [x,y] in get_all_moves(mainboard,computercolor):
        flip_posi=check_legal_move(mainboard,computercolor,x,y)
        score=len(flip_posi)
                
def scoreboard(board):
    blackscore=whitescore=0
    for x in range(n):
        for y in range(n):
            if board[x][y]=='X':
                blackscore+=1
            if board[x][y]=='O':
                whitescore+=1
    return {'X':blackscore,'O':whitescore}

def copy(board):
    dupeBoard=init_board()
    for x in range(n):
        for y in range(n):
            dupeBoard[x][y]=board[x][y]
    return dupeBoard
   
def isoncorner(x,y):#最优位置——角落
    return(x==0 and y==0)or(x==0 and y==n-1)or(x==n-1 and y==0)or(x==n-1 and y==n-1)

def computer_move(board,computercolor):#position score
    possibleMoves=get_all_moves(board,computercolor)#电脑下的棋必须在有效位置
    for x,y in possibleMoves:#电脑先下四角的棋子
        if isoncorner(x,y):
            return [x,y]
    bestscore = -1
    for x,y in possibleMoves:#电脑选最高分值的位置下棋
        boardcopy=copy(board)#new def#获取拷贝
        makemove(boardcopy,computercolor,x,y)
        score=scoreboard(boardcopy)[computercolor]
        if score > bestscore:
            bestMove=[x,y]
            bestscore=score
    return bestMove
    

def Gameover(board,color,x,y):
    if color==computercolor:
        othercolor=usercolor
    if color==usercolor:
        othercolor=computercolor
    blacks=scoreboard(board)['X']#分别计算棋盘上黑白颜色个数
    whites=scoreboard(board)['O']
    
    if get_all_moves(board,color)==[]:#无有效位置下棋
        if get_all_moves(board,othercolor)==[]:#双方都无有效位置可以下棋
            print('Both players have no valid move!')
            if scoreboard(board)['X']>scoreboard(board)['O']:
                print('X:0=%d:%d.X player wins!\nGame over.'%(blacks,whites))
            if scoreboard(board)['X']<scoreboard(board)['O']:
                print('X:0=%d:%d.O player wins!\nGame over.'%(blacks,whites))
            if scoreboard(board)['X']==scoreboard(board)['O']:
                print('X:0=%d:%d.Draw!\nGame over.'%(blacks,whites))
        else:
            print('%s player has no valid move.'%(color))
            if scoreboard(board)['X']>scoreboard(board)['O']:
                print('X:0=%d:%d.X player wins!\nGame over.'%(blacks,whites))
            if scoreboard(board)['X']<scoreboard(board)['O']:
                print('X:0=%d:%d.O player wins!\nGame over.'%(blacks,whites))
            if scoreboard(board)['X']==scoreboard(board)['O']:
                print('X:0=%d:%d.Draw!\nGame over.'%(blacks,whites))
            
    return False

def saveinfo(board,x,y): #人下棋info
    ti=time.strftime("%Y%m%d %H:%M:%S")
    if compcolor ==black:
        Xuser='computer'
        Ouser='player'
    else:
        Xuser='player'
        Ouser='computer'
    Xscore=str(scoreboard(board)['X'])
    Oscore=str(scoreboard(board)['O'])
    if check_legal_move(board,usercolor,x,y):
        result='Human gave up.'
    else:
        result=Xscore+'to'+Oscore
    duration=end-start
    size='%d*%d'%(n,n)
    total='%s\t%d\t%s\t%s\t%s\t%s\n'%(ti,int(duration),size,Xuser,Ouser,result)
    with open ('reversi.csv','a+') as handler:
        handler.write(total)

def main():
    global n
    global usercolor
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
        if turn == 'player': #人下
            move = human_move(mainboard, usercolor) # 下棋，无效位置则None
            
            
            valids = get_all_moves(mainboard, usercolor)
            if move in valids:#有效落子，翻转对方棋子，并打印新的棋盘，转为电脑下棋
                makemove(mainboard,usercolor,move[0],move[1])
                print_board(mainboard)
                turn='computer'
            else:
                print('Invalid move!\n%s player wins!\nGame over.'%(computercolor))
                return False
                         
        if turn=='computer':#电脑下
            if get_all_moves(mainboard,computercolor)==[]:#若电脑无有效位置下棋，gameover
                Gameover(mainboard,computercolor,x,y)
                return False
            else:#电脑有位置可下，则翻转对方棋子，告知落子位置，打印新的棋盘
                x,y=computer_move(mainboard,computercolor)
                makemove(mainboard,computercolor,x,y)
                print('Computer places %s at %s%s'%(computercolor,chr(x+97),chr(y+97)))
                print_board(mainboard)
                
            if get_all_moves(mainboard,usercolor)==[]:#电脑下完棋后，如果玩家没有有效下棋位置，gameover
                Gameover(mainboard,usercolor,x,y)
                return False
            else:
                turn='player'

    t_end=time.time()
    saveinfo(mainboard,x,y)
        
        

main()
