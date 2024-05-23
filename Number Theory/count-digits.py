import math as m
def countDigits(n):
    result = 0
    while n > 0:
        result += 1
        n = int(n/10)
    print(result)

def countDigitsRecursive(n):
    if(n==0):
        return 0
    else:
        return 1 + countDigitsRecursive(int(n/10))
    
def countDigitsLog(n):
    return int(m.log(n,10)) + 1

countDigits(970980)
print(countDigitsRecursive(1237912131))
print(countDigitsLog(1237912131))