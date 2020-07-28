def isPalindrome(str,start,end):
    if start==end:
        return True
    elif start<end:
        if str[start] == str[end]:
            return isPalindrome(str,start+1,end-1)
        else:
            return False


st = "1racecar1"
print(isPalindrome(st,0,len(st)-1))