# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from Fuctions import *

N = 58
# playerOne = input('Enter your name => ')
playerOne = 'User'

if N % (28 + 1) != 0:
    print('If you will be the first and you want to win take ' + str(N - (28 + 1) * (N // (28 + 1))) + ' candies!')
    print('If you will be the second - you have no chances to win, Sorry...\n')
else:
    print('If you will be the first - you have no chances to win, Sorry...\n')

CandiesGameVsBot(N, playerOne)

# playerTwo = 'Tom'
# # CandiesGame(N, playerOne, playerTwo)
