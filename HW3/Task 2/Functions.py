from random import randint

def InitRandList(minLen, maxLen, minValue, maxValue):
    listLength = randint(minLen, maxLen)
    randList = list()
    for i in range(listLength):
        randList.append(randint(minValue, maxValue))
    return randList

def MultCouples(myList):
    mult = list()
    if len(myList) % 2 == 0:
        for i in range(0, len(myList) // 2):
            mult.append(myList[i] * myList[len(myList) - 1 - i])
        return mult
    else:
        for i in range(0, len(myList) // 2 + 1):
            mult.append(myList[i] * myList[len(myList) - 1 - i])
        return mult
