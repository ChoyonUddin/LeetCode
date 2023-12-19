'''
209.

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Difficulty: Medium
'''
from typing import List
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp,subSum,subLen = 0,0,len(nums)+1
        for rp in range(len(nums)):
            subSum += nums[rp]
            while subSum >= target:
                subLen = min(subLen,rp - lp+1)
                subSum -= nums[lp]
                lp+=1
        if subLen == len(nums)+1:
            return 0
        return subLen