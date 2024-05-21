def printPattern(n):
    for i in range(1,2*n):
        stars = i
        if i > n:
            stars = 2*n - i
        
        print("*" * stars)

printPattern(5)

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *