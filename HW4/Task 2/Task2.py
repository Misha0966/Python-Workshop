# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Enter number => '))

def MultList(number):
    resultList = list()
    i = 2
    while number != 1:
        if number % i == 0:
            resultList.append(i)
            number /= i
        else:
            i += 1
    return resultList

print(MultList(N))
