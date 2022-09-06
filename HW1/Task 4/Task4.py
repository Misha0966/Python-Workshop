# Напишите программу, которая по заданному номеру четверти 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Enter quarter number (1-4) => "))

if quarter == 1:
    print("X > 0, Y > 0")
elif quarter == 2:
    print("X < 0, Y > 0")
elif quarter == 3:
    print("X < 0, Y < 0")
elif quarter == 4:
    print("X > 0, Y < 0")
else:
    print("Try again")