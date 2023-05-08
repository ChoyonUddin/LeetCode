'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Status:Completed
Notes: Lmao i+1
'''
def runningSum(nums):
        return [sum(nums[0:i+1]) for i in range(len(nums))]
print(runningSum([1,3,6,9]))