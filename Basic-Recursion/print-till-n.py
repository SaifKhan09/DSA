def printTillnForward(i,n):
    if i > n:
        return
    else:
        print(i)
        printTillnForward(i+1,n)
        
def printTillnBackward(n):
    if n == 0:
        return
    else:
        print(n)
        printTillnBackward(n-1)        

printTillnBackward(5)
printTillnForward(1,5)