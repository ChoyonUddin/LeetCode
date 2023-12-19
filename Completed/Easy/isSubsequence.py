#392. is Subsequence
#Difficulty: Easy

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Status: Completed
Notes: This took way longer than it should have lol. Better solution in description of one of the solutions but sticking with mine fn
'''
def isSubsequence(s: str, t: str):
    for i in range(len(s)): #could have just done i in s
        lastIndex = t.find(s[i]) 
        t = t[lastIndex+1:]
        
        if lastIndex <= -1:
            return False
    return True
print(isSubsequence("aaaaaa","bbaaaa"))
