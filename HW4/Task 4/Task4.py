# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

k = int(input("Enter k = > "))

coeffs = [randint(0, 100) for i in range(k + 1)]
monomials = list()

print(coeffs[::-1])

output = ''

for i in range(len(coeffs) - 1, -1, -1):
    if coeffs[i] != 0:
        if i == len(coeffs) - 1 and i != 1:
            monomials.append(str(coeffs[i]) + '*x^' + str(i))
        elif i > 1 and i < len(coeffs):
            monomials.append(str(coeffs[i]) + '*x^' + str(i))    
        elif i == 1:
            monomials.append(str(coeffs[i]) + '*x')
        elif i == 0:
            monomials.append(str(coeffs[i]))

if len(coeffs) == 1 or max(coeffs[1:]) == 0:
    output = 'Polynomial doesn\'t exist'
else:
    output = ' + '.join(monomials) + ' = 0'

result = open('result.txt', 'w')
result.write(output)
result.close()