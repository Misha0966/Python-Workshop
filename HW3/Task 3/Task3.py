# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from Functions import *

taskList = InitRandListFloat(5, 5, 0, 9)

print(taskList)

print(SubtractMinMax(taskList))