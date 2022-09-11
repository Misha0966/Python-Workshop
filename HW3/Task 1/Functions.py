from random import randint

def InitRandList(minLen, maxLen, minValue, maxValue):
    listLength = randint(minLen, maxLen)
    randList = list()
    for i in range(listLength):
        randList.append(randint(minValue, maxValue))
    return randList

def ListSumOdd(myList):
    sum = 0
    for i in range(1, len(myList), 2):
        sum += myList[i]
    return sum
