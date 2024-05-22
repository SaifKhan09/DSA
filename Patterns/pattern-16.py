def printPattern(n):
    for i in range(2*n):
        if i < n:
            spaces = 2*i
            stars = n-i
        elif i == n:
            spaces = 2*(n-1)
            stars = n-i+1
        else:
            spaces = 2*(2*n - i - 1)
            stars = i-n+1
        for j in range(stars):
            print("*",end="")
        for k in range(spaces):
            print(" ",end='')
        for l in range(stars):
            print("*",end="")
        print()

printPattern(5)

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
