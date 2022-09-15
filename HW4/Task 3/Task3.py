# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

initialList = list()
resultList = list()

for i in range(10):
    initialList.append(randint(1, 10))

print(initialList)

for item in initialList:
    if initialList.count(item) == 1:
        resultList.append(item)

print(resultList)