def Transmute(polynomial):
    for i in range(len(polynomial)):
        if '*x^' in polynomial[i]:
            polynomial[i] = polynomial[i].split('*x^')
        elif '*x' in polynomial[i]:
            polynomial[i] = polynomial[i].split('*x')
            polynomial[i][-1] = '1'
        elif 'x^' in polynomial[i]:
            polynomial[i] = polynomial[i].split('x^')
            polynomial[i][0] = 1
        elif '+' not in polynomial[i] and '-' not in polynomial[i] and '=' not in polynomial[i]:
            polynomial[i] = [polynomial[i], '0']
    for i in range(len(polynomial)):
        if polynomial[i] == '-':
            polynomial[i + 1][0] = - int(polynomial[i + 1][0])
            polynomial[i + 1][1] = int(polynomial[i + 1][1])
        elif polynomial[i] == '+' or polynomial[i] == '=':
            polynomial[i + 1][0] = int(polynomial[i + 1][0])
            polynomial[i + 1][1] = int(polynomial[i + 1][1])
        else:
            polynomial[i][0] = int(polynomial[i][0])
            polynomial[i][1] = int(polynomial[i][1])
    for element in polynomial:
        if element == '-' or element == '+' or element == '=':
            polynomial.remove(element)
    return polynomial

def SumPolinomials(polynomialOne, polynomialTwo):
    polynomialRes = list()
    for i in range(len(polynomialOne) - 1):
        flagOne = False
        for j in range(len(polynomialTwo) - 1):
            if polynomialOne[i][1] == polynomialTwo[j][1]:
                polynomialRes.append([polynomialOne[i][0] + polynomialTwo[j][0] , polynomialOne[i][1]])
                flagOne = True
        if not flagOne:
            polynomialRes.append(polynomialOne[i])
    for j in range(len(polynomialTwo) - 1):
        flagTwo = False
        for k in range(len(polynomialRes)):
            if polynomialTwo[j][1] == polynomialRes[k][1]:
                flagTwo = True
        if not flagTwo:
            polynomialRes.append(polynomialTwo[j])
    polynomialRes.sort(key=lambda monomial: monomial[1], reverse=True)
    polynomialRes.append([polynomialOne[-1][0] + polynomialTwo[-1][0], 0])
    return  polynomialRes

def ConvertToStr(polynomial):
    OutputRes = ''
    for i in range(len(polynomial)):
        if polynomial[i][0] < 0 and polynomial[i][1] > 1:
            OutputRes += '- '
            OutputRes += str(-1 * polynomial[i][0]) + '*x^' + str(polynomial[i][1]) + ' '
        elif polynomial[i][0] < 0 and polynomial[i][1] == 1:
            OutputRes += '- '
            OutputRes += str(-1 * polynomial[i][0]) + '*x' + ' '
        elif polynomial[i][0] < 0 and polynomial[i][1] == 0:
            OutputRes += '- '
            OutputRes += str(-1 * polynomial[i][0]) + ' '
        elif polynomial[i][0] > 0 and polynomial[i][1] > 1:
            OutputRes += '+ '
            OutputRes += str(polynomial[i][0]) + '*x^' + str(polynomial[i][1]) + ' '
        elif polynomial[i][0] > 0 and polynomial[i][1] == 1:
            OutputRes += '+ '
            OutputRes += str(polynomial[i][0]) + '*x' + ' '
        elif polynomial[i][0] > 0 and polynomial[i][1] == 0:
            OutputRes += '+ '
            OutputRes += str(polynomial[i][0]) + ' '
    OutputRes += '= ' + str(polynomial[-1][0])
    return OutputRes