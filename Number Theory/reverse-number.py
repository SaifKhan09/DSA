import math as m
def reverseNumber1(x):
    if x == 0:
        return 0
    if x < 0:
        isNegative = True
        x = x*(-1)
    else:
        isNegative = False
    result = 0
    numberOfDigits = int(m.log(x,10))
    while x > 0:
        digit = x%10
        result = result + int(digit*m.pow(10,numberOfDigits))
        numberOfDigits = numberOfDigits - 1
        x = int(x/10)
    if isNegative == True:
        return result*(-1)
    else:
        return result

def reverseNumber2(n):
    if(n == 0):
        return 0
    result = 0
    if n < 0:
        isNegative = True
        n = n*(-1)
    else:
        isNegative = False
    while n > 0:
        result = (result * 10) + (n % 10)
        n = int(n / 10)
    if isNegative == True:
        result = result*(-1)
    if result > 2 ** 31 - 1 or result < -2 ** 31:
        return 0

def reverseDigits3(x):
    x = str(x)
    isNegative = True if x[0] == '-' else False
    if isNegative:
        x = x[1:]
    x = x[::-1]
    x = int(x)
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0
    if isNegative:
        x = x*(-1)
    return x

# print(reverseDigits3(153423646))
# print(reverseNumber2(-124214))
# print(reverseNumber1(1534236469))