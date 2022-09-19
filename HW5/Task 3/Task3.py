myString = input("Enter your text with the symbols a-z: ")

def RLE(string):
    for number in range(10):
        if str(number) in string:
            return 'Your text should consist of letters a-z only.\n Try again.'
    result = ''
    count = 1
    for i in range(0, len(string)):
        letter = string[i]
        if i != len(string) - 1:
            if letter == string[i + 1]:
                count += 1
                if i == len(string) - 2:
                    result += str(count) + letter
            else:
                result += str(count) + letter
                letter = string[i + 1]
                count = 1
        else:
            if count == 1:
                result += str(count) + letter
    return result

print(RLE(myString))