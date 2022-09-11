from random import randint

def InitRandListFloat(minLen, maxLen, minValue, maxValue):
    listLength = randint(minLen, maxLen)
    randList = list()
    for i in range(listLength):
        randList.append(round(randint(minValue, maxValue - 1) + randint(0, 99) / 100, 2))
    return randList

def SubtractMinMax(myList):
    fractionalList = list()
    for element in myList:
        fractionalList.append(round(element - element // 1, 2))
    maxFractional = max(fractionalList)
    minFractional = min(fractionalList)
    return round(maxFractional - minFractional, 2)