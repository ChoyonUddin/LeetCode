from typing import List
import timeit
#349. 
#Difficulty: Easy

#Description: Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must be unique and you may return the result in any order.

#Progress: Completed

#Note Timeit function was just there for testing 

start_time = timeit.default_timer()
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))  
print(intersection([4,9,5,3],[9,4,9,8,4]),timeit.default_timer()-start_time)