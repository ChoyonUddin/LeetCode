#704. Binary Search
#Difficulty: Easy
from typing import List
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def search(nums: List[int], target: int) -> int:
    low,high = 0,len(nums) -1

    while low <= high:
        mid = low + (high-low) //2
      
        if nums[mid] == target:
            return mid  
        
        if nums[mid] > target:
            high = mid - 1 

        if nums[mid] < target:
            low = mid + 1
    return -1
            
print(search([-1,0,3,5,9,12],9))
