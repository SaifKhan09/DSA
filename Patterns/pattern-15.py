def printPattern(n):
    chars = ['A','B','C','D']
    for i in range(n):
        for j in range(n-i):
            print(" ",end='')
        for k in range(i+1):
            print(chars[k],end='')
        for m in range(i,0,-1):
            print(chars[m-1],end='')
        for l in range(n-i):
            print(" ",end='')
        print()

printPattern(4)

#     A    
#    ABA   
#   ABCBA
#  ABCDCBA