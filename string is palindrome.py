def ispalindrome(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return ispalindrome(s[1:-1])
        else:
            return False

string=str(input("Enter a string:"))
if(ispalindrome(string)==True):
    print("String is palindrome!")
else:
    print("String is not a palindrome!")
    
