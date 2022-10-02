from functions import *

def Menu(path):
    print('Добро пожаловать в базу данных учеников')
    print('Что вы хотите сделать?')
    print('Введите 1 если вы хотите внести нового ученика в базу')
    print('Введите 2 если вы хотите вывести на экран всех учеников')
    print('Введите 3 если вы хотите найти ученика по ФИО')
    print('Введите 4 если вы хотите вывести на экран всех учеников определенного класса')
    print('Введите 0 если вы хотите завершить работу')
    answer = int(input())
    while answer != 0:
        if answer == 1:
            Import(path)
            answer = 0
        if answer == 2:
            PrintDataBase(path)
            answer = 0
        if answer == 3:
            FindStudent(path)
            answer = 0
        if answer == 4:
            PrintClass(path)
            answer = 0
    print('Приходите еще!')
