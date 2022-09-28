def Import(file):
    contacts = open(file, 'a')
    name = input('Enter person\'s name: ')
    phone = input('Enter contact\'s phone number: ')
    contacts.write(name + '\t' + phone + '\n')
    contacts.close()
    print('Successfully')

def MergeBooks(fileOne, fileMain):
    yourFile = open(fileOne, 'r')
    contacts = open(fileMain, 'a')
    for line in yourFile:
        contacts.write(line)
    yourFile.close()
    contacts.close()
    print('Successfully')

def PrintBook(file):
    contacts = open(file, 'r')
    for line in contacts:
        print(line)
    contacts.close()
    print('\n===========\n' + 'End of file')

def FindPerson(file):
    name = input('Whom do you want to find? => ')
    contacts = open(file, 'r')
    flag = False
    for line in contacts:
        if name in line:
            print(line)
            flag = True
    if not flag:
        print('Not found')
    contacts.close()