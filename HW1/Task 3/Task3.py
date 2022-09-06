# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = float(input("Enter X coordinate => "))
y = float(input("Enter Y coordinate => "))

if x > 0 and y > 0:
    print("Coordinate quarter 1")
elif x < 0 and y > 0:
    print("Coordinate quarter 2")
elif x < 0 and y < 0:
    print("Coordinate quarter 3")
elif x > 0 and y < 0:
    print("Coordinate quarter 4")
elif x == 0 and y != 0:
    print("Y-axis")
elif y == 0 and x != 0:
    print("X-axis")
else:
    print("Try again")