import math as m
def armstrongNumber(x):
    n = x
    result = 0
    numberOfDigits = int(m.log(n,10)) + 1
    while n > 0:
        digit = n%10
        result += digit**numberOfDigits
        n = int(n/10)
    return result == x

print(armstrongNumber(371))