#859. Buddy Strings
#Difficulty: Easy
'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
Status: UD
Notes: thinking about getting the differences between the words and whatever characters are different, swap if it 
equals goal then good otherwise no. If there are more than 2 characters that are different return false. I and J
cannot be same index.
'''
def buddyStrings(s: str, goal: str) -> bool:
    a = 0
    b = 0
    for i,j in enumerate(zip(s,goal)):
        print(j)
        if i != j:
           a = i
    return True
x = buddyStrings("ab","cc")

print(x)
