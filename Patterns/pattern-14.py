def printPattern(n):
    chars = ['A','B','C','D','E']
    for i in range(n):
        for j in range(i+1):
            print(chars[i],end="")
        print()

printPattern(5)

# A
# BB
# CCC
# DDDD
# EEEEE