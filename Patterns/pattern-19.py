def printPattern(n):
    for i in range(((2*n)-1)):
        for j in range((2*n)-1):
            top = i
            left = j
            bottom = (2*n-2) - i
            right = (2*n-2) - j
            print(n-min(top,bottom,right,left)," ",end="")
        print()

printPattern(4)


# 4  4  4  4  4  4  4
# 4  3  3  3  3  3  4
# 4  3  2  2  2  3  4
# 4  3  2  1  2  3  4
# 4  3  2  2  2  3  4
# 4  3  3  3  3  3  4
# 4  4  4  4  4  4  4