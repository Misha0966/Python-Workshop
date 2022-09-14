# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

userNum = input('Enter number:\n')


def GeneratePI(number):
    k = 0
    pi_res = formulaPI(k)
    k = 1
    pi_gen = pi_res + formulaPI(k)
    try:
        if '.' in number:
            accuracy = len(number.split('.')[1])
        else:
            accuracy = len(number.split(',')[1])
    except IndexError:
        return int(pi_res)       
    while pi_res * 10**accuracy // 1 != pi_gen * 10**accuracy // 1:
        k += 1
        pi_res = pi_gen
        pi_gen += formulaPI(k)
    return round(pi_res, accuracy)

def formulaPI(k):
    return (1 / 16**k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))


print(GeneratePI(userNum))