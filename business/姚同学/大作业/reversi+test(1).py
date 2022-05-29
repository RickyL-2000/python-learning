import string
import time
black='X'
white='O'
empty='.'
direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def Init_board():#初始化棋盘
    board=[]
    for x in range(n):
        board.append(['.']*n)
    a=int(n/2-1)
    b=int(n/2)
    board[a][a],board[b][b]="O","O"
    board[a][b],board[b][a]="X","X"
    return board

def Print_board(board):
    global cn
    cn=string.ascii_lowercase[:n]
    print(' ',' '.join(cn))
    for i in range(n):
        print(cn[i],' '.join(board[i]))



def isonboard(x,y):#是否边界
    return 0<=x<=n-1 and 0<=y<=n-1

def check_legal_move(board,color,initx,inity):#落棋是否合法
    flip_pos=[]
    if board[initx][inity]!=empty or not isonboard(initx,inity):#要下的地方已经有棋子/超出棋盘
        return False
    if color==black:
        othercolor=white
    else:
        othercolor=black
        
    for (dx,dy) in direction:#遍历下棋初始位置的八个方向
        X=initx
        Y=inity
        X+=dx
        Y+=dy #落子位置向规定方向移动一个单位
        if isonboard(X,Y) and board[X][Y]==othercolor:#未超出棋盘且是对方颜色棋子，继续在该方向上移动一个单位
            X+=dx
            Y+=dy
            if not isonboard(X,Y):#已超出边界，重新换一个方向
                continue
            while board[X][Y]==othercolor:#只要是对方棋子则继续朝该方向移动
                X+=dx
                Y+=dy
                if not isonboard(X,Y):#超出边界，跳出while循环，返回for循环，换方向
                    break
            if not isonboard(X,Y):
                continue
            if board[X][Y]==color:#当while循环中移动到自己棋子时，说明初始位置有效，不断在这个方向上往回递减
                while X!=initx or Y!=inity:
                    X-=dx
                    Y-=dy
                    flip_pos.append([X,Y]) #记录每个被翻转的对方棋子的位置
    board[initx][inity]=empty #将初始位置清空
    if len(flip_pos)==0:#没有棋可以翻转
        return False
    return flip_pos #返回可以翻转的棋的列表


def human_move(board,playercolor):#玩家下棋
    humpos=input('Enter move for %s (RowCol):'%(playercolor))
    global x
    global y
    x=int(ord(humpos[0])-97)
    y=int(ord(humpos[1])-97)
    if check_legal_move(board,playercolor,x,y)==False:#输入位置有效
        Gameover(board,playercolor,x,y)
        return False
    if getValidMoves(board,playercolor)==[]:
        Gameover(board,playercolor,x,y)
        return False
    else:
        return[x,y]


def makemove(board,color,initx,inity):
    flip_pos=check_legal_move(board,color,initx,inity)
    if flip_pos==False:
        return False
    board[initx][inity]=color
    for x,y in flip_pos:
        board[x][y]=color
    return True

def getValidMoves(board,color):
    validMoves=[]
    for x in range(n):
        for y in range(n):
            if check_legal_move(board,color,x,y)!=False:
                validMoves.append([x,y])
    return validMoves

def bestposition(board):
    initscore=0
    for [x,y] in getValidMoves(mainboard,computercolor):
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
    dupeBoard=Init_board()
    for x in range(n):
        for y in range(n):
            dupeBoard[x][y]=board[x][y]
    return dupeBoard
   
def isoncorner(x,y):#最优位置——角落
    return(x==0 and y==0)or(x==0 and y==n-1)or(x==n-1 and y==0)or(x==n-1 and y==n-1)

def computer_move(board,computercolor):#position score
    possibleMoves=getValidMoves(board,computercolor)#电脑下的棋必须在有效位置
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
        othercolor=playercolor
    if color==playercolor:
        othercolor=computercolor
    blacks=scoreboard(board)['X']#分别计算棋盘上黑白颜色个数
    whites=scoreboard(board)['O']
    
    if getValidMoves(board,color)==[]:#无有效位置下棋
        if getValidMoves(board,othercolor)==[]:#双方都无有效位置可以下棋
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

def saveinfo(board,x,y):#人下棋info
    ti=time.strftime("%Y%m%d %H:%M:%S")
    if entercolor==black:
        Xuser='computer'
        Ouser='player'
    else:
        Xuser='player'
        Ouser='computer'
    Xscore=str(scoreboard(board)['X'])
    Oscore=str(scoreboard(board)['O'])
    if check_legal_move(board,playercolor,x,y):
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
    n=int(input('Enter the board dimension:'))
    global entercolor
    entercolor=input('Computer plays(X/O):')#选择电脑下棋的颜色
    mainboard=Init_board()
    Print_board(mainboard)#打印初始棋盘
    global playercolor
    global computercolor
    if entercolor==black:#【玩家，电脑】
        turn='computer'
        computercolor=black
        playercolor=white
    if entercolor==white:
        turn='player'
        computercolor=white
        playercolor=black

    while True:
        global start
        start=time.time()
        if turn=='player':#人下
            move=human_move(mainboard,playercolor)#下棋,无效位置则False
            valids=getValidMoves(mainboard,playercolor)
            if move in valids:#有效落子，翻转对方棋子，并打印新的棋盘，转为电脑下棋
                makemove(mainboard,playercolor,move[0],move[1])
                Print_board(mainboard)
                turn='computer'
            else:
                print('Invalid move!\n%s player wins!\nGame over.'%(computercolor))
                return False
                         
        if turn=='computer':#电脑下
            if getValidMoves(mainboard,computercolor)==[]:#若电脑无有效位置下棋，gameover
                Gameover(mainboard,computercolor,x,y)
                return False
            else:#电脑有位置可下，则翻转对方棋子，告知落子位置，打印新的棋盘
                x,y=computer_move(mainboard,computercolor)
                makemove(mainboard,computercolor,x,y)
                print('Computer places %s at %s%s'%(computercolor,chr(x+97),chr(y+97)))
                Print_board(mainboard)
                
            if getValidMoves(mainboard,playercolor)==[]:#电脑下完棋后，如果玩家没有有效下棋位置，gameover
                Gameover(mainboard,playercolor,x,y)
                return False
            else:
                turn='player'
        global end
        end=time.time()
        saveinfo(mainboard,x,y)
        
        

main()
