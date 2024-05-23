def printDivisors1(x):
    n = 1
    while n < x:
        if x % n == 0:
            print(n,",",end=' ')
        n+=1
    print(x)
    
def printDivisors2(x):
     for i in range(1,int(x**0.5)):
         if x % i == 0:
            print(i,",",end=' ')
            if x/i != i:
                print(int(x/i),",",end=' ')
        
     
printDivisors1(36)
printDivisors2(36)