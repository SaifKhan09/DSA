def printPattern(n):
    for i in range(2*n - 1):
        if i < n-1:
            stars = i+1
            spaces = 2*(n-i-1)
        elif i == n-1:
            stars = n
            spaces = n-i-1
        else:
            stars = 2*(n-1)+1-i
            spaces = 2*(i-n+1)
        for j in range(stars):
            print("*", end = "")
        for k in range(spaces):
            print(" ",end='')
        for l in range(stars):
            print("*", end = "")
        print()

printPattern(5)

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *