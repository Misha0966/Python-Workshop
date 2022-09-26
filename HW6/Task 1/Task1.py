# Вам уже приходилось писать таблицу множения. Но на этот раз вас попросили
# сделать в плюс к таблице умножения еще и таблицн словжения а также таблицу 
# возведения в степень.
# Чтобы не копировать один и тот же код и обощить все три функции до единой
# функции рисования таблиц (бинарных) арифметических операций, напишите функцию
# print_operation_table(operation, num_rows=9, num_columns=9), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля)

# Примечание: бинарной операцией называется любая операция, у которой ровно два
# аргумента, как, например у операции умножения.

def print_operation_table(operation, num_rows=5, num_columns=5):
    matrix = list()
    for i in range(num_rows):
        matrix.append(list())
        for j in range(num_columns):
            if i == 0:
                matrix[i].append(str(j + 1))
            elif  i != 0 and j == 0:
                matrix[i].append(str(i + 1))
            else:
                matrix[i].append(str(operation((i + 1), (j + 1))))
        print('\t'.join(matrix[i]))

print_operation_table(lambda x, y: x + y)
print()
print_operation_table(lambda x, y: x * y)
print()
print_operation_table(lambda x, y: x ** y)
