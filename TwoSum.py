#1. Two Sum
#Difficulty: Easy

#Description: Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Progress: Completed 

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    complement = {}
    for i in range(len(nums)):
        if target - nums[i] in complement:
            return(complement[target-nums[i]],i)
        else:
            complement[nums[i]] = i
