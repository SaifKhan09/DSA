def sumNNumbers(n):
    if n == 0:
        return 0
    else:
        return n + sumNNumbers(n-1)
    
print(sumNNumbers(10))