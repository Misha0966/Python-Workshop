# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def ConvertDecToBin(number):

number = int(input('Enter number => '))

answer = ''

while number > 0:
    answer = str(number % 2) + answer
    number = number // 2

print('The result is ' + answer)

