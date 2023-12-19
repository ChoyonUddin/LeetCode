#125. Valid Palindrome
#Difficulty: Easy

#Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase 
#letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
#Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

#Progress: Completed 


def isPalindrome(s: str) -> bool:
    return s[::-1].lower() == s.lower() if s.isalnum() else False
print(isPalindrome("racecar"))

'''
    #OLD CODE
    newstring = ""
    for i in s.lower():
        if i.isalnum():
            newstring += i
    if newstring == newstring[::-1]:
        return True
    return False
'''   