'''
20. Valid Parentheses
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''
def isValid(s: str) -> bool:
    s=s.strip("")
    # prev = s[0]
    dict = {'(':')','[':']','{':'}'}
    for i in range(len(s)-2):
        if s[i+1]!=dict[s[i]]:
            return False
        i+=1
    return True
print(isValid(s="({})"))