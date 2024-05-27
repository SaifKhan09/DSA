def checkPrime(n):
    if n==2:
        return True
    for i in range (1,int(n**0.5)+1):
        if i==1 or i == n:
            continue
        else:
            if n%i==0:
                return False
            else: 
                return True
            
print(checkPrime(103))