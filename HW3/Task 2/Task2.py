# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from Functions import *

taskList = InitRandList(4, 5, 0, 9)

print(taskList)

print(MultCouples(taskList))