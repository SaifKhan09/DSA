def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end="")
        print("")

printPattern(4)

# * 
# * * 
# * * *
# * * * *