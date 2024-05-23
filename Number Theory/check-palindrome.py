def checkPalindrome1(x):
    n = x
    result = 0
    isNegative = True if n < 0 else False
    if isNegative:
        return False
    while(n > 0):
        result = (result * 10) + (n % 10)
        n = int(n/10)
    
    return result == x

def checkPalindrome2(x):
    if x < 0:
        return False
    x = str(x)
    n = x[::-1]
    return x == n


print(checkPalindrome2(121))
print(checkPalindrome1(121))

            
    