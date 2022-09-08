# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.


N = int(input('Enter N => '))

min_div = -1

for i in range(N, 1, -1):
    if N % i == 0:
        min_div = i

print(min_div)
