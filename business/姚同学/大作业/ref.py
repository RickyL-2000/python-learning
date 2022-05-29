import time
import string

black='X'
white='O'
empty='·'
matrix=[]
board=[]
position=''

s=int(input('Enter the board dimension(4~26, odd number):'))
while s<4 or s>26 or s%2!=0:
    print('your input is wrong!')
    s=int(input('Enter the board dimension(4~26, odd number):'))

color_human=str(input('choose white or black:'))
while color_human!='white' and color_human!='black':
    print('your input is wrong!')
    color_human=str(input('choose white or black:'))
if color_human=='white':
    color_human=white
    color_computer=black
    Xplayer='computer'
    Oplayer='human'
    print('Computer plays (X/O):%s'%(black))
if color_human=='black':
    color_human=black
    color_computer=white
    Xplayer='human'
    Oplayer='computer'
    print('Computer plays (X/O):%s'%(white))
    
direction = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
letter=[chr(i) for i in range(97,123)]
num_letter=enumerate(letter)

#初始化棋盘 check!
def init_board(n):
    for i in range(0,n+1):
        row=[]
        if i==0:
            for j in range(0,n+1):
                if j==0:
                    row.append('')
                if j!=0:
                    row.append('%s'%(letter[j-1]))
        if i==n/2:
            for j in range(0,n+1):
                if j==0:
                    row.append(letter[i-1])
                if j!=n/2 and j!=(n+2)/2 and j!=0:
                    row.append(empty)
                if j==n/2:
                    row.append(white)
                if j==(n+2)/2:
                    row.append(black)
        if i==(n+2)/2:
            for j in range(0,n+1):
                if j==0:
                    row.append(letter[i-1])
                if j!=n/2 and j!=(n+2)/2 and j!=0:
                    row.append(empty)
                if j==n/2:
                    row.append(black)
                if j==(n+2)/2:
                    row.append(white)
        if i>0 and i!=n/2 and i!=(n+2)/2:
            for j in range(0,n+1):
                if j==0:
                    row.append(letter[i-1])
                if j!=0:
                    row.append(empty)
        matrix.append(row)

#打印棋盘 check!
def print_board(board):
    board=[]
    for m in range(0,s+1):
        for n in range(0,s+1):
            board.append(matrix[m][n])
        board.append('\n')
    print(' ',' '.join(board))
    
#找出棋盘上还空着的位置
def all_directions(color):
    for row in range(0,s):
        for col in range(0,s):
            if matrix[row][col]==empty:
                return True
            else:
                return False

#定义颜色 check!
def judge_color(color):
    global color_oppo
    if color==black:
        color_oppo=white
    if color==white:
        color_oppo=black
    return color_oppo

#检查该颜色的棋子是否能在(row,col)位置上落子 check!
def check_legal_move(row,col,color):
    judge_color(color)
    color_oppo=judge_color(color)
    for (x,y) in direction:
        if row+x>s or col+y>s:
            continue
        if matrix[row+x][col+y]==color_oppo and matrix[row][col]==empty:
            i=0
            while i>=0:
                if row+x+i*x>s or col+y+i*y>s:
                    break
                elif matrix[row+x+i*x][col+y+i*y]==color:
                    return True
                elif matrix[row+x+i*x][col+y+i*y]==color_oppo:
                    i=i+1
                else:
                    break
            
#收集所有合法落子位置(用于电脑下棋和计分以及判断用户是否还能下棋和游戏是否可以结束) check!
def all_legal_position(color):
    global okposition
    okposition=[]
    for row in range(1,s+1):
        for col in range(1,s+1):
            if check_legal_move(row,col,color):
                okposition.append((row,col))
    return okposition
    
#计算会被翻转颜色的棋的个数 
def count_flip(row,col,color):
    global num
    num=0
    for (x,y) in direction:
        if (row+x)>s or (col+y)>s:
            continue
        else:
            if matrix[row+x][col+y]==color_oppo:
                i=2
                while i>1:
                    if (row+i*x)>s or (col+i*y)>s:
                        break
                    else:
                        if matrix[row+i*x][col+i*y]==color:
                            num=num+i-1
                            i=1
                            break
                        elif matrix[row+i*x][col+i*y]==empty:
                            break
                        elif matrix[row+i*x][col+i*y]==color_oppo:
                            i=i+1
                        else:
                            break 
            else:   
                i=1
    return num,matrix
                            
#翻转棋的颜色 check!
def flip(row,col,color):
    for (x,y) in direction:
        if (row+x)>s or (col+y)>s:
            continue
        else:
            if matrix[row+x][col+y]==color_oppo:
                i=2
                while i>1:
                    if (row+i*x)>s or (col+i*y)>s:
                        break
                    else:
                        if matrix[row+i*x][col+i*y]==color:
                            for j in range(1,i):
                                matrix[row+j*x][col+j*y]=color
                            num=i-1
                            break
                        elif matrix[row+i*x][col+i*y]==empty:
                            break
                        elif matrix[row+i*x][col+i*y]==color_oppo:
                            i=i+1
                        else:
                            break
            else:   
                i=1

#电脑下棋并告知对方下棋位置 check!
def computer_move(color):
    matrix[row][col]=color
    print('Computer places %s at %s.'%(color_computer,position))


