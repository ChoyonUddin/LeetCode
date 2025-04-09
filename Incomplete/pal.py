def isPalindrome(s: str):
    s.strip()
    res = ""
    for letter in s.lower():
        if letter.isalnum():
            res +=letter
    return(res == res[::-1])
print(isPalindrome(s = "Was it a car     or a cat I saw?  "))