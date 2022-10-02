import csv

def Import(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    try:
        lastID = str(int(reader[-1][0]) + 1)
    except IndexError:
        lastID = '1'
    contacts.close()
    contacts = open(file, 'a', encoding='utf-8')
    secondName = input('Введите фамилию ученика: ')
    firstName = input('Введите имя ученика: ')
    patronymic = input('Введите отчетство ученика: ')
    classNum = input('Введите класс ученика: ')
    classLiter = input('Введите литеру класса: ')
    birthDate = input('Введите дату рождения ученика: ')
    contacts.write(lastID + ',' + secondName + ',' + firstName + ','  + patronymic + ',' + classNum + ',' + classLiter + ',' + birthDate + '\n')
    contacts.close()
    print('Successfully')

def PrintDataBase(file):
    contacts = open(file, 'r', encoding='utf-8')
    for line in contacts:
        print(line.replace(',', '  '))
    contacts.close()
    print('\n===========\n' + 'Конец базы учеников')

def FindStudent(file):
    secondName = input('Введите фамилию ученика => ')
    firstName = input('Введите имя ученика => ')
    patronymic = input('Введите отчество ученика => ')
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    flag = False
    for i in range(1, len(reader)):
        if secondName in reader[i] and firstName in reader[i] and patronymic in reader[i]:
            print(' | '.join(reader[0]))
            print(' | '.join(reader[i]))
            flag = True
    if not flag:
        print('Not found')
    contacts.close()

def PrintClass(file):
    contacts = open(file, 'r', encoding='utf-8')
    reader = list(csv.reader(contacts))
    classNum = input('Введите номер класса => ')
    classLiter = input('Введите литеру класса => ')
    flag = False
    for i in range(1, len(reader)):
        if classNum in reader[i] and classLiter in reader[i]:
            if not flag:
                print(' | '.join(reader[0]))
            print(' | '.join(reader[i]))
            flag = True
    if not flag:
        print('Ученики не найдены')
    contacts.close()
