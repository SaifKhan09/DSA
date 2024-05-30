def checkStringPalindrome(str,start,end):
    if start>=end:
        return True
    else:
        if str[start] == str[end]:
            return checkStringPalindrome(str,start+1,end-1)
        else:
            return False
        
string = 'ab'
print(checkStringPalindrome(string,0,len(string)-1))