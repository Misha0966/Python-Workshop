# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from Functions import *

taskList = InitRandList(5, 9, 0, 10)

print(taskList)

print(ListSumOdd(taskList))
