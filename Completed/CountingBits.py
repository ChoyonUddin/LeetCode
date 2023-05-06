#338. Counting Bits
#Difficulty: Easy

#Description: Given an integer n, 
#return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
# of i.

#Progress: Completed 

#Notes:
from typing import List
'''OLD CODE
def countBits(n: int) -> List[int]:
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count("1"))
    return ans
print(countBits(4))
'''

def countBits(n: int) -> List[int]:
    return [bin(i).count("1") for i in range(n+1)]
print(countBits(4))