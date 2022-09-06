# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Enter day number from 1 to 7 => "))

if day in range(1,6):
    print("It's time to work!")
elif day in range(6,8):
    print("Have a rest")
else:
    print("Incorrect input, please try again")