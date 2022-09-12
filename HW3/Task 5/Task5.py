# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

N = int(input("Enter N => "))

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

myList = list()

for i in range(N + 1):
    myList.append(Fibonacci(i))
    if i != 0:
        myList.insert(0, -1 * myList[-1])

print(myList)