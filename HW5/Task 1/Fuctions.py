from random import randint

def PlayerMove(N, player):
    n = 0
    while n < 1 or n > 28:
        print('Player ' + player + '\'s move!')
        try:
            if N > 27:
                n = int(input('Enter number from 1 to 28 => '))
                while (n < 1 or n > 28) and N > 27:
                    print('You should choose from 1 to 28 candies! \n Try again!')
                    n = int(input('Enter number from 1 to 28 => '))
            else:
                n = int(input('Enter number from 1 to ' + str(N) + ' => '))
                while n < 1 or n > N:
                    print('You should choose from 1 to ' + str(N) + ' candies! \n Try again!')
                    n = int(input('Enter number from 1 to ' + str(N) + ' => '))
        except ValueError:
            print('Incorrect Input!')
    print('Player ' + player + ' took ' + str(n) + ' candies!')
    print(str(N - n) + ' candies left!\n')
    return N - n

def CandiesGame(N, player1, player2):
    print('Welcome to Candies Game!')
    print('We are going to fight for ' + str(N) + ' Candies!')
    Ntotal = N
    fate = randint(0, 1)
    if fate:
        player = player1
    else:
        player = player2
    while N > 0:
        N = PlayerMove(N, player)
        if N < 1:
            print('Player ' + player + ' has won all the ' + str(Ntotal) + ' candies!')
            print('Game over!')
        if player == player1:
            player = player2
        else:
            player = player1

def BotMove(N, player = 'Skynet'):
    n = 0
    print(player + '\'s move!')
    if N > 27:
        if N % (28 + 1) == 0:
            print(player + ' said: I know that you can make a mistake!')
            n = randint(1, 28)
        else:
            print(player + ' said: Ha-ha, I will win!')
            n = N - (28 + 1) * (N // (28 + 1))
    else:
        n = N
    print('Player ' + player + ' took ' + str(n) + ' candies!')
    print(str(N - n) + ' candies left!\n')
    return N - n

def CandiesGameVsBot(N, player1):
    print('Welcome to Candies Game!')
    print('We are going to fight for ' + str(N) + ' Candies!')
    Ntotal = N
    player2 = 'SkyNet'
    fate = randint(0, 1)
    if fate:
        player = player1
    else:
        player = player2
    while N > 0:
        if player == player1:
            N = PlayerMove(N, player)
            if N < 1:
                print('Player ' + player + ' has won all the ' + str(Ntotal) + ' candies!')
                print('Game over!')
            player = player2
        else:
            N = BotMove(N, player)
            if N < 1:
                print('Player ' + player + ' has won all the ' + str(Ntotal) + ' candies!\n')
                print('Game over!')
            player = player1