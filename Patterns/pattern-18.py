def printPattern(n):
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print("*", end=" ")
        else:
            print("*", end=" ")
            for j in range(n-2):
                print(" ", end=" ")
            print("*",end='')
        print()

printPattern(5)

# * * * * * 
# *       *
# *       *
# *       *
# * * * * *

