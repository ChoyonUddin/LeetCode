#434. Number of Segments in a String
'''
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1

Difficulty: Easy Af
Status: Completed

Brute force cause i totally forgot split existed for a hot minute
'''
def countSegments(self, s: str) -> int:
        res = []
        r = ''
        s = s.lstrip(" ")
        for i in s:
            if i != " ":
                r += i
            elif r:
                res.append(r)
                r = ''
        if r:
            res.append(r)
        return len(res)

'''Easiest way lol
def countSegments(self, s: str) -> int:
       return len(s.split())
'''
