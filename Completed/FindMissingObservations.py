#2028. Find Missing Observations
#Difficulty: Medium 
#Description: You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. 
#n of the observations went missing, and you only have the observations of m rolls. 
#Fortunately, you have also calculated the average value of the n + m rolls.
#You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.
#Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.
#The average value of a set of k numbers is the sum of the numbers divided by k.
#Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

#Progress: Completed 
#Notes: Lost the original file so this is just what I submitted on leetcode

def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = []
        missingSum = mean*(n+len(rolls)) - sum(rolls) 
        if missingSum < n or missingSum > n * 6:
            return []

        nextNum = missingSum//n
        remaining = missingSum%n

        for i in range(n):
            if i < remaining:
                res.append(nextNum + 1)
                continue
            res.append(nextNum)
            
        return res

'''Old Solution
import numpy as np
from typing import List
def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    mt = mean*(n+len(rolls)) - np.sum(rolls)
    mAvg = mt/n
    missingNumbers = []
    if 1<= mAvg <= 6:
        for i in range(n):
            if n > 0:
                missingNumbers.append((int)(np.ceil(mAvg)))
                mt -= (int)(np.ceil(mAvg))
                n -= 1
                mAvg = mt/n
        return(missingNumbers)
    return([])   
'''

 
 