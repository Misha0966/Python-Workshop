from random import randint

def PlayerMove(field, symbol):
    flag = False
    while not flag:
        row = int(input('Enter row => '))
        column = int(input('Enter column => '))
        if field[row][column] == '*':
            field[row][column] = symbol
            flag = True
        else:
            print('Cell is already used. Try one another.')
            flag = False

def PrintField(field):
    for row in field:
        print('\t'.join(row))

def CheckForWinner(field, symbol):
    for i in range(3):
        count = 0
        for j in range(3):
            if field[i][j] == symbol:
                count += 1
        if count == 3:
            return True
    for j in range(3):
        count = 0
        for i in range(3):
            if field[i][j] == symbol:
                count += 1
        if count == 3:
            return True
    count = 0
    for i in range(3):
        if field[i][i] == symbol:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(3):
        if field[i][2 - i] == symbol:
            count += 1
    if count == 3:
        return True
    return False

def TicTacToe(field, playerOne, playerTwo):
    print('Welcome to the Tic-Tac-Toe game!')
    symbolOne = 'X'
    symbolTwo = '0'
    coin = randint(0, 1)
    winFlag = False
    count = 0
    if coin:
        player = playerOne
        symbol = symbolOne
    else:
        player = playerTwo
        symbol = symbolTwo
    PrintField(field)
    while not winFlag:
        print(player + ' your time to play!')
        PlayerMove(field, symbol)
        count += 1
        PrintField(field)
        if CheckForWinner(field, symbol):
            print(player + ' won the game!')
            winFlag = True
        elif not winFlag and count > 8:
            print('Nobody wins... One more game?')
            return None
        else:
            if player == playerOne:
                player = playerTwo
                symbol = symbolTwo
            else:
                player = playerOne
                symbol = symbolOne
        
