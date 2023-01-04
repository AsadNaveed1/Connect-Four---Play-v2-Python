def createBoard():
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)

def makeMove():
    import sys
    validmove = False
    while validmove == False:
        move = input('player' + player + ' (col #): ')

        if move == 'e':
            print("bye")
            sys.exit()
            break
        else:
            Col = int(move)
            RW = len(board)
            CL = len(board[0])
            if Col in range(0, CL):
                Column = []
                for i in range(RW):
                    Column.append(board[i][Col])
                if Column.count('·') != 0:
                    for R in range(RW):
                        if board[R][Col] == '·':
                            board[R][Col] = player
                            break
                        elif board[R][Col] != '·' and board[R + 1][Col] == '·':
                            board[R + 1][Col] = player
                            break
                    validmove = True
        if validmove == False: printBoard(board)

def testOwin(board):
    colH = len(board[0])
    rowL = len(board)

    count=0
    for i in range(rowL):
        for y in range(colH-3):
            if board[i][y] == "O" and board[i][y + 1] == "O" and board[i][y + 2] == "O" and board[i][y + 3] == "O":
                return True


    for i in range(rowL - 3):
        for j in range(3, colH):
            if board[i][j] == "O" and board[i + 1][j - 1] == "O" and board[i + 2][j - 2] == "O" and board[i + 3][j - 3] == "O":
                return True

    for i in range(rowL - 3):
        for j in range(colH - 3):
            if board[i][j] == "O" and board[i+1][j+1] =="O" and board[i+2][j+2] == "O" and board[i+3][j+3] == "O":
                return True

    for i in range(colH):
        for j in range(rowL - 3):
            if board[j][i] == "O" and board[j + 1][i] == "O" and board[j + 2][i] == "O" and board[j + 3][i] == "O":
                return True
    return False

def testXwin(board):
    colH = len(board[0])
    rowL = len(board)

    count = 0
    for i in range(rowL):
        for y in range(colH - 3):
            if board[i][y] == "X" and board[i][y + 1] == "X" and board[i][y + 2] == "X" and board[i][y + 3] == "X":
                return True

    for i in range(rowL - 3):
        for j in range(3, colH):
            if board[i][j] == "X" and board[i + 1][j - 1] == "X" and board[i + 2][j - 2] == "X" and board[i + 3][j - 3] == "X":
                return True

    for i in range(rowL - 3):
        for j in range(colH - 3):
            if board[i][j] == "X" and board[i + 1][j + 1] == "X" and board[i + 2][j + 2] == "X" and board[i + 3][j + 3] == "X":
                return True

    for i in range(colH):
        for j in range(rowL - 3):
            if board[j][i] == "X" and board[j + 1][i] == "X" and board[j + 2][i] == "X" and board[j + 3][i] == "X":
                return True
    return False


def draw(board):
    colH = len(board[0])
    rowL = len(board)
    count=0
    for i in range(rowL):
        for j in range(colH):
            if board[i][j]== "X":
                count+=1
            if board[i][j]== "O":
                count+=1
        if count== rowL*colH:
            return True


def invalidmove(board, player, col):
    r = len(board)
    count=0
    boardHeight = len(board[0])
    for row in range(r):
        for t in range(boardHeight):
            if board[row+t][col] != '·':
                count+=1
            if count==boardHeight:
                return True
            else:
                break

board = createBoard()
printBoard(board)
player = 'X'
while True:

    if makeMove( )==True:
        break

    if testOwin(board) == True:
        printBoard(board)
        print("Player O has won!")
        break
    if testXwin(board) == True:
        printBoard(board)
        print("Player X has won!")
        break
    if draw(board):
        printBoard(board)
        print("Draw!")
        break

    printBoard(board)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
print('bye')
