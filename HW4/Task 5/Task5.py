# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from Fuctions import *

fileOne = open('PolynomialOne.txt', 'r', encoding='utf8')
fileTwo = open('PolynomialTwo.txt', 'r', encoding='utf8')
output = open('Output.txt', 'w')

monomialsOne = fileOne.read().split(' ')
monomialsTwo = fileTwo.read().split(' ')
monomialsRes = list()

fileOne.close()
fileTwo.close()

monomialsOne = Transmute(monomialsOne)
monomialsTwo = Transmute(monomialsTwo)

monomialsRes = SumPolinomials(monomialsOne, monomialsTwo)

outputRes = ConvertToStr(monomialsRes)
output.write(outputRes)

output.close()