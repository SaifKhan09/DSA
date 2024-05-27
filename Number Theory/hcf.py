def findHCF1(a,b):
    res = 1
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            res = i
            
    return res

# Equilodean theorm : hcf(a,b) == hcf(a-b,b) where a>b

def findHCF2(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        max_val = max(a,b)
        min_val = min(a,b)
        return findHCF2(max_val%min_val,min_val)

print(findHCF2(4,20))