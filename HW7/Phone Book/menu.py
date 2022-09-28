from functions import *

def Menu(path):
    print('Welcome to PhoneBook')
    print('What do you want to do?')
    print('Type 1 if you want to Import contact')
    print('Type 2 if you want to Merge PhoneBooks')
    print('Type 3 if you want to Print PhoneBook')
    print('Type 4 if you want to Find person\'s number')
    print('Type 0 if you want to exit')
    answer = int(input())
    while answer != 0:
        if answer == 1:
            Import(path)
            answer = 0
        if answer == 2:
            MergeBooks(input('Enter file path '), path)
            answer = 0
        if answer == 3:
            PrintBook(path)
            answer = 0
        if answer == 4:
            FindPerson(path)
            answer = 0
    print('Bye')
