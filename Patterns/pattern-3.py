def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1," ",end="")
        print()

printPattern(5)

# 1  
# 1  2  
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5