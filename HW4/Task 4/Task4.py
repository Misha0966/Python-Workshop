# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

k = int(input("Enter k = > "))

coeffs = [randint(0, 1) for i in range(k + 1)]

print(coeffs)

output = ''

for i in range(len(coeffs) - 1, -1, -1):
    if coeffs[i] != 0 and i == len(coeffs) - 1:
        output += str(coeffs[i]) + '*x^' + str(i)
    elif coeffs[i] != 0 and i > 1 and i < len(coeffs):
        output += ' + ' + str(coeffs[i]) + '*x^' + str(i)    
    elif coeffs[i] != 0 and i == 1:
        output += ' + ' + str(coeffs[i]) + '*x'
    elif coeffs[i] != 0 and i == 0:
        output += ' + ' + str(coeffs[i])

output += ' = 0'


print(output)
    


# if 

# for i in range(k, -1, -1):
#     output += str(randint(0, 100)) + '*' + 'x**' + str(i) + ' '

# print(output)