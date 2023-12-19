#278. FirstBadVersion
#Difficulty: Easy
import math
'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Status: Solved

Notes: Simple solution although I think there's a better more effective way about doing
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n: int) -> int:
    high,low = n,0
    
    while high > low:
        mid = (high+low)//2

        if isBadVersion(low) == False:
            return 0
        
        if isBadVersion(mid) == True:
            high = mid
        
        if isBadVersion(mid) == False:
            low = mid + 1
        
    return low
    
'''
import math
def firstBadVersion(n: int) -> int:
    target = math.ceil(n/2)
    last = target
    
    while target > 0:

        if target == n:
            return n
        if isBadVersion(last) != isBadVersion(target):
            return target
        
        if isBadVersion(target) == True:
            target -= 1
            last = target

        if isBadVersion(target) == False:
            last = target
            target += 1
    
        
        
    return target
'''
print(firstBadVersion(5))

#Given test case return false is good and true is bad 
def isBadVersion(n: int) -> bool:
        
        return False
  
        return True

