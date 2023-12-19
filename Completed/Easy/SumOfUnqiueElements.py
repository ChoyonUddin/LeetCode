#1748. Sum of Unique Elements
#Difficulty: Easy

#Description: You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
#Return the sum of all the unique elements of nums

#Progress: Completed

from typing import List


def sumOfUnique(nums: List[int]):
    arr = []
    for i in nums:
        if nums.count(i) == 1:
            arr.append(i)
    return arr
           
print(sumOfUnique([1,2,3,2]))

'''
Dictionary attempted solution: Ignore this

 for i in range(len(nums)):
        if nums[i] not in mydic:
            mydic[nums[i]] = nums[i]
    if len(mydic) == 1:
            print(0)
    print(sum(mydic.values()))
    print(mydic)
sumOfUnique([1,2,3,4,5])
'''
