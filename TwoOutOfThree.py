from typing import List
#2032. Two Out of Three
#Difficulty: Easy

#Description: Given three integer arrays nums1, nums2, and nums3, 
#return a distinct array containing all the values that are present in at least two out of the three arrays. 
#You may return the values in any order.

#Progress: UNder Development 

#Note: Dumb solution literally hardcoded 


def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    return list(((set(nums1).intersection(set(nums2))).union(set(nums1).intersection(set(nums3)))).union(set(nums2).intersection(set(nums3))))
print(twoOutOfThree([1,1,3,2],[2,3],[3]))
