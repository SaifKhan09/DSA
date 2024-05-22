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

# i < n-1 star = n/2 , space = 2*(n-i-1) , star = i+1
# i = n-1 star = n , space = n-i-1 , start = n
# i > n-1 star = i-n + 1 , space = 2*(n-1)+1 - i , start = i -n +1


# n = 5
# row(i) star space star 
# 0       2    0     0 
# 1       1    2     1
# 2       1    2     1
# 3       2    0     2
# 4       5    0     5   
# 5       4    2     4         
# 6       3    4     3
# 7       2    6     2 
# 8       1    8     1 