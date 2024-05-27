def printName(n):
    if n > 0:
        print("Saif")
        printName(n-1)
    else:
        return
printName(10)