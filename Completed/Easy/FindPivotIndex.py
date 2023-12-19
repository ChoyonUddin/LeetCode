'''
Difficulty: Easy
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Status: Completed
Notes: lol i was trying to do it some next level way so that it would be more efficient but it would've required too many check for
my liking

if len(nums)>1:
        mid = len(nums)//2
        right = sum(nums[mid:len(nums)-1])
        left = sum(nums[0:mid])
        flip = "left"

        if right > left:
            flip = "right"
        check = flip

        print(f'{left},{right}')
        while check == flip:
            #two checks
            #check if mid is on the left most side
            #check if the smaller side is now the larger side 
            if mid == 0 or mid == len(nums)-1:
                return mid if right == mid or left == mid else -1
            if left == right:
                return mid
            
            if left > right:
                mid -= 1
                flip = "left"

            if left < right:
                mid += 1
                flip == "right"
        return -1
    return -1

'''
from typing import List
def pivotIndex(nums: List[int]) -> int:
    left = 0
    for count,i in enumerate(nums):
        if left == sum(nums) - i -left:
            return count   
        left += i
    return -1     
print(pivotIndex([1,7,3,6,5,6]))