#计算分值并选定位置 check!
def position_score(color):
    global row1,row,col1,col,position
    single_move_score=[]
    k=0
    max1=0
    for (row,col) in okposition:
        count_flip(row,col,color)
        single_move_score.append(num)
    for k in range(len(single_move_score)):
        if single_move_score[k]>max1:
            max1=single_move_score[k]
            k=k+1
    for (row,col) in okposition:
        count_flip(row,col,color)
        if num==max1:
            break
    row1=letter[row-1]
    col1=letter[col-1]
    position='%s%s'%(row1,col1)
    return position

#让玩家确定落子位置并下棋 check!
def human_move(color):
    global move1,move2,row,col,t
    t=False
    position=str(input('Enter move for %s (RowCol):'%(color)))
    position=','.join(position)
    row,col=position.split(',')
    for i,row1 in enumerate(letter):
        if row1==row:
            row=i+1
            break
    for j,col1 in enumerate(letter):
        if col1==col:
            col=j+1
            break
    move1=row
    move2=col
    all_legal_position(color)
    for (x,y) in okposition:
        if (move1,move2)==(x,y):
            matrix[move1][move2]=color
            t=True
    return matrix,t


#检查游戏是否结束 False代表游戏结束
def check_board(color):
    global result
    a0=0 #检查棋盘是否已满
    a1=0 #检查是否还有黑子
    a2=0 #检查是否还有白子
    result=True
    for i in range(1,s+1):
        for j in range(1,s+1):
            if matrix[i][j]==empty:
                a0=1
            elif matrix[i][j]==black:
                a1=1
            elif matrix[i][j]==white:
                a2=1
    if a0==0: #棋盘满了
        gameover('count')
    elif all_legal_position(color)==[] and all_legal_position(color_oppo)==[]: #双发均无子可下
        gameover('count')
    elif a1==0 and a2==1: #只剩白棋
        gameover('white wins')
    elif a1==0 and a2==1: #只剩黑棋
        gameover('black wins')
    elif color==color_human and t==False: #人类落子非法
        gameover('Human gave up.')
    if result:
        print_board(board)
    return result
    
#游戏结束，统计得分，判断胜负
def gameover(abc):
    global result,result_final
    if abc=='count': #数双方棋子个数，判断胜负
        num_black=0
        num_white=0
        for i in range(1,s+1):
            for j in range(1,s+1):
                if matrix[i][j]==black:
                    num_black=num_black+1
                elif matrix[i][j]==white:
                    num_white=num_white+1
        if num_black>num_white:
            print_board(board)
            print('Both players have no valid move.')
            print('Game over.')
            print('X : O = %d : %d'%(num_black,num_white))
            print('X player wins!')
            result_final='X : O = %d : %d'%(num_black,num_white)
        elif num_black<num_white:
            print_board(board)
            print('Both players have no valid move.')
            print('Game over.')
            print('X : O = %d : %d'%(num_black,num_white))
            print('O player wins!')
            result_final = 'X : O = %d : %d' % (num_black, num_white)
        else:
            print_board(board)
            print('Both players have no valid move.')
            print('Game over.')
            print('Draw!')
            result_final='Draw!'
        result=False
    elif abc=='white wins':
        print_board(board)
        print('Game over.')
        print('O player wins!')
        result_final='X player has no check left.'
        result=False
    elif abc=='black wins':
        print_board(board)
        print('Game over.')
        print('X player wins!')
        result_final = 'O player has no check left.'
        result=False
    elif abc=='Human gave up.':
        print('Invalid move.')
        print('Game over.')
        print('Computer wins!')
        result_final = 'Human gave up.'
        result=False
    return result,result_final

#将相关信息写入日志
def saveinfo():
    time2=time.time()
    time_last=time2-time1
    file=open('Reversi.csv','a+')
    content=str(time1)+','+str(time_last)+','+str(s)+'*'+str(s)+','+Xplayer+','+Oplayer+','+result_final
    file.write(content)
    file.write('\n')
    file.close()


##############################开始下棋###################################    
time1=time.time()
init_board(s)
print_board(board)
judge_color(color_human)
round=1
result=True
while round>0 and result:
    if color_human is black:
        if round%2!=0:
            all_legal_position(color_human)   #人下棋
            if okposition!=[]:
                human_move(color_human)    #人下棋
                flip(row,col,color_human)    #人下棋
                check_board(color_human)    #人下棋
                round=round+1
            else:
                check_board(color_computer)
                print('%s player has no valid move.' % (color_human))
                round=round+1
        elif round%2==0:
            all_legal_position(color_computer)   #电脑下棋
            if okposition!=[]:
                position_score(color_computer)   #电脑下棋
                computer_move(color_computer)   #电脑下棋
                flip(row,col,color_computer) #电脑下棋
                check_board(color_computer)
                round=round+1
            else:
                check_board(color_human)
                print('%s player has no valid move.' % (color_computer))
                round=round+1
    if color_computer is black:
        if round%2!=0:
            all_legal_position(color_computer)   #电脑下棋
            if okposition!=[]:
                position_score(color_computer)   #电脑下棋
                computer_move(color_computer)   #电脑下棋
                flip(row,col,color_computer)   #电脑下棋
                check_board(color_computer)
                round=round+1
            else:
                check_board(color_human)
                print('%s player has no valid move.' % (color_computer))
                round=round+1
        elif round%2==0:
            all_legal_position(color_human)   #人下棋
            if okposition!=[]:
                human_move(color_human)    #人下棋
                flip(row,col,color_human)    #人下棋
                check_board(color_human)    #人下棋
                round=round+1
            else:
                check_board(color_computer)
                print('%s player has no valid move.' % (color_human))
                round=round+1
saveinfo()





