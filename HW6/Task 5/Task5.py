# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли
# объекты имеют одинаковое значение некоторой характеристики, и возвращает True,
# если это так. Если значение характеристики для разных объектов отличается - 
# то False. Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его
# характеристику.

def same_by(characteristic, objects):
    answers = [characteristic(object) for object in objects]
    results = [answers[0] == answers[i] for i in range(len(answers))]
    if objects == []:
        return True
    elif False not in results:
        return True
    else:
        return False

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')